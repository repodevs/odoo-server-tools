from odoo import http
from odoo.addons.web.controllers.view import View

from ..tracer import tracing


class ViewPatch(View):
    @http.route()
    @tracing.trace()
    def edit_custom(self, custom_id, arch):
        return super(ViewPatch, self).edit_custom(custom_id, arch)
