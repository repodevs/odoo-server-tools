from odoo import http
from odoo.addons.web.controllers.home import Home

from ..tracer import tracing


class HomePatch(Home):
    @http.route()
    @tracing.trace()
    def index(self, s_action=None, db=None, **kw):
        return super(HomePatch, self).index(s_action, db, **kw)

    # ideally, this route should be `auth='user'` but that don't work in non-monodb mode.
    @http.route()
    @tracing.trace()
    def web_client(self, s_action=None, **kw):
        return super(HomePatch, self).web_client(s_action, **kw)

    @http.route()
    @tracing.trace()
    def web_load_menus(self, unique):
        return super(HomePatch, self).web_load_menus(unique)

    @http.route()
    @tracing.trace()
    def web_login(self, redirect=None, **kw):
        return super(HomePatch, self).web_login(redirect, **kw)

    @http.route()
    @tracing.trace()
    def login_successful_external_user(self, **kwargs):
        return super(HomePatch, self).login_successful_external_user(**kwargs)

    @http.route()
    @tracing.trace()
    def switch_to_admin(self):
        return super(HomePatch, self).switch_to_admin()

    @http.route()
    @tracing.trace()
    def health(self):
        return super(HomePatch, self).health()
