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
#    'stanford_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output

def setup(app):
    app.add_css_file('./_static/custom.css')

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
#import os, sys
#on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

#if not on_rtd:  # only import and set the theme if we're building docs locally
#    import stanford_theme
#    html_theme = 'stanford_theme'
#    html_theme_path = ['_themes/stanford_theme']
#    html_sidebars = []
    
    #html_theme_path = [stanford_theme.get_html_theme_path()]

# otherwise, readthedocs.org uses their theme by default, so no need to specify it


html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}


# -- Options for EPUB output
epub_show_urls = 'footnote'
