from odoo import http
from odoo.addons.web.controllers.profiling import Profiling

from ..tracer import tracing


class ProfilingPatch(Profiling):
    @http.route()
    @tracing.trace()
    def profile(self, profile=None, collectors=None, **params):
        return super(ProfilingPatch, self).profile(profile, collectors, **params)

    @http.route()
    @tracing.trace()
    def speedscope(self, profile=None):
        return super(ProfilingPatch, self).speedscope(profile)
