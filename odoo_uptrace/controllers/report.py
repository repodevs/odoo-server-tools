from odoo import http
from odoo.addons.web.controllers.report import ReportController

from ..tracer import tracing


class ReportControllerPatch(ReportController):
    @http.route()
    @tracing.trace()
    def report_routes(self, reportname, docids=None, converter=None, **data):
        return super(ReportControllerPatch, self).report_routes(
            reportname, docids, converter, **data
        )

    @http.route()
    @tracing.trace()
    def report_barcode(self, barcode_type, value, **kwargs):
        return super(ReportControllerPatch, self).report_barcode(
            barcode_type, value, **kwargs
        )

    @http.route()
    @tracing.trace()
    def report_download(self, data, context=None, token=None):
        return super(ReportControllerPatch, self).report_download(data, context, token)

    @http.route()
    @tracing.trace()
    def check_wkhtmltopdf(self):
        return super(ReportControllerPatch, self).check_wkhtmltopdf()
