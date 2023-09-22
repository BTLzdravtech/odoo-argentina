##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models, api, _
from odoo.tools import float_round


class AccountMoveChangeRate(models.TransientModel):
    _name = 'account.move.change.rate'
    _description = 'account.move.change.rate'

    @api.model
    def get_move(self):
        move = self.env['account.move'].browse(
            self._context.get('active_id', False))
        return move

    currency_rate = fields.Float(
        'Currency Rate',
        required=True,
        digits=(16, 6),
        help="Select a rate to apply on the invoice"
    )
    move_id = fields.Many2one(
        'account.move',
        default=get_move
    )

    day_rate = fields.Boolean(
        string="Use currency rate of the day", help="The currency rate on the invoice date will be used. If the invoice does not have a date, the currency rate will be used at the time of validation.")

    @api.onchange('move_id')
    def _onchange_move(self):
        self.currency_rate = self.move_id.l10n_ar_currency_rate or self.move_id.computed_currency_rate

    def confirm(self):
        # Agrego este contexto para obtenerlo desde el modulo account_invoice_tax y evitar que se recompute el monto (amount_currency ) de los impuestos fijos
        # al cambiar la cotizacion de la moneda
        # Si bien no seria necesario si no esta instalado este modulo, nos evita un modulo puente
        context = {
                'tax_list_origin': self.move_id.mapped('invoice_line_ids.tax_ids'),
                'tax_total_origin': self.move_id.tax_totals
        }
        if self.day_rate:
            message = _("Currency rate changed from %s to %s") % (self.move_id.l10n_ar_currency_rate or self.move_id.computed_currency_rate, float_round(self.move_id.computed_currency_rate,2))
            self.move_id.with_context(context).l10n_ar_currency_rate = 0.0
        else:
            message = _("Currency rate changed from %s to %s . Currency rate forced") % (float_round(self.move_id.l10n_ar_currency_rate or self.move_id.computed_currency_rate, 2), float_round(self.currency_rate, 2))
            self.move_id.with_context(context).l10n_ar_currency_rate = self.currency_rate
        self.move_id.message_post(body=message)
        return {'type': 'ir.actions.act_window_close'}
