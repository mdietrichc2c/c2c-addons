# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Leonardo Pistone
#    Copyright 2014 Camptocamp SA
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
    'name': 'Sale Alternate Currency',
    'version': '1.0',
    'category': 'Generic Modules/Sale',
    'description': """
Sale Alternate Currency
=======================

This module shows the value untaxed total of the sale order in two, fixed
alternate currencies. These two currencies are hardcoded.

The totals are written at the moment when the order is confirmed. The rate
used is stored, too.

Contributors
------------

  * Leonardo Pistone <leonardo.pistone@camptocamp.com>

""",
    'author': 'Camptocamp',
    'depends': ['sale'],
    'website': 'http://www.camptocamp.com',
    'data': [
        'view/sale.xml',
    ],
    'test': [
        'test/set_rate.yml',
        'test/sale_alternate_currency.yml',
    ],
    'demo': [],
    'installable': True,
    'active': False,
}
