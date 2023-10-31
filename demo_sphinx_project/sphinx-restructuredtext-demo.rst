.. _sphinx-additions:

==================================================
Sphinx additions to reStructuredText Demonstration
==================================================

The following section is showcase of Sphinx additions to reStructuredText -- directives and roles that are not in Docutils.

.. contents:: Table of Contents

Reference roles
===============

Sphinx adds few roles for referencing across its documentation:

* ref role for reference to arbitrary location in any document, e.g. :ref:`sphinx-additions`,
* doc role for reference to document, e.g. :doc:`index`
* download role to create downloadable link :download:`screenshot.png`
* term role to reference to glossary's term :term:`term1`

Semantic roles
===============

* abbr role for abbreviation, e.g. :abbr:`LIFO (last-in, first-out)`
* command OS-level command, e.g. :command:`rm -rf`
* file for printing file paths with optional placeholder :file:`/usr/lib/python{version}/site-packages`
* kbd for printing keyboard shortcuts. E.g. compound shortcut :kbd:`Ctrl-Alt-Delete` or just a key name :kbd:`F12`.
* guilabel for referring buttons and control's labels in GUI, e.g. :guilabel:`Cancel` or with accelerator key :guilabel:`&Cancel`.
* menuselection for paths in GUI menu, e.g. :menuselection:`Start --> Programs`
* program for names of executable problems, e.g. :program:`sphinx-build -q -b html source build`
* regex for showing regular expressions, e.g. :regexp:`//[^\r\n]*[\r\n]`
* samp role for literal text with placeholders, e.g. :samp:`print 1+{variable}`

Directives
==========

code-block
----------

Sphinx adds code-block directive that can syntax highlight, number lines, emphasis lines, and have a caption.

.. code-block:: javascript
   :caption: Caption of a code-block
   :emphasize-lines: 2
   :linenos:

   // line numbered code block with JavaScript syntax highlighting
   for (let i = 0; i < 3; i++) {        // line 2 should be emphasised
       alert(i);
   }

Last option for showing code examples is parsed-literal directive. It can’t highlight code as code-block, but allows you to use reStructuredText inline markup (emphasis, hyperlinks, etc.). Very useful e.g. for terminal session examples.

literal-include

toctree
-------

toctree directive define a *global Table of Contents (global TOC)*, i.e. ordering of documents in project.

The directive in action is seen in :doc:`index` page.

versionadded
-------------

.. versionadded:: 2.5
   The *spam* parameter.

versionchanged
--------------

.. versionchanged:: 2.8
   Newly accepts only ``str``.

deprecated
----------

.. deprecated:: 3.1
   Use :func:`spam` instead.

seealso
-------

.. seealso::

   More can be found at foo website.

hlist
-----

This directive must contain a bullet list. It will transform it into a more compact list by either distributing more than one item horizontally, or reducing spacing between items, depending on the builder.

.. hlist::
   :columns: 3

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally

Glossary
--------

.. glossary::

   term1
      term1 is ...

   term2
      term2 to is ...

   multiple
   terms
   can share
   definition
      In contrast to regular definition lists, multiple terms per entry are allowed, and inline markup is allowed in terms. You can link to all of the terms.

   environment
      A structure where information about all documents under the root is
      saved, and used for cross-referencing.  The environment is pickled
      after the parsing stage, so that successive runs only need to read
      and parse new and changed documents.

   source directory
      The directory which, including its subdirectories, contains all
      source files for one Sphinx project.

   term 1 : A
   term 2 : B
      Definition of both terms. If you want to specify “grouping key” for general index entries, you can put a “key” as “term : key”. For example:

sectionauthor and codeauthor
----------------------------

Identifies the author of the current section, or code. It maybe hidden if `show_authors <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-show_authors>`_ option is ``False``.

.. sectionauthor:: Guido van Rossum <guido@python.org>

.. codeauthor:: Guido van Rossum <guido@python.org>

productionlist
--------------

This directive is used to enclose a group of productions. Each production is given on a single line and consists of a name, separated by a colon from the following definition. If the definition spans multiple lines, each continuation line must begin with a colon placed at the same column as in the first line.

.. productionlist::
   try_stmt: try1_stmt | try2_stmt
   try1_stmt: "try" ":" `suite`
            : ("except" [`expression` ["," `target`]] ":" `suite`)+
            : ["else" ":" `suite`]
            : ["finally" ":" `suite`]
   try2_stmt: "try" ":" `suite`
            : "finally" ":" `suite`
