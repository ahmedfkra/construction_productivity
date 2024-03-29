# -*- coding: utf-8 -*-
{
    'name': "construction_productivity",

    'summary': "Construction project management module",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/project_info.xml',
        'views/equipment_info.xml',
        'views/crusher_views.xml',
        'views/mixer_management.xml',
        'views/worker_info.xml',
        'report/crusher.xml',
        'report/crusher_template.xml',
        # 'views/report.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
