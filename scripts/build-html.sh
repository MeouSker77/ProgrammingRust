#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
STAGE="$ROOT/.bookml-build"
OUT="$ROOT/dist"
BOOKML_IMAGE="${BOOKML_IMAGE:-ghcr.io/vlmantova/bookml@sha256:f83090bdd26958621043f282b2400a2546a07cd14bcb71baedbead0594921836}"

command -v docker >/dev/null || { echo "Docker is required for BookML." >&2; exit 1; }
rm -rf "$STAGE"
python3 "$ROOT/scripts/bookml/prepare.py" "$ROOT" "$STAGE"
docker run --rm --user "$(id -u):$(id -g)" -v "$STAGE:/source" "$BOOKML_IMAGE" html

SITE="$STAGE/auxdir/html/book"
test -s "$SITE/index.html" || { echo "BookML did not produce index.html." >&2; exit 1; }
test "$(find "$SITE" -maxdepth 1 -name 'Ch[0-9]*.html' | wc -l)" -eq 23 || {
  echo "BookML did not produce all 23 chapters." >&2; exit 1;
}
rm -rf "$OUT"
mkdir -p "$OUT"
cp -a "$SITE/." "$OUT/"
python3 "$ROOT/scripts/bookml/finalize.py" "$OUT" "$STAGE"
echo "BookML HTML site generated in $OUT"
