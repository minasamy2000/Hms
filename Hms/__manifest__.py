# -*- coding: utf-8 -*-
{
    'name': "Hms Hospital",
    'summary': """ """,
    'description': """ """,
    'author': "Mina samy",
    'category': 'Productivity',
    'version': '16.0.1.0',
    'depends': ['base','sale'],
    'application': True,
    'installable': True,
    'data': [
        'security/rules_record.xml',
        'security/seuirty_groups.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/patient.xml',
        'views/department.xml',
        'views/doctor.xml',
        'reports/patient_report.xml',
        'reports/doctor_report.xml',
        'views/partner.xml',
         # 'views/contacts.xml'

    ],
}