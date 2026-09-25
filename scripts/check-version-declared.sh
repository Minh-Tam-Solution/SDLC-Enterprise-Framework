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
# Dùng: check-version-declared.sh [--block] [--selftest]  (cờ cũ --chan vẫn nhận, deprecated)
#   không cờ → đếm, exit 0 (nấc 1 ADVISORY) · --block → exit 2 nếu khong_khai>0 (nấc 3 MACHINE)
# Mã thoát (21-V7): 0 ĐẠT · 1 KHÔNG ĐO ĐƯỢC (mất SSOT / quét 0 file / tham số lạ) · 2 VI PHẠM.
# Dòng cuối stdout = nhãn: result=pass|insufficient_evidence|violation gate=check-version-declared reason=<slug>
set -uo pipefail
CHAN=0; TU_THU=0
nhan() { echo "result=$1 gate=check-version-declared reason=$2"; }
for a in "$@"; do case $a in
  --block) CHAN=1;;
  --chan) echo "DEPRECATED: --chan, use --block (removal 2026-12-31)" >&2; CHAN=1;;
  --selftest) TU_THU=1;;
  *) echo "KHÔNG ĐO ĐƯỢC: tham số lạ $a"; nhan insufficient_evidence tham_so_la; exit 1;; esac; done

if [ $TU_THU = 1 ]; then
  # Fixture cục bộ: chép chính script vào cây tạm (ROOT = .. của script, scripts/ ở gốc repo) — không đụng repo thật.
  t=$(mktemp -d); S="$t/scripts/$(basename "$0")"
  mkdir -p "$(dirname "$S")" "$t/d"; cp "$0" "$S"
  kq() { local o rc; o=$(bash "$S" "$@"); rc=$?; echo "$rc|$(echo "$o" | grep -oE 'khai_cu=[0-9]+  khong_khai=[0-9]+')|${o##*$'\n'}"; }
  printf '# r\n**Version**: 9.9.9\n' > "$t/README.md"
  a=$(kq --block)                                                           # chỉ có file miễn ⇒ quét 0 ⇒ 1 (G1)
  printf '# a\n**SDLC Framework Version**: 9.9.9\n' > "$t/d/moi.md";     b=$(kq --block)  # khai đúng SSOT ⇒ 0
  printf -- '---\nsdlc_framework: "1.0.0"\n---\n' > "$t/d/cu.md";       c=$(kq --block)  # khai_cu KHÔNG phải lỗi ⇒ 0
  printf '# khong khai\n' > "$t/d/khong.md";                             d=$(kq --block)  # thiếu trường ⇒ 2
  e=$(kq)                                                                   # nấc 1: chỉ đếm ⇒ 0
  g=$(kq --chan)                                                            # cờ cũ --chan vẫn hoạt động như --block (deprecated)
  rm "$t/README.md";                                                        f=$(kq --block)  # mất SSOT ⇒ 1
  rm -rf "$t"
  G=gate=check-version-declared
  want="1|khai_cu=0  khong_khai=0|result=insufficient_evidence $G reason=quet_0_file
0|khai_cu=0  khong_khai=0|result=pass $G reason=khong_khai_0
0|khai_cu=1  khong_khai=0|result=pass $G reason=khong_khai_0
2|khai_cu=1  khong_khai=1|result=violation $G reason=khong_khai_1
0|khai_cu=1  khong_khai=1|result=pass $G reason=nac1_chi_dem_khong_khai_1
2|khai_cu=1  khong_khai=1|result=violation $G reason=khong_khai_1
1||result=insufficient_evidence $G reason=thieu_ssot_readme"
  got=$(printf '%s\n' "$a" "$b" "$c" "$d" "$e" "$g" "$f")
  [ "$got" = "$want" ] && { echo "selftest OK (7 ca)"; nhan pass selftest_ok; exit 0; }
  echo "selftest HỎNG:"; diff <(echo "$want") <(echo "$got")
  nhan insufficient_evidence selftest_hong; exit 1  # selftest hỏng = CỔNG hỏng ⇒ không đo được (1), không phải vi phạm (2)
fi
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# File META của repo — KHÔNG phải tài liệu luật ⇒ miễn. Danh sách KHAI TAY, không suy.
META='^(README|CHANGELOG|CONTENT-MAP|CONTRIBUTING|CODE_OF_CONDUCT|SECURITY|DEPRECATION-POLICY|CLAUDE)\.md$'

# Tách "không có README" khỏi "README không khai" — hai nguyên nhân, hai nhãn (G2).
[ -f "$ROOT/README.md" ] || { echo "❌ CHƯA ĐO ĐƯỢC: không có $ROOT/README.md (SSOT)"; nhan insufficient_evidence thieu_ssot_readme; exit 1; }
SSOT="$(grep -m1 -oE '^\*\*Version\*\*: [0-9]+\.[0-9]+\.[0-9]+' "$ROOT/README.md" | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')"
[ -n "$SSOT" ] || { echo "❌ CHƯA ĐO ĐƯỢC: README.md không khai '**Version**: x.y.z'"; nhan insufficient_evidence readme_khong_khai_version; exit 1; }

khai_moi=0; khai_cu=0; khong_khai=0; mien=0; DS=$(mktemp); trap 'rm -f "$DS"' EXIT  # mktemp: hai lần chạy song song không ghi đè nhau
while IFS= read -r -d '' f; do
  rel="${f#$ROOT/}"
  if [[ "$rel" =~ / ]]; then base="${rel##*/}"; else base="$rel"; fi
  if [[ ! "$rel" =~ / ]] && [[ "$base" =~ $META ]]; then mien=$((mien+1)); continue; fi
  v=$(head -20 "$f" | grep -m1 -oE 'sdlc_framework: *"?[0-9]+\.[0-9]+\.[0-9]+|^\*\*SDLC Framework Version\*\*: *[0-9]+\.[0-9]+\.[0-9]+' | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')
  if   [ -z "$v" ];            then khong_khai=$((khong_khai+1)); echo "$rel" >> "$DS"
  elif [ "$v" = "$SSOT" ];     then khai_moi=$((khai_moi+1))
  else                              khai_cu=$((khai_cu+1)); fi
done < <(find "$ROOT" -name '*.md' -not -path '*/.git/*' -not -path '*/10-Archive/*' -not -path '*/site/*' -print0)

tong=$((khai_moi+khai_cu+khong_khai+mien))
echo "SSOT=$SSOT  khai_moi=$khai_moi  khai_cu=$khai_cu  khong_khai=$khong_khai  mien=$mien  tong=$tong"
echo "  khai_cu KHÔNG phải lỗi (Convention A) — chỉ là bản đồ nợ nghiệm thu."
# G1: quét 0 file cần đo ⇒ "sạch" không có nghĩa ⇒ không đo được, không phải đạt.
[ $((tong-mien)) -gt 0 ] || { echo "❌ CHƯA ĐO ĐƯỢC: không có file nào ngoài danh sách miễn"; nhan insufficient_evidence quet_0_file; exit 1; }
[ "$khong_khai" -gt 0 ] && { echo "--- $khong_khai file CHƯA BAO GIỜ ghi nhận nghiệm với phiên bản nào (10 đầu) ---"; head -10 "$DS"; }
[ "$khong_khai" = 0 ] && { nhan pass khong_khai_0; exit 0; }
[ "$CHAN" = 1 ] && { nhan violation "khong_khai_$khong_khai"; exit 2; }
nhan pass "nac1_chi_dem_khong_khai_$khong_khai"; exit 0
