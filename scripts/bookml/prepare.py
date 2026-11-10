"""Prepare LaTeX sources for BookML without changing the PDF edition."""

from pathlib import Path
import re
import shutil
import sys


root = Path(sys.argv[1]).resolve()
stage = Path(sys.argv[2]).resolve()
stage.mkdir(parents=True, exist_ok=True)
shutil.copytree(root / "img", stage / "img", dirs_exist_ok=True)
(stage / "bmluser").mkdir(exist_ok=True)
shutil.copy2(root / "scripts" / "bookml" / "fonts.gitbook.css", stage / "bmluser")
shutil.copy2(root / "scripts" / "bookml" / "navigation.gitbook.css", stage / "bmluser")

languages = {"c": "C", "c++": "C++", "python": "Python", "bash": "bash"}
minted_start = re.compile(r"\\begin\{minted\}(?:\[[^\]]*\])?\{([^}]+)\}")
source_count = 0


def convert_start(match: re.Match[str]) -> str:
    global source_count
    source_count += 1
    language = languages.get(match.group(1).lower())
    return r"\begin{lstlisting}" + (f"[language={language}]" if language else "")


for source in sorted((root / "src").glob("*.tex")):
    if source.name.startswith("main"):
        continue
    original = source.read_text(encoding="utf-8")
    converted = minted_start.sub(convert_start, original)
    converted = converted.replace(r"\end{minted}", r"\end{lstlisting}")
    converted = converted.replace("../img/", "img/")
    if r"\begin{minted}" in converted or r"\end{minted}" in converted:
        raise RuntimeError(f"Unconverted minted environment in {source}")
    (stage / source.name).write_text(converted, encoding="utf-8")

entry = (root / "src" / "main_html.tex").read_text(encoding="utf-8")
(stage / "book.tex").write_text(entry, encoding="utf-8")
(stage / "GNUmakefile").write_text(
    "SOURCES=book.tex\n"
    "FORMATS=zip\n"
    "SPLITAT=chapter\n"
    "book_LATEXMKFLAGS=-pdfxe\n"
    "include bookml/bookml.mk\n",
    encoding="utf-8",
)
print(f"Prepared {source_count} code blocks for BookML")
