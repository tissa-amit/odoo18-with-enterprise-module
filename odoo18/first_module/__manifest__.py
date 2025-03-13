{
    'name': 'First Module',
    'version': '1.0',
    'category': 'Sales',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/first_module_views.xml',
    ],
    'installable': True,
    'application': True,
}
