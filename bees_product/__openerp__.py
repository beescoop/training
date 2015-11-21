# -*- coding: utf-8 -*-
{
    'name': "Bees Member", 

    'summary': """
		Module extend product for beescoop
     """,

    'description': """
    """,

    'author': "Bees ",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product.xml',
        'data/colors.xml',
    ],
    # only loaded in demonstration mode
}
