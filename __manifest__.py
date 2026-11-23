{
    'name': 'Partner Auto Sequence',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'summary': 'Automatic customer and supplier numbering',
    'description': """
Automatic customer and supplier numbering
=========================================

Assign an automatic reference to partners on creation:

* customers get a reference from the ``partner.sequence`` sequence;
* suppliers get a reference from the ``supplier.sequence`` sequence.

A manually provided reference is never overwritten.
""",
    'author': 'HOUARI',
    'license': 'LGPL-3',
    'website': 'https://github.com/MrH0u/partner_auto_sequence',
    'depends': ['base'],
    'data': [
        'data/sequence.xml',
    ],
    'installable': True,
    'application': False,
}