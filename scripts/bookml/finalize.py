"""Check BookML's output and set the generated book label."""

from pathlib import Path
import re
import sys


site = Path(sys.argv[1])
stage = Path(sys.argv[2])
expected_code_count = sum(
    source.read_text(encoding="utf-8").count(r"\begin{lstlisting}")
    for source in stage.glob("*.tex")
)
pages = list(site.glob("*.html"))
chapters = list(site.glob("Ch[0-9]*.html"))
if len(pages) != 26 or len(chapters) != 23:
    raise RuntimeError(f"Expected 26 pages and 23 chapters, got {len(pages)} and {len(chapters)}")

code_count = 0
for page in pages:
    html = page.read_text(encoding="utf-8")
    code_count += html.count('class="bml_listing"')
    html = re.sub(
        r'(<a\b[^>]*\brel="start"[^>]*>).*?(</a>)',
        r'\1Programming Rust, 2nd Edition\2',
        html,
        flags=re.S,
    )
    if page.name == "index.html":
        html = html.replace("<title>Contents</title>", "<title>Programming Rust, 2nd Edition</title>")
    page.write_text(html, encoding="utf-8")

    for url in re.findall(r'(?:src|href)="([^"]+)"', html):
        if url.startswith(("http:", "https:", "data:", "#", "mailto:", "javascript:")) or "@" in url:
            continue
        local = url.split("#")[0].split("?")[0]
        if local and not (page.parent / local).exists():
            raise RuntimeError(f"Broken local link in {page.name}: {url}")

if code_count != expected_code_count:
    raise RuntimeError(f"Expected {expected_code_count} code blocks, got {code_count}")
print(f"Checked {len(pages)} pages, {len(chapters)} chapters, {code_count} code blocks")
