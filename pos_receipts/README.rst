==============================
POS Custom Receipt – Odoo 19
==============================

.. image:: banner.png
:alt: POS Custom Receipt Banner
:align: center

Overview
========

**POS Custom Receipt** is an Odoo 19 module that enhances the default Point of Sale receipt layout.
It provides a clean, professional, and fully customized POS receipt including company name,
tax details, cashier information, itemized sales,total quantity, total items, totals, and QR code support.

This module is ideal for restaurants, retail stores, supermarkets, and businesses that require
a branded, clear, and customer-friendly POS receipt.

Key Features
============

* Custom POS receipt layout with professional design
* Displays company branding:

  * Company logo
  * Company name and address
  * VAT / TAXnumber
  * Phone, email, and website

* Sales information included:

  * Receipt number
  * Cashier name
  * Date and time
  * S.No.
  * Product description
  * Quantity and price per item
  * Discount
  * Subtotal (Untaxed Amount)
  * Tax amount
  * Grand total
  * Payment method



Installation
============

1. Copy the module into your Odoo addons directory.
2. Activate **Developer Mode**.
3. Go to **Apps → Update Apps List**.
4. Search for **POS Custom Receipt**.
5. Click **Install**.

Configuration
=============

No additional configuration is required.

(Optional Customization)
------------------------

* Modify receipt layout:
  `static/src/xml/pos_receipt.xml`
* Update logo or styles:
  `static/src/css/receipt.css`
* Customize QR code logic (if applicable):
  Python or JS extension can be added

How It Works
============

* When a POS order is validated, the system generates a customized receipt.
* The receipt pulls live data from the POS order:

  * Company details
  * Order lines
  * Taxes and totals
  * Payment method
  * Cashier information

* A QR code is generated and printed on the receipt.
* The receipt is printed automatically or shown as a PDF, depending on POS settings.

Use Cases
=========

* Retail stores
* Fashion and apparel shops
* Electronics stores
* Supermarkets
* VAT-compliant businesses
* Businesses requiring branded POS receipts

Requirements
============

* Odoo 19 Community or Enterprise
* Point of Sale module enabled
* Compatible thermal printer (optional)

Support & Contact
=================

For support, customization, or professional implementation services, please contact:

Website: https://www.hidxet.com.pk Email: asrarhnd@gmail.com

License
=======

AGPL-3

Changelog
=========

Version 1.0.0
-------------

* Initial release
* Custom POS receipt layout
* Company branding support
* Tax and total breakdown
* QR code support
