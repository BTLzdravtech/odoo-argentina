import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


@openupgrade.migrate()
def migrate(env, version):
    cr = env.cr

    _logger.info("START add l10n_ar_fiscal_position_id to account_payment")
    openupgrade.add_columns(env, [
        ("account_payment", "l10n_ar_fiscal_position_id", "integer"),
    ])
    _logger.info("END add l10n_ar_fiscal_position_id to account_payment")


    _logger.info("START add withholdable_advanced_amount to account_payment")
    openupgrade.add_columns(env, [
        ("account_payment", "withholdable_advanced_amount", "float"),
    ])
    _logger.info("END add withholdable_advanced_amount to account_payment")


    _logger.info("START add l10n_ar_withholding_line_ids to account_payment")
    openupgrade.add_columns(env, [
        ("account_payment", "l10n_ar_withholding_line_ids", "integer"),
    ])
    _logger.info("END add l10n_ar_withholding_line_ids to account_payment")
