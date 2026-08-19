#!/usr/bin/env bash
set -euo pipefail

PANDOC="${PANDOC:-pandoc}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/site-src"
MACROS="$(mktemp)"
trap 'rm -f "$MACROS"' EXIT

cat > "$MACROS" <<'EOF'
\newcommand{\codeentry}[1]{\paragraph{#1}}
\newcommand{\hangparagraph}[1]{#1}
\newenvironment{note}{\begin{quote}\textbf{NOTE}: }{\end{quote}}
EOF

rm -rf "$SRC"
mkdir -p "$SRC/public/img"

convert() {
  "$PANDOC" -f latex -t gfm --wrap=none "$MACROS" "$1" -o "$2"
  sed -i \
    -e 's|src="../img/|src="/img/|g' \
    -e 's|\[\([^]]*@[^]]*\)\]([^)]*)|\1|g' \
    -e 's|<a href="\([^"]*@[^"]*\)" class="uri">\([^<]*\)</a>|\2|g' \
    "$2"
}

convert "$ROOT/src/preface.tex"    "$SRC/preface.md"
convert "$ROOT/src/translator.tex" "$SRC/translator.md"
for n in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23; do
  convert "$ROOT/src/ch${n}.tex" "$SRC/ch${n}.md"
done

cp -r "$ROOT/img/." "$SRC/public/img/"
touch "$SRC/public/.nojekyll"

echo "Markdown generated in $SRC ($(ls "$SRC"/*.md | wc -l) pages)"
