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
import sphinx_rtd_theme
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'miaaim'
copyright = '2021, Joshua Hess'
author = 'Joshua Hess'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
"sphinx_rtd_theme",
"sphinx.ext.autodoc",
"sphinx.ext.viewcode",
"nbsphinx",
"sphinx.ext.githubpages",
"sphinx_rtd_theme"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'
#highlight_language = 'python3'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
#html_logo = "logo.png"

html_theme_options = {
#    'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
#    'analytics_anonymize_ip': False,
    'logo_only': False,
    # 'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '5DADE2',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_context = {
  'display_github': True,
  'github_user': 'JoshuaHess12',
  'github_repo': 'miaaim',
  'github_version': '0.0.1',
}

#html_logo = "logo.tif"

nbsphinx_allow_errors = True

html_sidebars = { '**': ['localtoc.html', 'globaltoc.html', 'searchbox.html'] }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]
