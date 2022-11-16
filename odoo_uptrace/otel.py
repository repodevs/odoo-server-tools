# -*- coding: utf-8 -*-
from odoo.release import version as odoo_version
from odoo.tools import config
from odoo.http import request as orequest
from odoo.http import Response

import uptrace
from opentelemetry import trace as oteltrace
from opentelemetry.trace import (
    NonRecordingSpan,
    SpanContext,
    SpanKind,
    TraceFlags,
    Link,
)
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

IGNORE_TRACING_RESPONSE_CLASS_NAME = [
    # 'HomePatch',
    # 'WebClientPatch',
    # 'ProxyPatch',
    # 'DatabasePatch',
    # 'SessionPatch',
    # 'DataSetPatch',
    # 'ViewPatch',
    "BinaryPatch",
    # 'ActionPatch',
    "ExportPatch",
    "CSVExportPatch",
    "ExcelExportPatch",
    # 'ReportControllerPatch',
]


class OdooUptrace:
    """
    Tracer that can trace certain requests to Odoo app.
    @param tracer the OpenTelemetry tracer implementation to trace requests with
    """

    def __init__(self, tracer=None):

        self._service_name = config.get("uptrace_service_name", "odoo.webservice")
        self._uptrace_dsn = config.get("uptrace_dsn", "")
        self._uptrace_version = uptrace.__version__

        if not callable(tracer):
            self.__tracer = oteltrace.get_tracer("uptrace", self._uptrace_version)
            self.__tracer_getter = None
        else:
            self.__tracer = None
            self.__tracer_getter = tracer

        self._current_spans = {}

        # Init Uptrace
        uptrace.configure_opentelemetry(
            dsn=self._uptrace_dsn,
            service_name=self._service_name,
            service_version=odoo_version,
        )
        # print(f"Uptrace Configured: {self._service_name} - {self._uptrace_dsn}")

    @property
    def tracer(self):
        if not self.__tracer:
            if self.__tracer_getter is None:
                return oteltrace.get_tracer(self._service_name, self._uptrace_version)
            self.__tracer = self.__tracer_getter()
        return self.__tracer

    def trace(self, *attributes):
        """
        Function decorator that traces functions
        NOTE: Must be placed after the @app.route decorator
        @param attributes any number of odoo.request attributes
        (strings) to be set as tags on the created span
        """

        def decorator(f):
            def wrapper(*args, **kwargs):
                attr = {"attributes": attributes, "kwargs": kwargs, "fn": f}
                self._before_request_fn(attr, f)
                try:
                    r = f(*args, **kwargs)
                except Exception as e:
                    self._after_request_fn(f, error=e)
                    raise
                self._after_request_fn(f, response=r)
                return r

            wrapper.__name__ = f.__name__
            return wrapper

        return decorator

    def _before_request_fn(self, attributes, fn):
        """Trace before request"""
        request = orequest.httprequest
        operation_name = request.url
        cls_patch_name = self._extract_cls_patch_name(fn)
        odooattr = self._extract_odoo_attrs(attributes)
        headers = {}
        for k, v in request.headers:
            headers[k.lower()] = v

        try:
            parentContext = TraceContextTextMapPropagator().extract(headers)
            span = self.tracer.start_span(
                operation_name,
                context=parentContext,
                # links=[Link(ctx)],
                # links=[Link(parentContext)],
            )
        except Exception as e:
            print(e)
            span = self.tracer.start_span(operation_name)

        self._current_spans[request] = span

        span.set_attribute("component", "Odoo")
        span.set_attribute("span.kind", "server")
        span.set_attribute("http.method", request.method)
        span.set_attribute("http.url", request.base_url)
        span.set_attribute("odoo.patchname", cls_patch_name)
        span.set_attribute("odoo.method", fn.__name__)
        span.set_attribute("odoo.model", odooattr.get("model"))
        span.set_attribute("odoo.model.id", odooattr.get("id"))

        if cls_patch_name == "BinaryPatch":
            span.set_attribute("odoo.model.field", odooattr.get("field"))

        if cls_patch_name in IGNORE_TRACING_RESPONSE_CLASS_NAME:
            pass

    def _after_request_fn(self, fn, response=None, error=None):
        request = orequest.httprequest
        span = self._current_spans.pop(request, None)
        if span is None:
            return

        ignore_response_data = False
        if self._extract_cls_patch_name(fn) in IGNORE_TRACING_RESPONSE_CLASS_NAME:
            ignore_response_data = True

        if response is not None:
            if response and isinstance(response, Response):
                rmsg = "<ignored>" if ignore_response_data else response.data
                span.set_attribute("http.status_code", response.status_code)
                response.direct_passthrough = False
                span.set_attribute("odoo.respose.data", rmsg)
            else:
                rmsg = "<ignored>" if ignore_response_data else response
                span.set_attribute("http.status_code", 200)
                span.set_attribute("odoo.respose.data", str(rmsg))

        if error is not None:
            span.set_attribute("error", True)
            span.record_exception(error)

        # print(self._extract_cls_patch_name(fn), " -> ", uptrace.trace_url(span))
        # print("end span")
        span.end()

    def _extract_odoo_attrs(self, datas):
        """Extract common odoo attributes
        - model -> e.g: sale.order, sale.order.line
        - model.id -> e.g: 1, 2, 3
        """
        res = {"model": None, "id": 0}
        try:
            res["model"] = datas.get("kwargs", {}).get("model", None)
            try:
                oid = datas.get("kwargs", {}).get("args", [[0]])[0][0]
                if oid == 0:
                    oid = datas.get("kwargs", {}).get("id", 0)
                res["id"] = oid
            except Exception as ee:
                print(ee)
                pass
            # for binary field
            if self._extract_cls_patch_name(datas.get("fn", None)) == "BinaryPatch":
                res["field"] = datas.get("kwargs", {}).get("field", None)
        except Exception as e:
            print(e)
            pass
        finally:
            return res

    def _extract_cls_patch_name(self, fn):
        """Extract Class patch name"""
        cls_name = None
        try:
            cls_name = fn.__qualname__.split(".")[0]
        except Exception as e:
            print(e)
            pass
        finally:
            return cls_name
