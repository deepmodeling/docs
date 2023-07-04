from datetime import date
from pathlib import Path

from sphinx.util.fileutil import copy_asset_file


project = 'DeepModeling'
copyright = '2021-%d, DeepModeling' % date.today().year
author = 'DeepModeling'

extensions = [
    'deepmodeling_sphinx',
]
html_theme = 'sphinx_rtd_theme'

def copy_custom_files(app):
    if app.builder.format == "html":
        staticdir = os.path.join(app.builder.outdir)
        cwd = Path(__file__).parent.absolute()
        google_html = cwd / "googleb1dcd004739ab7d2.html"
        baidu_html = cwd / "baidu_verify_codeva-DsQg16XEgd.html"
        os.makedirs(staticdir, exist_ok=True)
        copy_asset_file(str(google_html), staticdir)
        copy_asset_file(str(baidu_html), staticdir)


def setup(app):
    app.connect("builder-inited", copy_custom_files)
    return {"parallel_read_safe": True}
