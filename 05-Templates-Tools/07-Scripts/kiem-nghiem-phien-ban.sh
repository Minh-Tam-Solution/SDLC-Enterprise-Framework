#!/usr/bin/env bash
# Cổng MACHINE đầu tiên của v7 — "tài liệu này đã được nghiệm với phiên bản khung nào?"
#
# CƠ SỞ: Convention A (Amendment B, CEO phê chuẩn 2026-06-03, Framework 6.3.2)
#   **Version**: X.Y.Z              = semver RIÊNG của tài liệu — ĐƯỢC PHÉP và NÊN khác khung
#   sdlc_framework / **SDLC Framework Version**  = đã nghiệm với phiên bản khung nào
# ⇒ Cổng này KHÔNG kiểm `**Version**`. Kiểm trường thứ hai.
# ⇒ Khai phiên bản CŨ HƠN SSOT **KHÔNG phải lỗi** — Convention B (bump đồng loạt)
#   đã bị BÁC vì nó làm khung phạm MM#9 Demand Before Surface. Chỉ ĐẾM, không cờ.
#
# G2 — ba rổ, không gộp:
#   khai_moi  : đã nghiệm với SSOT hiện tại
#   khai_cu   : đã nghiệm với bản cũ hơn        → HỢP LUẬT, chỉ đếm
#   khong_khai: không có trường nào             → CHƯA ĐO ĐƯỢC ⇒ đây là phát hiện
#
# Dùng: kiem-nghiem-phien-ban.sh [--chan]
#   không cờ → đếm, exit 0 (nấc 1 ADVISORY) · --chan → exit 1 nếu khong_khai>0 (nấc 3 MACHINE)
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
CHAN=0; [ "${1:-}" = "--chan" ] && CHAN=1

# File META của repo — KHÔNG phải tài liệu luật ⇒ miễn. Danh sách KHAI TAY, không suy.
META='^(README|CHANGELOG|CONTENT-MAP|CONTRIBUTING|CODE_OF_CONDUCT|SECURITY|DEPRECATION-POLICY|CLAUDE)\.md$'

SSOT="$(grep -m1 -oE '^\*\*Version\*\*: [0-9]+\.[0-9]+\.[0-9]+' "$ROOT/README.md" | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')"
[ -n "$SSOT" ] || { echo "❌ CHƯA ĐO ĐƯỢC: README.md không khai '**Version**: x.y.z'"; exit 1; }

khai_moi=0; khai_cu=0; khong_khai=0; mien=0; : > /tmp/v7_khong_khai.txt
while IFS= read -r -d '' f; do
  rel="${f#$ROOT/}"
  if [[ "$rel" =~ / ]]; then base="${rel##*/}"; else base="$rel"; fi
  if [[ ! "$rel" =~ / ]] && [[ "$base" =~ $META ]]; then mien=$((mien+1)); continue; fi
  v=$(head -20 "$f" | grep -m1 -oE 'sdlc_framework: *"?[0-9]+\.[0-9]+\.[0-9]+|^\*\*SDLC Framework Version\*\*: *[0-9]+\.[0-9]+\.[0-9]+' | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')
  if   [ -z "$v" ];            then khong_khai=$((khong_khai+1)); echo "$rel" >> /tmp/v7_khong_khai.txt
  elif [ "$v" = "$SSOT" ];     then khai_moi=$((khai_moi+1))
  else                              khai_cu=$((khai_cu+1)); fi
done < <(find "$ROOT" -name '*.md' -not -path '*/.git/*' -not -path '*/10-Archive/*' -not -path '*/site/*' -print0)

echo "SSOT=$SSOT  khai_moi=$khai_moi  khai_cu=$khai_cu  khong_khai=$khong_khai  mien=$mien  tong=$((khai_moi+khai_cu+khong_khai+mien))"
echo "  khai_cu KHÔNG phải lỗi (Convention A) — chỉ là bản đồ nợ nghiệm thu."
[ "$khong_khai" -gt 0 ] && { echo "--- $khong_khai file CHƯA BAO GIỜ ghi nhận nghiệm với phiên bản nào (10 đầu) ---"; head -10 /tmp/v7_khong_khai.txt; }
[ "$CHAN" = 1 ] && [ "$khong_khai" -gt 0 ] && exit 1
exit 0
