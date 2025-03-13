{
    'name': 'My Hospital',  
    'version': '1.0',  
    'category': 'Unique',  
    'depends': ['base','contacts'],  
    'data': [   
        'security/ir.model.access.csv',
        'views/my_hospital_views.xml',
        'views/extended_views.xml',
        'report/my_hospital_report.xml',   

    ],  
    'images': ['static/description/icon.png'],
    
    'installable': True,
    'application': True,
}




