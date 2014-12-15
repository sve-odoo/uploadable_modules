see_translations
================

Compatibility
-------------
Odoo 8.0: OK

Abstract
--------
This module adds a button on the "ir_ui_view" form: "See translations"
If you click on it:
* If you are in a QWeb view, you will
  * See all translations that apply on your view
  * If you click on "Create", just fill the source, destination & language to translate a new term. The other values are filled by default to apply on your QWeb view.
* If you are in another view, you will
  * See all translations of type "view" that apply on the same model
  * The default values are set to create new "view" translations for the same model
