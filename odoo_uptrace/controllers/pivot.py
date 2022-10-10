from odoo import http
from odoo.addons.web.controllers.pivot import TableExporter

from ..tracer import tracing

class TableExporterPatch(TableExporter):
    @http.route()
    @tracing.trace()
    def check_xlsxwriter(self):
        return super(TableExporterPatch, self).check_xlsxwriter()

    @http.route()
    @tracing.trace()
    def export_xlsx(self, data, **kw):
        return super(TableExporterPatch, self).export_xlsx(data **kw)
