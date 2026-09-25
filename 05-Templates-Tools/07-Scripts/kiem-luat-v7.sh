#!/usr/bin/env bash
# Cổng Hợp đồng Luật v7 (§1, lô 1). FILE = đơn vị định tuyến · DÒNG = đơn vị thi hành.
#   File có "## Luật v7" = file luật; còn lại = tham khảo. Tỉ lệ = file_luat / file trong PHẠM VI.
#   Mỗi dòng bảng | id | lop | lenh | ca_dot | — chạy lenh ở gốc repo:
#     lenh rỗng            -> tham_khao (đếm)
#     mã 0 / 1             -> đạt / ĐỎ "vi phạm"
#     mã >=2 (126/127…)    -> ĐỎ "lệnh không chạy" — KHÔNG gộp vào vi phạm (G2, ca pyyaml 24/09)
#   Quy ước mã thoát cho MỌI lệnh luật: 0 đạt · 1 vi phạm · >=2 không đo được (như grep).
#   --l3: mọi script có tên trong cột lenh phải có --selftest và --selftest phải qua (Luật 3).
# Dùng: kiem-luat-v7.sh [--goc DIR] [--pham-vi DIR] [--chan] [--l3] [--selftest]
# Mã thoát: 0 · 1 (--chan và có dòng đỏ / --l3 vi phạm) · 2 không đo được.
# ponytail: không timeout cho từng lenh — thêm `timeout` khi có luật chạy lâu.
set -u
GOC=.; PHAM_VI=03-AI-GOVERNANCE; CHAN=0; L3=0
while [ $# -gt 0 ]; do case $1 in
  --goc) GOC=$2; shift;; --pham-vi) PHAM_VI=$2; shift;; --chan) CHAN=1;; --l3) L3=1;;
  --selftest) exec bash "$0" --tu-thu;; --tu-thu) TU_THU=1;; *) echo "tham số lạ: $1"; exit 2;; esac; shift; done

if [ "${TU_THU:-0}" = 1 ]; then
  t=$(mktemp -d); mkdir -p "$t/pv"
  printf '# a\n## Luật v7\n| id | lop | lenh | ca_dot |\n|---|---|---|---|\n| X1 | MACHINE | `true` | ca |\n| X2 | MACHINE | `false` | ca |\n| X3 | MACHINE | `khong_co_lenh_xyz_127` | ca |\n| X4 | ADVISORY |  | ca |\n| X5 | MACHINE | `true` |  |\n## Khác\n| Y | MACHINE | `false` | ca |\n' > "$t/pv/co-luat.md"
  printf '# b\nkhông có bảng\n' > "$t/pv/tham-khao.md"
  out=$(bash "$0" --goc "$t" --pham-vi pv); rc=$?
  want='file=2 file_luat=1 ty_le=1/2 dat=1 vi_pham=1 khong_do_duoc=1 tham_khao=1 thieu_truong=1'
  got=$(echo "$out" | grep -oE 'file=[0-9]+ file_luat=[0-9]+ ty_le=[0-9/]+ dat=[0-9]+ vi_pham=[0-9]+ khong_do_duoc=[0-9]+ tham_khao=[0-9]+ thieu_truong=[0-9]+')
  bash "$0" --goc "$t" --pham-vi pv --chan >/dev/null; rc_chan=$?
  bash "$0" --goc "$t" --pham-vi khong-ton-tai >/dev/null; rc_mu=$?
  rm -rf "$t"
  [ "$got" = "$want" ] && [ $rc = 0 ] && [ $rc_chan = 1 ] && [ $rc_mu = 2 ] && { echo "selftest OK"; exit 0; }
  echo "selftest HỎNG: got=[$got] rc=$rc chan=$rc_chan mu=$rc_mu"; exit 1
fi

cd "$GOC" || { echo "CHƯA ĐO ĐƯỢC: không vào được $GOC"; exit 2; }
[ -d "$PHAM_VI" ] || { echo "CHƯA ĐO ĐƯỢC: phạm vi $PHAM_VI không tồn tại"; exit 2; }

