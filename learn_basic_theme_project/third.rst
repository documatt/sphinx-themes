.. Template blocks documentation master file, created by
   sphinx-quickstart on Tue Jul 28 14:12:47 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Third document
===============

.. epigraph:: reStructuredText is used for documentation and books. Snippets is online editor with preview useful for learning and testing reStructuredText and Sphinx without installing it.

.. tip:: The following text shows just a very little of reStructuredText. For more examples and description of reStructuredText see for example https://blog.documatt.com/restructuredtext-sphinx/index.html.

***************
Inline elements
***************

Paragraphs may contain *emphasised*, **strong emphasised** words. Links to external webs like https://blog.documatt.com are auto-recognized. Sometimes you need ``monospaced text``. Useful are also :sup:`superscript` or :sub:`subscript`.

*****
Lists
*****

Unordered lists usually use ``*`` as bullet symbol:

* A bullet list item
* Second item
* A sub item

Ordered (enumerated) lists that is auto-numbered starts with ``#.``:

#. one
#. two
#. three

*********************
Showing code examples
*********************

It's easy to show code parts with ``inline literal``, or literal block::

  some literal text

Or, literal block with syntax highlighting:

.. code-block:: javascript

   for (let i = 0; i < 3; i++) {        // shows 0, then 1, then 2
       alert(i);
   }


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
