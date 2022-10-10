from odoo import http
from odoo.addons.web.controllers.webclient import WebClient

from ..tracer import tracing


class WebClientPatch(WebClient):
    @http.route()
    @tracing.trace()
    def load_locale(self, lang):
        return super(WebClientPatch, self).load_locale(lang)

    @http.route()
    @tracing.trace()
    def bootstrap_translations(self, mods=None):
        return super(WebClientPatch, self).bootstrap_translations(mods)

    @http.route()
    @tracing.trace()
    def translations(self, unique, mods=None, lang=None):
        return super(WebClientPatch, self).translations(unique, mods, lang)

    @http.route()
    @tracing.trace()
    def version_info(self):
        return super(WebClientPatch).version_info()

    @http.route()
    # @tracing.trace() # NOTE: no need to trace tests
    def test_suite(self, mod=None, **kwargs):
        return super(WebClientPatch, self).test_suite(mod, **kwargs)

    @http.route()
    # @tracing.trace() # NOTE: no need to trace tests
    def test_mobile_suite(self, mod=None, **kwargs):
        return super(WebClientPatch, self).test_mobile_suite(mod, **kwargs)

    @http.route()
    # @tracing.trace() # NOTE: no need to trace tests
    def benchmarks(self, mod=None, **kwargs):
        return super(WebClientPatch, self).benchmarks(mod, **kwargs)

    @http.route()
    @tracing.trace()
    def bundle(self, bundle_name, **bundle_params):
        return super(WebClientPatch, self).bundle(bundle_name, **bundle_params)
