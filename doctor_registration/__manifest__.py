{
    'name': 'Doctor Registration',
    'version': '1.0',
    'sequence': -100,
    'author': 'Zafir Abdullah',
    'category': 'Doctor',
    'summary': 'Docter registration system',
    'description': 'Docter registration system',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/doctor_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
