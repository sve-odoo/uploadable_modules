create_report
==================

Compatibility
-------------
Odoo 8.0: [x]

Abstract
--------
This modules add a menu item in Settings / Technical / Reports: "Create new report"
This wizard automates all boring and touchy tasks you have to manually perform when creating a report from scratch:
* Creating the document QWeb view
** Copying the structure form an existing report, including the internal/external layout t-call.
* Creating an XMLID for it
* If the report is translatable,
** Creating a "translator" Qweb view
** Creating an XMLID for it
* Creating the Report record
* Creating an action binding

