# Part of Odoo. See LICENSE file for full copyright and licensing details.

import warnings
from odoo import http
from odoo.tools import lazy
from odoo.addons.web.controllers import (
    utils,
    binary as obinary,
    database as odatabase,
    home as ohome,
    export as oexport,
    webclient as owebclient,
)

from odoo.addons.odoo_uptrace.controllers import (
    action,
    binary,
    database,
    dataset,
    export,
    home,
    report,
    session,
    view,
    webclient,
)

_MOVED_TO_MAP = {
    "_get_login_redirect_url": utils,
    "_local_web_translations": owebclient,
    "Action": action,
    "allow_empty_iterable": oexport,
    "Binary": binary,
    "clean": obinary,
    "clean_action": utils,
    "content_disposition": http,
    "CONTENT_MAXAGE": owebclient,
    "CSVExport": export,
    "Database": database,
    "DataSet": dataset,
    "DBNAME_PATTERN": odatabase,
    "ensure_db": utils,
    "ExcelExport": export,
    "Export": export,
    "ExportFormat": oexport,
    "ExportXlsxWriter": oexport,
    "fix_view_modes": utils,
    "generate_views": utils,
    "GroupExportXlsxWriter": oexport,
    "GroupsTreeNode": oexport,
    "Home": home,
    "none_values_filtered": oexport,
    "OPERATOR_MAPPING": oexport,
    "ReportController": report,
    "Session": session,
    "SIGN_UP_REQUEST_PARAMS": ohome,
    "View": view,
    "WebClient": webclient,
}


def __getattr__(attr):
    module = _MOVED_TO_MAP.get(attr)
    if not module:
        raise AttributeError(f"Module {__name__!r} has not attribute {attr!r}.")

    @lazy
    def only_one_warn():
        warnings.warn(
            f"{__name__!r} has been split over multiple files, you'll find {attr!r} at {module.__name__!r}",
            DeprecationWarning,
            stacklevel=4,
        )
        return getattr(module, attr)

    return only_one_warn
