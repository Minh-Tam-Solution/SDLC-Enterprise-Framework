#!/usr/bin/env bash
# Luật 4: cấm `\b` trong `git grep -E`. Nó khớp KHÔNG GÌ và trả về THÀNH CÔNG — im lặng.
#   Ca đốt 25/09: `git grep -E '\bMUST\b'` ra 0 dòng (chuỗi có thật). Cùng buổi ra 0 "không còn chỗ ghi 8"
#   rồi 5 "câu MUST" (thật là hàng trăm) — hai lần sai ngược hướng, chỉ lộ nhờ ca dương. Dùng `-w` hoặc `-P`.
# Quét file CHẠY ĐƯỢC (*.sh *.py *.yml *.yaml Makefile), không quét văn xuôi — tài liệu kể ca đốt không phải lệnh.
# Mã thoát (plan §6.22 A): 0 đạt · 1 không đo được · 2 vi phạm.
set -u
GOC=${1:-.}
if [ "$GOC" = --selftest ]; then
  t=$(mktemp -d)
  printf 'git grep -w MUST\n' > "$t/sach.sh"; bash "$0" "$t" >/dev/null; a=$?
  printf 'git grep -E %s\n' "'\\bMUST\\b'" > "$t/ban.sh"; bash "$0" "$t" >/dev/null; b=$?
  bash "$0" "$t/khong-co" >/dev/null; c=$?
  rm -rf "$t"
  [ "$a$b$c" = "021" ] && { echo "selftest OK"; exit 0; }; echo "selftest HỎNG: $a$b$c (muốn 021)"; exit 2
fi
[ -d "$GOC" ] || { echo "KHÔNG ĐO ĐƯỢC: $GOC không tồn tại"; exit 1; }
vi_pham=0
while IFS= read -r -d '' f; do
  while IFS= read -r l; do vi_pham=$((vi_pham+1)); echo "ĐỎ — vi phạm: ${f#"$GOC"/}: $l"; done \
    < <(grep -nE 'git grep' "$f" | grep -E -- '(-E|--extended-regexp)' | grep -F '\''b' )
done < <(find "$GOC" -type f \( -name '*.sh' -o -name '*.py' -o -name '*.yml' -o -name '*.yaml' -o -name Makefile \) \
          -not -path '*/.git/*' -not -path '*/10-Archive/*' -not -name "$(basename "$0")" -print0)
echo "vi_pham=$vi_pham"; [ $vi_pham -gt 0 ] && exit 2; exit 0
