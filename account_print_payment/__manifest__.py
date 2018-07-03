# -*- coding: utf-8 -*-
{
    'name': 'Account Print Payment',
    'version': '1.0',
    'category': 'Account',
    'description': "",
    'author': "Abdul Nazar, Parker Randall",
    'depends': ['base', 'account', 'amount_to_word_base'],
    'data': [
        'report/report.xml',
        'report/report_payment.xml'
#        'wizard/account_report_aged_partner_balance_view.xml',
            ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 10,
    'currency': 'USD',
    'license': 'AGPL-3'	

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
