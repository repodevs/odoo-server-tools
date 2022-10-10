from odoo import http
from odoo.addons.web.controllers.binary import Binary

from ..tracer import tracing


class BinaryPatch(Binary):
    @http.route()
    @tracing.trace()
    def content_filestore(self, _path):
        return super(BinaryPatch, self).content_filestore(_path)

    @http.route()
    @tracing.trace()
    def content_common(
        self,
        xmlid=None,
        model="ir.attachment",
        id=None,
        field="raw",
        filename=None,
        filename_field="name",
        mimetype=None,
        unique=False,
        download=False,
        access_token=None,
        nocache=False,
    ):
        return super(BinaryPatch, self).content_common(
            xmlid,
            model,
            id,
            field,
            filename,
            filename_field,
            mimetype,
            unique,
            download,
            access_token,
            nocache,
        )

    @http.route()
    @tracing.trace()
    def content_assets(
        self, id=None, filename=None, unique=False, extra=None, nocache=False
    ):
        return super(BinaryPatch, self).content_assets(
            id, filename, unique, extra, nocache
        )

    @http.route()
    @tracing.trace()
    def content_image(
        self,
        xmlid=None,
        model="ir.attachment",
        id=None,
        field="raw",
        filename_field="name",
        filename=None,
        mimetype=None,
        unique=False,
        download=False,
        width=0,
        height=0,
        crop=False,
        access_token=None,
        nocache=False,
    ):
        return super(BinaryPatch, self).content_image(
            xmlid,
            model,
            id,
            field,
            filename_field,
            filename,
            mimetype,
            unique,
            download,
            width,
            height,
            crop,
            access_token,
            nocache,
        )

    @http.route()
    @tracing.trace()
    def upload_attachment(self, model, id, ufile, callback=None):
        return super(BinaryPatch, self).upload_attachment(model, id, ufile, callback)

    @http.route()
    @tracing.trace()
    def company_logo(self, dbname=None, **kw):
        return super(BinaryPatch, self).company_logo(dbname, **kw)

    @http.route()
    @tracing.trace()
    def get_fonts(self, fontname=None):
        return super(BinaryPatch, self).get_fonts(fontname)
