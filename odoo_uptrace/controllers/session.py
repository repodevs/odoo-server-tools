from odoo import http
from odoo.addons.web.controllers.session import Session

from ..tracer import tracing


class SessionPatch(Session):
    @http.route()
    @tracing.trace()
    def get_session_info(self):
        return super(SessionPatch, self).get_session_info()

    @http.route()
    @tracing.trace()
    def authenticate(self, db, login, password, base_location=None):
        return super(SessionPatch, self).authenticate(
            db, login, password, base_location
        )

    @http.route()
    @tracing.trace()
    def get_lang_list(self):
        return super(SessionPatch, self).get_lang_list()

    @http.route()
    @tracing.trace()
    def modules(self):
        return super(SessionPatch, self).modules()

    @http.route()
    @tracing.trace()
    def check(self):
        return super(SessionPatch, self).check()

    @http.route()
    @tracing.trace()
    def account(self):
        return super(SessionPatch, self).account()

    @http.route()
    @tracing.trace()
    def destroy(self):
        return super(SessionPatch, self).destroy()

    @http.route()
    @tracing.trace()
    def logout(self, redirect="/web"):
        return super(SessionPatch, self).logout(redirect)
