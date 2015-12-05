# -*- coding: utf-8 -*-
{
    'name': "Bees Member", 

    'summary': """
		Module to manage bees member
     """,

    'description': """
        Module to manage bees member
        
        
        
        
    """,

    'author': "Bees ",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/task_type.xml',
        'views/task.xml',
        'views/res_users.xml',
        'views/day_template.xml',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
