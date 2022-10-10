# -*- coding: utf-8 -*-
{
    "name": "Odoo Uptrace",
    "summary": """Odoo Uptrace Module""",
    "description": """
        Odoo Uptrace Integration

    # Setup

    - install `uptrace` depedencies `pip install uptrace`

    - set `uptrace_dsn` in odoo.conf file or set envvar `UPTRACE_DSN`
    """,
    "author": "Edi Santoso",
    "website": "https://me.repodevs.com",
    "category": "Technical Settings",
    "version": "0.1",
    "depends": ["web"],
    "external_dependencies": {
        "python": ["uptrace"],
    },
}
