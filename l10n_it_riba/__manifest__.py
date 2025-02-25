# Copyright (C) 2012 Andrea Cometa.
# Email: info@andreacometa.it
# Web site: http://www.andreacometa.it
# Copyright (C) 2012 Associazione OpenERP Italia
# (<http://www.odoo-italia.org>).
# Copyright (C) 2012-2017 Lorenzo Battistini - Agile Business Group
# Copyright (C) 2019 Sergio Zanchetta - Associazione PNLUG
# Copyright 2023 Simone Rubino - Aion Tech
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "ITA - Ricevute bancarie",
    "version": "16.0.1.5.1",
    "development_status": "Beta",
    "author": "Odoo Community Association (OCA)",
    "category": "Localization/Italy",
    "summary": "Ricevute bancarie",
    "website": "https://github.com/OCA/l10n-italy",
    "license": "AGPL-3",
    "depends": [
        "account",
        "account_due_list",
        "l10n_it_fatturapa_out",
        "l10n_it_fiscalcode",
        "base_iban",
        "l10n_it_abicab",
    ],
    "data": [
        "data/riba_sequence.xml",
        "report/report.xml",
        "security/ir.model.access.csv",
        "security/riba_security.xml",
        "views/wizard_credit.xml",
        "views/wizard_past_due.xml",
        "views/riba_view.xml",
        "views/account_view.xml",
        "views/configuration_view.xml",
        "views/partner_view.xml",
        "views/wizard_riba_issue.xml",
        "views/wizard_riba_file_export.xml",
        "views/account_config_view.xml",
        "views/slip_report.xml",
        "views/riba_detail_view.xml",
        "views/wizard_presentation.xml",
        "views/wizard_due_date_settlement.xml",
    ],
    "demo": ["demo/riba_demo.xml"],
    "installable": True,
}
