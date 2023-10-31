========================================
Demo Sphinx and reStructuredText project
========================================

About
=====

This Sphinx documentation project demonstrates almost all possible syntax you can use with Sphinx. If you develop a theme, build this project with your theme to see if everything is properly styled.

Demo documents
==============

Some themes show global TOC in sidebar, but you can place in document body like here:

.. toctree::
   :maxdepth: 3

   restructuredtext-demo
   sections

Optionally, it can have caption. For example "Sphinx specific" like here:

.. toctree::
   :maxdepth: 3
   :caption: Sphinx specific

   sphinx-restructuredtext-demo
   sphinx-apidocs-demo

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
