from odoo import http
from odoo.addons.web.controllers.dataset import DataSet

from ..tracer import tracing


class DataSetPatch(DataSet):
    @http.route()
    @tracing.trace()
    def search_read(
        self, model, fields=False, offset=0, limit=False, domain=None, sort=None
    ):
        return super(DataSetPatch, self).search_read(
            model, fields, offset, limit, domain, sort
        )

    @http.route()
    @tracing.trace()
    def load(self, model, id, fields):
        return super(DataSetPatch, self).load(model, id, fields)

    @http.route()
    @tracing.trace()
    def call(self, model, method, args, domain_id=None, context_id=None):
        return super(DataSetPatch, self).call(
            model, method, args, domain_id, context_id
        )

    @http.route()
    @tracing.trace()
    def call_kw(self, model, method, args, kwargs, path=None):
        return super(DataSetPatch, self).call_kw(model, method, args, kwargs, path)

    @http.route()
    @tracing.trace()
    def call_button(self, model, method, args, kwargs):
        return super(DataSetPatch, self).call_button(model, method, args, kwargs)

    @http.route()
    @tracing.trace()
    def resequence(self, model, ids, field="sequence", offset=0):
        return super(DataSetPatch, self).resequence(model, ids, field, offset)
