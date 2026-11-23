=====================
Partner Auto Sequence
=====================

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status

.. |badge2| image:: https://img.shields.io/badge/license-LGPL--3-blue.png
    :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html

|badge1| |badge2|

This module assigns an automatic reference to contacts when they are created:

* customers receive a reference from the ``partner.sequence`` sequence;
* suppliers receive a reference from the ``supplier.sequence`` sequence.

A reference entered manually is never overwritten.

**Table of contents**

.. contents::
   :local:

Configuration
=============

The two sequences (``partner.sequence`` and ``supplier.sequence``) are
installed automatically with the module, with the prefixes ``CUS-`` and
``SUP-`` and a padding of 5 (e.g. ``CUS-00001``).

Go to *Settings > Technical > Database Structure > Sequences* to change the
prefix, padding or numbering.

Usage
=====

Create a customer or a supplier. The *Reference* field is filled in
automatically.

.. note::

   If a partner is created first and later marked as a customer or supplier,
   the reference is not generated retroactively. Set the customer/supplier
   rank at creation time, or fill the reference manually.

Known issues / Roadmap
======================

* When a partner is both a customer and a supplier at creation time, the
  supplier sequence takes precedence.
* In a database where the sequences already exist manually (created from the
  user interface before installing this module), remove those duplicates to
  avoid two sequences sharing the same code.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/MrH0u/partner_auto_sequence/issues>`_.

Credits
=======

Authors
-------

* HOUARI

License
=======

This module is licensed under the GNU Lesser General Public License v3
(LGPL-3). See the ``LICENSE`` file for the full text.
