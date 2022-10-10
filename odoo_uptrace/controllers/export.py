from odoo import http
from odoo.addons.web.controllers.export import (
    Export,
    CSVExport,
    ExcelExport,
)

from ..tracer import tracing


class ExportPatch(Export):
    @http.route()
    @tracing.trace()
    def formats(self):
        return super(ExportPatch, self).formats()

    @http.route()
    @tracing.trace()
    def get_fields(
        self,
        model,
        prefix="",
        parent_name="",
        import_compat=True,
        parent_field_type=None,
        parent_field=None,
        exclude=None,
    ):
        return super(ExportPatch, self).get_fields(
            model,
            prefix,
            parent_name,
            import_compat,
            parent_field_type,
            parent_field,
            exclude,
        )

    @http.route()
    @tracing.trace()
    def namelist(self, model, export_id):
        return super(ExportPatch, self).namelist(model, export_id)


class CSVExportPatch(CSVExport):
    @http.route()
    @tracing.trace()
    def index(self, data):
        return super(CSVExportPatch, self).index(data)


class ExcelExportPatch(ExcelExport):
    @http.route()
    @tracing.trace()
    def index(self, data):
        return super(ExcelExportPatch, self).index(data)
