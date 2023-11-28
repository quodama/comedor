# -*- coding: utf-8 -*-
{
    'name': "Gestión de Comedor Solidario",

    'summary': """
        Sistema de Gestión de Comedor Solidario""",

    'description': """
        Módulo desarrollado para la gestión de aprendizaje electrónico
    """,

    'author': "Universidad Intercultural Amawtay Wasi",
    'website': "http://www.salesias.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'], #Instalan antes de usarse el módulo actual
    

    # always loaded
    'data': [
        #data
        #security
        "security/sis_comedor_security.xml",
        'security/ir.model.access.csv',
        #Views
        'views/sis_comedor_menu.xml',
        'views/sis_comedor_beneficiario_views.xml',
        'views/sis_comedor_asistencia_views.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
