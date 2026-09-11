from odoo import api, models


class ResCurrency(models.Model):
    _inherit = "res.currency"

    @api.model
    def _search_by_name(self, currency_name):
        """Extend currency lookup with the ARCA code for Argentine companies."""
        parent_search = getattr(super(), "_search_by_name", None)
        currencies = parent_search(currency_name) if parent_search else self.search([("name", "=", currency_name)])
        if self.env.company.account_fiscal_country_id.code == "AR":
            currencies |= self.search([("l10n_ar_afip_code", "=", currency_name)])
        return currencies
