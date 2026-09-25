#!/usr/bin/env bash
# Luật 2 (G2): cấm nuốt stderr trong 07-Scripts/. Cần thật ⇒ khai .mien-nuot-stderr kèm HẠN.
#   Vì sao: `find … 2>/dev/null | wc -l` gặp lỗi quyền ⇒ ra 0 ⇒ script coi là "rỗng" và ra quyết định.
#   Ca đốt 24/09: `2>/dev/null` nuốt ModuleNotFoundError, cổng in "README lệch YAML" — sai nguyên nhân.
# .mien-nuot-stderr, mỗi dòng:  duong/dan<TAB>YYYY-MM-DD(hết hạn)<TAB>lý do
# Mã thoát (plan §6.22 A): 0 đạt · 1 không đo được · 2 vi phạm (kể cả miễn trừ quá hạn).
set -u
DIR=${1:-05-Templates-Tools/07-Scripts}
if [ "$DIR" = --selftest ]; then
  t=$(mktemp -d); s=$(basename "$0")
  printf '#!/bin/sh\nls x\n' > "$t/sach.sh"; bash "$0" "$t" >/dev/null; a=$?
  printf '#!/bin/sh\nls x 2>/dev/nul''l\n' > "$t/ban.sh"; bash "$0" "$t" >/dev/null; b=$?
  printf 'ban.sh\t2999-01-01\tthử\n' > "$t/.mien-nuot-stderr"; bash "$0" "$t" >/dev/null; c=$?
  printf 'ban.sh\t2000-01-01\tthử\n' > "$t/.mien-nuot-stderr"; bash "$0" "$t" >/dev/null; d=$?
  bash "$0" "$t/khong-co" >/dev/null; e=$?
  rm -rf "$t"
  [ "$a$b$c$d$e" = "02021" ] && { echo "selftest OK"; exit 0; }; echo "selftest HỎNG: $a$b$c$d$e (muốn 02021)"; exit 1  # selftest hỏng = CỔNG hỏng ⇒ không đo được (1), không phải vi phạm (2)
fi
[ -d "$DIR" ] || { echo "KHÔNG ĐO ĐƯỢC: $DIR không tồn tại"; exit 1; }
hom_nay=$(date +%F); vi_pham=0; mien=0; qua_han=0
while IFS= read -r -d '' f; do
  rel=${f#"$DIR"/}
  n=$(grep -c '2>/dev/nul[l]' "$f"); [ "$n" -gt 0 ] || continue
  han=""; [ -f "$DIR/.mien-nuot-stderr" ] && han=$(awk -F'\t' -v r="$rel" '$1==r{print $2; exit}' "$DIR/.mien-nuot-stderr")
  if [ -z "$han" ] || ! [[ $han =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then vi_pham=$((vi_pham+n)); echo "ĐỎ — vi phạm: $rel ($n chỗ)"
  elif [[ $han < $hom_nay ]]; then qua_han=$((qua_han+n)); echo "ĐỎ — miễn trừ QUÁ HẠN $han: $rel ($n chỗ)"
  else mien=$((mien+n)); fi
done < <(find "$DIR" -type f \( -name '*.sh' -o -name '*.py' \) -not -name "$(basename "$0")" -print0)
echo "vi_pham=$vi_pham mien_con_han=$mien mien_qua_han=$qua_han"
[ $((vi_pham+qua_han)) -gt 0 ] && exit 2; exit 0
