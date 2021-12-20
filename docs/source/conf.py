# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'AK - Metadaten'
copyright = 'GDI-DI'
author = 'GDI-DE'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'stanford_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import stanford_theme
    html_theme = 'stanford_theme'
    html_theme_path = [stanford_theme.get_html_theme_path()]

# otherwise, readthedocs.org uses their theme by default, so no need to specify it


#html_theme = 'sphinx_rtd_theme'


# -- Options for EPUB output
epub_show_urls = 'footnote'
