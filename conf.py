from datetime import date

project = 'DeepModeling'
copyright = '2021-%d, DeepModeling' % date.today().year
author = 'DeepModeling'

extensions = [
    'deepmodeling_sphinx',
    'sphinx-favicon',
]
html_theme = 'sphinx_rtd_theme'
favicons = [
    {
        "rel": "icon",
        "href": "https://unpkg.com/@njzjz/icons@0.0.4/logos/deepmodeling.png",
        "type": "image/svg+xml",
    },
]