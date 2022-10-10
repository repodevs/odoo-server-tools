from odoo import http
from odoo.addons.web.controllers.database import Database

from ..tracer import tracing


class DatabasePatch(Database):
    @http.route()
    @tracing.trace()
    def selector(self, **kw):
        return super(DatabasePatch, self).selector(**kw)

    @http.route()
    @tracing.trace()
    def manager(self, **kw):
        return super(DatabasePatch, self).manager(**kw)

    @http.route()
    @tracing.trace()
    def create(self, master_pwd, name, lang, password, **post):
        return super(DatabasePatch, self).create(
            master_pwd, name, lang, password, **post
        )

    @http.route()
    @tracing.trace()
    def duplicate(self, master_pwd, name, new_name):
        return super(DatabasePatch, self).duplicate(master_pwd, name, new_name)

    @http.route()
    @tracing.trace()
    def drop(self, master_pwd, name):
        return super(DatabasePatch, self).drop(master_pwd, name)

    @http.route()
    @tracing.trace()
    def backup(self, master_pwd, name, backup_format="zip"):
        return super(DatabasePatch, self).backup(master_pwd, name, backup_format)

    @http.route()
    @tracing.trace()
    def restore(self, master_pwd, backup_file, name, copy=False):
        return super(DatabasePatch, self).restore(master_pwd, backup_file, name, copy)

    @http.route()
    @tracing.trace()
    def change_password(self, master_pwd, master_pwd_new):
        return super(DatabasePatch, self).change_password(master_pwd, master_pwd_new)

    @http.route()
    @tracing.trace()
    def list(self):
        return super(DatabasePatch, self).list()
