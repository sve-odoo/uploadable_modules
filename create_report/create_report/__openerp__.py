# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013-Today OpenERP SA (<http://www.openerp.com>).
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
    'name': 'Create new reports',
    'category': 'Custo',
    'summary': 'Module to help creating new QWeb reports',
    'version': '1.0',
    'description': """
        Module to help creating new QWeb reports
        """,
    'author': 'Odoo SA Professional Services',
    'data': [
        'data/models.xml',
        'data/values.xml',
        'data/ir_actions_server.xml',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
}
