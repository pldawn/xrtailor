import os

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

language = os.environ.get('READTHEDOCS_LANGUAGE', 'en')

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'XRTailor'
copyright = '2025, OpenXRLab'
author = 'OpenXRLab'
release = 'v1.9.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx_markdown_tables',
    'sphinx.ext.mathjax',
]

myst_enable_extensions = [
    "colon_fence",
    "dollarmath",  # enables $...$ and $$...$$
    "amsmath",
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_logo = "_static/logo.png"
html_title = "XRTailor Documentation"
html_theme_options = {
    "home_page_in_toc": True,
    "repository_url": "https://github.com/openxrlab/xrtailor",
    "use_repository_button": True,
    "use_issues_button": True,
    "show_toc_level": 2,
}
html_static_path = ['_static']