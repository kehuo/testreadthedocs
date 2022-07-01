# Configuration file for the Sphinx documentation builder.

# path setup
import os
import sys

sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath(""))

# -- Project information

project = "test read the docs"
copyright = "2022, hk"
author = "hk"

release = "9.9"
version = "9.9.9"

# -- General configuration

# autosummary supports display class members.
extensions = [
    # "sphinx.ext.duration",
    # "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "recommonmark",
    "sphinx.ext.autosummary",
    # "sphinx.ext.intersphinx",
]

# supports .rst and .md source files.
source_suffix = [".rst", ".md"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output
# epub_show_urls = "footnote"

# html_theme_options = {
#     'collapse_navigation': True,
#     'display_version': True,
#     'navigation_depth': 5,
#     'navigation_with_keys': True,
#     'body_max_width': '80%',
# }
#
# html_css_files = [
#     'custom.css',
# ]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# html_logo = 'picture.png'
