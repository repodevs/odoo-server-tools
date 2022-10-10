# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.web.controllers.main import (
    serialize_exception,
    Home,
    WebClient,
    Proxy,
    Database,
    Session,
    DataSet,
    View,
    Binary,
    Action,
    Export,
    CSVExport,
    ExcelExport,
    ReportController,
)

from ..otel import OdooUptrace, init_uptrace

tracing = OdooUptrace(init_uptrace("odoo.webservice"))

# ----------------------------------------------------------
# Odoo Web web Controllers Patch
# ----------------------------------------------------------


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
    def web_db_redirect(self, redirect="/", **kw):
        return super(HomePatch, self).web_db_redirect(redirect, **kw)

    @http.route()
    @tracing.trace()
    def web_login(self, redirect=None, **kw):
        return super(HomePatch, self).web_login(redirect, **kw)

    @http.route()
    @tracing.trace()
    def switch_to_admin(self):
        return super(HomePatch, self).switch_to_admin()


class WebClientPatch(WebClient):
    @http.route()
    @tracing.trace()
    def csslist(self, mods=None):
        return super(WebClientPatch, self).csslist(mods)

    @http.route()
    @tracing.trace()
    def jslist(self, mods=None):
        return super(WebClientPatch, self).jslist(mods)

    @http.route()
    @tracing.trace()
    def load_locale(self, lang):
        return super(WebClientPatch, self).load_locale(lang)

    @http.route()
    @tracing.trace()
    def qweb(self, unique, mods=None, db=None):
        return super(WebClientPatch, self).qweb(unique, mods, db)

    @http.route()
    @tracing.trace()
    def bootstrap_translations(self, mods):
        return super(WebClientPatch, self).bootstrap_translations(mods)

    @http.route()
    @tracing.trace()
    def translations(self, unique, mods=None, lang=None):
        return super(WebClientPatch, self).translations(unique, mods, lang)

    @http.route()
    @tracing.trace()
    def version_info(self):
        return super(WebClientPatch, self).version_info()

    @http.route()
    @tracing.trace()
    def test_suite(self, mod=None, **kwargs):
        return super(WebClientPatch, self).test_suite(mod, **kwargs)

    @http.route()
    @tracing.trace()
    def test_mobile_suite(self, mod=None, **kwargs):
        return super(WebClientPatch, self).test_mobile_suite(mod, **kwargs)

    @http.route()
    @tracing.trace()
    def benchmarks(self, mod=None, **kwargs):
        return super(WebClientPatch, self).benchmarks(mod, **kwargs)


class ProxyPatch(Proxy):
    @http.route()
    @tracing.trace()
    def post(self, path):
        return super(ProxyPatch, self).post(path)


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
    def change_password(self, fields):
        return super(SessionPatch, self).change_password(fields)

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
    def save_session_action(self, the_action):
        return super(SessionPatch, self).save_session_action(the_action)

    @http.route()
    @tracing.trace()
    def get_session_action(self, key):
        return super(SessionPatch, self).get_session_action(key)

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


class ViewPatch(View):
    @http.route()
    @tracing.trace()
    def edit_custom(self, custom_id, arch):
        return super(ViewPatch, self).edit_custom(custom_id, arch)


class BinaryPatch(Binary):
    @http.route()
    @tracing.trace()
    def content_common(
        self,
        xmlid=None,
        model="ir.attachment",
        id=None,
        field="datas",
        filename=None,
        filename_field="name",
        unique=None,
        mimetype=None,
        download=None,
        data=None,
        token=None,
        access_token=None,
        **kw
    ):
        return super(BinaryPatch, self).content_common(
            xmlid,
            model,
            id,
            field,
            filename,
            filename_field,
            unique,
            mimetype,
            download,
            data,
            token,
            access_token,
            **kw
        )

    @http.route()
    @tracing.trace()
    def content_image_partner(
        self, rec_id, field="image_128", model="res.partner", **kwargs
    ):
        return super(BinaryPatch, self).content_image_partner(
            rec_id, field, model, **kwargs
        )

    @http.route()
    @tracing.trace()
    def content_image(
        self,
        xmlid=None,
        model="ir.attachment",
        id=None,
        field="datas",
        filename_field="name",
        unique=None,
        filename=None,
        mimetype=None,
        download=None,
        width=0,
        height=0,
        crop=False,
        access_token=None,
        **kwargs
    ):
        return super(BinaryPatch, self).content_image(
            xmlid,
            model,
            id,
            field,
            filename_field,
            unique,
            filename,
            mimetype,
            download,
            width,
            height,
            crop,
            access_token,
            **kwargs
        )

    @http.route()
    @tracing.trace()
    def content_image_backward_compatibility(self, model, id, field, resize=None, **kw):
        return super(BinaryPatch, self).content_image_backward_compatibility(
            model, id, field, resize, **kw
        )

    @http.route()
    @tracing.trace()
    @serialize_exception
    def upload(self, callback, ufile):
        return super(BinaryPatch, self).upload(callback, ufile)

    @http.route()
    @tracing.trace()
    @serialize_exception
    def upload_attachment(self, callback, model, id, ufile):
        return super(BinaryPatch, self).upload_attachment(callback, model, id, ufile)

    @http.route()
    @tracing.trace()
    def company_logo(self, dbname=None, **kw):
        return super(BinaryPatch, self).company_logo(dbname, **kw)

    @http.route()
    @tracing.trace()
    def get_fonts(self, fontname=None):
        return super(BinaryPatch, self).get_fonts(fontname)


class ActionPatch(Action):
    @http.route()
    @tracing.trace()
    def load(self, action_id, additional_context=None):
        return super(ActionPatch, self).load(action_id, additional_context)

    @http.route()
    @tracing.trace()
    def run(self, action_id):
        return super(ActionPatch, self).run(action_id)


class ExportPatch(Export):
    @http.route()
    @tracing.trace()
    def formats(self):
        return super(ExportPatch, self).formats()

    @http.route()
    @tracing.trace()
    def get_fields(
        self,
        model,
        prefix="",
        parent_name="",
        import_compat=True,
        parent_field_type=None,
        parent_field=None,
        exclude=None,
    ):
        return super(ExportPatch, self).get_fields(
            model,
            prefix,
            parent_name,
            import_compat,
            parent_field_type,
            parent_field,
            exclude,
        )

    @http.route()
    @tracing.trace()
    def namelist(self, model, export_id):
        return super(ExportPatch, self).namelist(model, export_id)


class CSVExportPatch(CSVExport):
    @http.route()
    @tracing.trace()
    @serialize_exception
    def index(self, data, token):
        return super(CSVExportPatch, self).index(data, token)


class ExcelExportPatch(ExcelExport):
    @http.route()
    @tracing.trace()
    @serialize_exception
    def index(self, data, token):
        return super(ExcelExportPatch, self).index(data, token)


class ReportControllerPatch(ReportController):
    @http.route()
    @tracing.trace()
    def report_routes(self, reportname, docids=None, converter=None, **data):
        return super(ReportControllerPatch, self).report_routes(
            reportname, docids, converter, **data
        )

    @http.route()
    @tracing.trace()
    def report_barcode(self, type, value, **kwargs):
        return super(ReportControllerPatch, self).report_barcode(type, value, **kwargs)

    @http.route()
    @tracing.trace()
    def report_download(self, data, token, context=None):
        return super(ReportControllerPatch, self).report_download(data, token, context)

    @http.route()
    @tracing.trace()
    def check_wkhtmltopdf(self):
        return super(ReportControllerPatch, self).check_wkhtmltopdf()
