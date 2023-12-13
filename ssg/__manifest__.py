# -*- coding: utf-8 -*-
{
    'name': "ssg",

    'summary': """
        Módulo de SSG""",

    'description': """
        Proyecto SSG.
    """,

    'author': "Daniel",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/proyecto_report.xml',
        'security/ssg_regla_registro.xml',
        
        # 'security/incidencias_reglas_registro.xml',
        # 'reports/municipios_report.xml',
        # 'reports/municipios_report_view.xml',
        # 'data/product_category_data.xml', FUNCIONA, PERO NO DEJA ACTUALIZAR SI ESTA AQUI
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': 'True',
    'sequence': 1,

    # assets
    'assets': {
        'web.assets_common':[
            'ssg/static/src/scss/style1.scss',
        ],
    }
}
