========================
ITA - Ritenute d'acconto
========================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:3705d8ac89650a80494b22aa6d623ae079694439862a9a3df35035d5507f40d9
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fl10n--italy-lightgray.png?logo=github
    :target: https://github.com/OCA/l10n-italy/tree/16.0/l10n_it_withholding_tax
    :alt: OCA/l10n-italy
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/l10n-italy-16-0/l10n-italy-16-0-l10n_it_withholding_tax
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/l10n-italy&target_branch=16.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

La ritenuta d’acconto provvede a calcolare automaticamente i valori
delle diverse tipologie di ritenuta presenti nella contaiblità italiana.

Con questo modulo è possibile, tramite apposito workflow, gestire i
diversi passaggi di stato delle ritenute rilevate: dovuta, applicata,
versata

**Table of contents**

.. contents::
   :local:

Usage
=====

Per prima cosa dovremo creare una ritenuta d’acconto dove inserire tutti
i campi necessari per un corretto calcolo.

Visto che le aliquote possono variare nel corso del tempo, nella
codifica sono previsti scaglioni temporali di competenza.

E’ necessario anche inserire i conti contabili che verranno utilizzati
quando il modulo si occuperà di generare registrazioni contabili per la
rilevazione della ritenuta.

|image1|

Una volta aggiunta, nella tabella ritenute, potrà essere utilizzata
all’interno della fattura, in corrispondenza delle righe soggette a
ritenute.

Per ogni riga è possibile utilizzare più di una ritenuta. Per alcune
casistiche il moduo ritenute viene usato anche per rilevare le
trattenute INPS.

Il modulo ritenute calcolerà i valori corrispondenti e ne mostrerà il
dettaglio nell’apposita area ritenute, dove è possibile verificare per
ogni codice ritenuta usato, l’imponibile e l’importo ritenuta applicato.

In calce ai totali, verrà totalizzato l’ammontare della ritenuta e il
netto a pagare. Questa sezione sarà visibile solamente in presenza di
almeno una ritenuta

|image2|

Per registrare il pagamento di una fattura con ritenuta, indicare come
importo il "Netto a pagare" e lasciare aperta la fattura:

|image3|

Il sistema provvederà alla creazione di un ulteriore pagamento che
coprirà l'ammontare della ritenuta e la fattura risulterà completamente
pagata:

|image4|

Per il pagamento della ritenuta d'acconto fare riferimento al modulo
l10n_it_withholding_tax_payment.

Successivamente andando nella sezione situazione ritenute d’acconto il
sistema vi mostrerà una situazione riepilogativa delle varie ritenute
divisa per documento di origine.

I campi principalmente da tenere in considerazione in questa tabella
sono: ritenuta dovuta, ritenuta applicata e ritenuta versata.

*Ritenuta dovuta* contiene il valore della ritenuta contenuta nella
fattura.

*Ritenuta applicata* mostra il valore della ritenuta rilevata al momento
del pagamento della fattura.

*Ritenuta versata* contiene l’importo di ritenuta, già applicata, che è
stata versata all’erario

|image5|

.. |image1| image:: https://raw.githubusercontent.com/OCA/l10n-italy/16.0/l10n_it_withholding_tax/static/img/ritenuta-acconto-odoo-codifica-768x457.png
.. |image2| image:: https://raw.githubusercontent.com/OCA/l10n-italy/16.0/l10n_it_withholding_tax/static/img/fattura-fornitore-768x517.png
.. |image3| image:: https://raw.githubusercontent.com/OCA/l10n-italy/16.0/l10n_it_withholding_tax/static/img/pagamento-fattura-fornitore.png
.. |image4| image:: https://raw.githubusercontent.com/OCA/l10n-italy/16.0/l10n_it_withholding_tax/static/img/pagamento-ritenuta.png
.. |image5| image:: https://raw.githubusercontent.com/OCA/l10n-italy/16.0/l10n_it_withholding_tax/static/img/foto-3-1-1024x505.png

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/l10n-italy/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/l10n-italy/issues/new?body=module:%20l10n_it_withholding_tax%0Aversion:%2016.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Openforce
* Odoo Italia Network

Contributors
------------

-  Alessandro Camilli <alessandrocamilli@openforce.it>
-  Lorenzo Battistini <lorenzo.battistini@agilebg.com>
-  Marco Colombo <https://github.com/TheMule71>
-  Alex Comba <alex.comba@agilebg.com>

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/l10n-italy <https://github.com/OCA/l10n-italy/tree/16.0/l10n_it_withholding_tax>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
