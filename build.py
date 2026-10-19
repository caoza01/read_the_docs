"""构建 Sphinx 文档。

用法:
    python build.py            # 构建 HTML 到 _build/html
    python build.py clean      # 清理构建产物
"""

import shutil
import sys
from pathlib import Path

SRC_DIR = Path(__file__).parent
BUILD_DIR = SRC_DIR / "_build"


def clean() -> None:
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
        print(f"cleaned: {BUILD_DIR}")


def build() -> None:
    from sphinx.application import Sphinx

    app = Sphinx(
        srcdir=str(SRC_DIR),
        confdir=str(SRC_DIR),
        outdir=str(BUILD_DIR / "html"),
        doctreedir=str(BUILD_DIR / ".doctrees"),
        buildername="html",
    )
    app.build()
    print(f"done -> {BUILD_DIR / 'html' / 'index.html'}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "clean":
        clean()
    else:
        build()
