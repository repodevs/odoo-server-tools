from odoo import http
from odoo.addons.web.controllers.action import Action

from ..tracer import tracing

class ActionPatch(Action):
    @http.route()
    @tracing.trace()
    def load(self, action_id, additional_context=None):
        return super(ActionPatch, self).load(action_id, additional_context)

    @http.route()
    @tracing.trace()
    def run(self, action_id):
        return super(ActionPatch, self).run(action_id)
