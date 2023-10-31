from os import path


# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    app.add_html_theme('sphinx_documatt_theme', path.abspath(path.dirname(__file__)))
