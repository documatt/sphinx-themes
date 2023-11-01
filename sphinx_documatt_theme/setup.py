from setuptools import setup

setup(
    name='sphinx_documatt_theme',
    version='0.0.6',
    url='http://documatt.com/sphinx-themes/themes/documatt.html',
    license='BSD3',
    author='Documatt.com',
    author_email='hello@documatt.com',
    description='Documatt Theme for Sphinx documentation projects',
    long_description=open('README.rst', encoding='utf-8').read(),
    packages=['sphinx_documatt_theme'],
    package_data={
        "": ["theme.conf", "*.html", "static/js/*", "static/css/*", "static/img/*", "static/css/fonts/*"]
    },
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points={
        'sphinx.html_themes': [
            'sphinx_documatt_theme = sphinx_documatt_theme',
        ]
    },
    install_requires=[
        'sphinx'
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
