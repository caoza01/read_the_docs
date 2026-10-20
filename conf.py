# Configuration file for the Sphinx documentation builder.

project = '像写代码一样写文档'
copyright = '2026, caoza'
author = 'caoza'
release = '1.1.2'
version = '1.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'zh_CN'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

todo_include_todos = True
