# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'sphinx-themes'
copyright = '2023, Documatt.com'
author = 'Documatt.com'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_sitemap"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_baseurl = 'https://documatt.com/sphinx-themes/'
html_extra_path = ['robots.txt']

html_theme = 'sphinx_documatt_theme'
html_theme_path = ['../sphinx_documatt_theme']
html_theme_options = {
    'motto': 'A collection of themes for the Sphinx documentation projects. Themes suitable both for a documentation and a prose.',
    'header_text': project,

    'header_logo_style': 'width: 3rem; margin-right: 1rem;',
    'footer_logo_style': 'width: 3rem;'
}
html_logo = html_favicon = '../icons8-change-theme-64.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# --- Options for sphinx-sitemap ---------------------------------------------

# No lang code in generated URLs
sitemap_url_scheme = "{link}"


def setup(app):
    app.add_object_type('confval', 'confval',
                        objname='configuration value',
                        indextemplate='pair: %s; configuration value')
