# Author(s): Silvio Gregorini (silviogregorini@openforce.it)
# Copyright 2019 Openforce Srls Unipersonale (www.openforce.it)
# Copyright 2023 Simone Rubino - Aion Tech
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "ITA - Gestione Cespiti",
    "version": "16.0.1.0.1",
    "category": "Localization/Italy",
    "summary": "Gestione Cespiti",
    "author": "Openforce, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-italy",
    "license": "AGPL-3",
    "depends": [
        "account",
        "account_financial_report",
        "account_fiscal_year",
        "mail",
    ],
    "data": [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "security/rules.xml",
        "data/ir_cron.xml",
        "data/asset_data.xml",
        "report/layout.xml",
        "report/paperformat.xml",
        "report/templates/asset_journal.xml",
        "report/templates/asset_previsional.xml",
        "report/reports.xml",
        "views/asset_menuitems.xml",
        "views/account_move.xml",
        "views/asset.xml",
        "views/asset_accounting_info.xml",
        "views/asset_category.xml",
        "views/asset_depreciation.xml",
        "views/asset_depreciation_line.xml",
        "views/asset_depreciation_line_type.xml",
        "views/asset_depreciation_mode.xml",
        "views/asset_depreciation_type.xml",
        "views/asset_tag.xml",
        "wizard/account_move_manage_asset_view.xml",
        "wizard/asset_generate_depreciation_view.xml",
        "wizard/asset_journal_report_view.xml",
        "wizard/asset_previsional_report_view.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "l10n_it_asset_management/static/src/js/*",
            "l10n_it_asset_management/static/src/xml/*",
        ],
    },
    "development_status": "Beta",
    "installable": True,
    "external_dependencies": {
        "python": [
            "openupgradelib",
        ],
    },
    "pre_init_hook": "pre_absorb_old_module",
}
