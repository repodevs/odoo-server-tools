from odoo.tools import config
from .otel import OdooUptrace, init_uptrace

# Init Tracing
tracing = OdooUptrace()
