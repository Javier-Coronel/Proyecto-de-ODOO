# -*- coding: utf-8 -*-
{
    'name': "taller",

    'summary': """
        Taller mecánico de vehículos""",

    'description': """
        Módulo para gestionar un taller mecánico de vehículos.
    """,

    'author': "MechaSerranitos",
    'website': "https://www.mesonserranito.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/repuesto_views.xml'
        'views/servicio_views.xml'
        'views/orden_reparacion_view.xml',
        'views/vehiculo_view.xml',
        'views/menu_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}