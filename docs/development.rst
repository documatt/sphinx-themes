***********
Development
***********

Themes has names ``sphinx_<name>_theme``, e.g. sphinx_documatt_theme. Folder ``sphinx_<name>_theme/`` is Python package. Theme sources itself are in ``sphinx_<name>_theme/sphinx_<name>_theme/`` folder.

Theme markup and styles are based on amazing `Bulma.io <https://bulma.io>`_ CSS framework. Theme source folder itself is NPM project preconfigured with Bulma, SASS, PostCSS and Babel. Heavily based on `Bulma start package <https://bulma.io/bulma-start/>`_. It means you need Node.js and NPM installed.

It means you need to build SCSS and ES6. In theme source folder ``sphinx_<name>_theme/sphinx_<name>_theme/``, execute::

    # first-time only
    npm i
    npm run deploy

SCSS in ``_sass/main.scss`` will become ``static/css/main.css``, JS in ``_javascript/main.js`` will become ``static/js/main.js``. These two output files are referred from the Sphinx theme as normally.

If you want to build your theme, execute in project root::

    scripts/build_theme <theme_name>