# Dòng bảng luật trong MỌI file .md (luật có thể sống ngoài phạm vi); bỏ 10-Archive.
bang=$(mktemp)
find . -name '*.md' -not -path './10-Archive/*' -not -path './.git/*' -print0 | while IFS= read -r -d '' f; do
  awk -v f="$f" '/^## /{t=($0 ~ /^## Luật v7[[:space:]]*$/); next}
    t && /^\|/ && !/^\|[-: |]+\|$/ { n=split($0,c,"|"); for(i=2;i<n;i++) gsub(/^[[:space:]]+|[[:space:]]+$/,"",c[i]);
      if (c[2]=="id") next; print f "\037" c[2] "\037" c[3] "\037" c[4] "\037" c[5] }' "$f"
done > "$bang"

file=0; file_luat=0
while IFS= read -r -d '' f; do file=$((file+1)); grep -q '^## Luật v7[[:space:]]*$' "$f" && file_luat=$((file_luat+1)); done \
  < <(find "$PHAM_VI" -name '*.md' -print0)

dat=0; vi_pham=0; khong_do_duoc=0; tham_khao=0; thieu_truong=0; l3=0
# \037 (unit separator), KHÔNG dùng tab: tab là khoảng trắng trong IFS ⇒ ô rỗng bị gộp, cột lệch.
while IFS=$'\037' read -r f id lop lenh ca_dot; do
  lenh=${lenh#\`}; lenh=${lenh%\`}
  if [ -z "$lenh" ]; then tham_khao=$((tham_khao+1)); continue; fi
  if [ -z "$id" ] || [ -z "$lop" ] || [ -z "$ca_dot" ]; then thieu_truong=$((thieu_truong+1)); echo "ĐỎ — thiếu trường: $f $id"; continue; fi
  if [ $L3 = 0 ]; then
    # --l3 KHÔNG chạy lenh: dòng L3 gọi chính cổng này ⇒ chạy lenh ở chế độ --l3 là đệ quy vô hạn.
    # stdout bỏ, stderr GIỮ (G2): nhãn đúng mà vứt lý do thì người đọc vẫn đi đoán.
    err=$(bash -c "$lenh" 2>&1 >/dev/null </dev/null); m=$?; err=${err##*$'\n'}
    case $m in 0) dat=$((dat+1));; 1) vi_pham=$((vi_pham+1)); echo "ĐỎ — vi phạm: $id ($f)${err:+ — $err}";;
      *) khong_do_duoc=$((khong_do_duoc+1)); echo "ĐỎ — lệnh không chạy (mã $m): $id ($f)${err:+ — $err}";; esac
  else s=$(echo "$lenh" | awk '{for(i=1;i<=NF;i++) if($i ~ /\.(sh|py)$/){print $i; exit}}')
    if [ -n "$s" ]; then
      if [ ! -f "$s" ] || ! grep -q -- '--selftest' "$s"; then l3=$((l3+1)); echo "ĐỎ — L3 thiếu --selftest: $s ($id)"
      else case $s in *.py) chay=python3;; *) chay=bash;; esac
        o=$($chay "$s" --selftest 2>&1) || { l3=$((l3+1)); echo "ĐỎ — L3 --selftest hỏng: $s ($id) — ${o##*$'\n'}"; }; fi
    fi; fi
done < "$bang"
rm -f "$bang"

echo "PHAM_VI=$PHAM_VI file=$file file_luat=$file_luat ty_le=$file_luat/$file dat=$dat vi_pham=$vi_pham khong_do_duoc=$khong_do_duoc tham_khao=$tham_khao thieu_truong=$thieu_truong$([ $L3 = 1 ] && echo " l3=$l3")"
[ $L3 = 1 ] && [ $l3 -gt 0 ] && exit 1
[ $CHAN = 1 ] && [ $((vi_pham+khong_do_duoc+thieu_truong)) -gt 0 ] && exit 1
exit 0
