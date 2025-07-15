# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api


class AccountInvoiceReport(models.Model):

    _inherit = 'account.invoice.report'

    # @api.model
    # def get_view(self, view_id=None, view_type="form", **options):
    #     if view_type == "tree" and self.env.company.country_code == "AR":
    #         view_id = self.env.ref("l10n_ar_ux.view_account_invoice_line_report_tree_ar").id
    #     return super().get_view(view_id=view_id, view_type=view_type, **options)
