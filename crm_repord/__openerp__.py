# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'CRM Repord',
    'version': '0.1',
    'category': '',
    'description': """
CRM Repord for mobile device
===================================
""",
    'author': 'Vertel AB',
    'website': 'http://www.vertel.se',
    'depends': ['sale', 'product', 'website', 'calendar_ics', 'calendar_kanban', 'crm_meeting', 'product_customer_code','l10n_se', 'sale_crm', 'website_imagemagick'], # product_customer_code from oca-addons-vauxoo
    'data': [
        'views/crm_repord_view.xml',
        'views/crm_repord_data.xml',
        'views/crm_repord_report.xml',
        'views/repord_view.xml',
        'wizard/repord_make_invoice.xml',
        'repord_data.xml',
        'security/ir.model.access.csv',
    ],
    'application': False,
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4s:softtabstop=4:shiftwidth=4:
