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

from openerp.osv import orm, fields
import openerp.addons.decimal_precision as dp


class PurchaseOrder(orm.Model):
    _inherit = 'purchase.order'

    _columns = {
        'rate_eur': fields.float(
            'EUR Rate when confirmed', digits=(12, 6),
            readonly=True,
            help='The rate used when the order was confirmed'),
        'rate_usd': fields.float(
            'USD Rate when confirmed', digits=(12, 6),
            readonly=True,
            help='The rate used when the order was confirmed'),
        'amount_untaxed_eur': fields.float(
            'EUR Untaxed',
            digits_compute=dp.get_precision('Account'),
            readonly=True,
            help='Untaxed Amount in EUR '
            'computed at when the order is confirmed',
        ),
        'amount_untaxed_usd': fields.float(
            'USD Untaxed',
            digits_compute=dp.get_precision('Account'),
            readonly=True,
            help='Untaxed Amount in USD '
            'computed at when the order is confirmed',
        ),
    }

    def wkf_confirm_order(self, cr, uid, ids, context=None):
        super(PurchaseOrder, self).wkf_confirm_order(cr, uid, ids, context)

        currency_obj = self.pool['res.currency']
        mod_obj = self.pool['ir.model.data']
        eur_id = mod_obj.get_object_reference(cr, uid, 'base', 'EUR')[1]
        usd_id = mod_obj.get_object_reference(cr, uid, 'base', 'USD')[1]
        eur, usd = currency_obj.browse(cr, uid, [eur_id, usd_id],
                                       context=context)

        for order in self.browse(cr, uid, ids, context=context):
            order.write({
                'rate_eur': currency_obj._get_conversion_rate(
                    cr, uid, order.currency_id, eur, context=context),
                'rate_usd': currency_obj._get_conversion_rate(
                    cr, uid, order.currency_id, usd, context=context),
                'amount_untaxed_eur': currency_obj.compute(
                    cr, uid, order.currency_id.id, eur_id,
                    order.amount_untaxed, context=context),
                'amount_untaxed_usd': currency_obj.compute(
                    cr, uid, order.currency_id.id, usd_id,
                    order.amount_untaxed, context=context),
            })

        return True

    def copy_data(self, cr, uid, id, default, context):
        if default is None:
            default = {}

        default.update({
            field: 0.0 for field in ('rate_eur', 'amount_untaxed_eur',
                                     'rate_usd', 'amount_untaxed_usd')
        })

        return super(PurchaseOrder, self).copy_data(cr, uid, id, default,
                                                    context)
