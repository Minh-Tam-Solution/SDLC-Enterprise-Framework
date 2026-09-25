#!/usr/bin/env bash
# Cổng Hợp đồng Luật v7 (§1, lô 1). FILE = đơn vị định tuyến · DÒNG = đơn vị thi hành.
#   File có "## Luật v7" = file luật; còn lại = tham khảo. Tỉ lệ = file_luat / file trong PHẠM VI.
#   Mỗi dòng | id | lop | lenh | ca_dot | — chạy lenh ở gốc repo. Quy ước mã (plan §6.22 A):
#     0 ĐẠT · 1 KHÔNG ĐO ĐƯỢC · 2 VI PHẠM · ≥3 dành riêng (⇒ không đo được)
#   1 là mã mặc định của mọi thứ hỏng (exception, set -e, grep không khớp) ⇒ nó phải rơi vào rổ
#   trung thực; "vi phạm" chỉ khi script chạy tới cùng và cố ý trả 2.
#   lenh PHẢI là script của ta ([bash|sh|python3] <đường dẫn trong repo> [tham số]) — công cụ ngoài
#   tự đặt nghĩa cho mã 1 (grep: không khớp · shellcheck: có lỗi) ⇒ không đọc được theo quy ước.
#   --l3: mọi script trong cột lenh phải có --selftest, --selftest phải qua, và không có `exit $?`.
# Dùng: kiem-luat-v7.sh [--goc DIR] [--pham-vi DIR] [--chan] [--l3] [--selftest]
# Mã thoát của chính cổng theo cùng quy ước: 0 · 1 không đo được · 2 (--chan có dòng đỏ / --l3 vi phạm).
# ponytail: không timeout từng lenh — thêm `timeout` khi có luật chạy lâu.
set -u
GOC=.; PHAM_VI=03-AI-GOVERNANCE; CHAN=0; L3=0; TU_THU=0
while [ $# -gt 0 ]; do case $1 in
  --goc) GOC=$2; shift;; --pham-vi) PHAM_VI=$2; shift;; --chan) CHAN=1;; --l3) L3=1;; --selftest) TU_THU=1;;
  *) echo "KHÔNG ĐO ĐƯỢC: tham số lạ $1"; exit 1;; esac; shift; done

if [ $TU_THU = 1 ]; then
  t=$(mktemp -d); mkdir -p "$t/pv" "$t/s"
  printf 'exit 0\n' > "$t/s/dat.sh"; printf 'exit 2\n' > "$t/s/vp.sh"
  printf 'import khong_co_mod_xyz\n' > "$t/s/hong.py"; printf 'exit 7\n' > "$t/s/ma-la.sh"
  printf '# a\n## Luật v7\n| id | lop | lenh | ca_dot |\n|---|---|---|---|\n| X1 | MACHINE | `bash s/dat.sh` | ca |\n| X2 | MACHINE | `bash s/vp.sh` | ca |\n| X3 | MACHINE | `python3 s/hong.py` | ca |\n| X4 | MACHINE | `bash s/khong-co.sh` | ca |\n| X5 | MACHINE | `bash s/ma-la.sh` | ca |\n| X6 | ADVISORY |  | ca |\n| X7 | MACHINE | `bash s/dat.sh` |  |\n| X8 | MACHINE | `true` | ca |\n## Khác\n| Y | MACHINE | `bash s/vp.sh` | ca |\n' > "$t/pv/co-luat.md"
  printf '# b\nkhông có bảng\n' > "$t/pv/tham-khao.md"
  out=$(bash "$0" --goc "$t" --pham-vi pv); rc=$?
  # X1 đạt · X2 vi phạm · X3 (Python chết = 1) · X4 (127) · X5 (≥3) ⇒ không đo được · X6 tham khảo · X7,X8 khai sai
  want='file=2 file_luat=1 ty_le=1/2 dat=1 vi_pham=1 khong_do_duoc=3 tham_khao=1 khai_sai=2'
  got=$(echo "$out" | grep -oE 'file=[0-9]+ file_luat=[0-9]+ ty_le=[0-9/]+ dat=[0-9]+ vi_pham=[0-9]+ khong_do_duoc=[0-9]+ tham_khao=[0-9]+ khai_sai=[0-9]+')
  bash "$0" --goc "$t" --pham-vi pv --chan >/dev/null; rc_chan=$?
  bash "$0" --goc "$t" --pham-vi khong-ton-tai >/dev/null; rc_mu=$?
  printf 'case $1 in --selftest) exit 0;; esac\nexit $?\n' > "$t/s/nuot.sh"
  printf '## Luật v7\n| id | lop | lenh | ca_dot |\n|---|---|---|---|\n| Z | MACHINE | `bash s/nuot.sh` | ca |\n' > "$t/pv/co-luat.md"
  bash "$0" --goc "$t" --pham-vi pv --l3 >/dev/null; rc_l3=$?
  rm -rf "$t"
  [ "$got" = "$want" ] && [ $rc = 0 ] && [ $rc_chan = 2 ] && [ $rc_mu = 1 ] && [ $rc_l3 = 2 ] && { echo "selftest OK"; exit 0; }
  echo "selftest HỎNG: got=[$got] rc=$rc chan=$rc_chan mu=$rc_mu l3=$rc_l3"; exit 2
fi

cd "$GOC" || { echo "KHÔNG ĐO ĐƯỢC: không vào được $GOC"; exit 1; }
[ -d "$PHAM_VI" ] || { echo "KHÔNG ĐO ĐƯỢC: phạm vi $PHAM_VI không tồn tại"; exit 1; }

# Dòng bảng luật trong MỌI file .md (luật có thể sống ngoài phạm vi); bỏ 10-Archive.
# \037 (unit separator), KHÔNG dùng tab: tab là khoảng trắng trong IFS ⇒ ô rỗng bị gộp, cột lệch.
bang=$(mktemp); trap 'rm -f "$bang"' EXIT
find . -name '*.md' -not -path './10-Archive/*' -not -path './.git/*' -print0 | while IFS= read -r -d '' f; do
  awk -v f="$f" '/^## /{t=($0 ~ /^## Luật v7[[:space:]]*$/); next}
    t && /^\|/ && !/^\|[-: |]+\|$/ { n=split($0,c,"|"); for(i=2;i<n;i++) gsub(/^[[:space:]]+|[[:space:]]+$/,"",c[i]);
      if (c[2]=="id") next; print f "\037" c[2] "\037" c[3] "\037" c[4] "\037" c[5] }' "$f"
done > "$bang"

file=0; file_luat=0
while IFS= read -r -d '' f; do file=$((file+1)); grep -q '^## Luật v7[[:space:]]*$' "$f" && file_luat=$((file_luat+1)); done \
  < <(find "$PHAM_VI" -name '*.md' -print0)

dat=0; vi_pham=0; khong_do_duoc=0; tham_khao=0; khai_sai=0; l3=0
while IFS=$'\037' read -r f id lop lenh ca_dot; do
  lenh=${lenh#\`}; lenh=${lenh%\`}
  if [ -z "$lenh" ]; then tham_khao=$((tham_khao+1)); continue; fi
  if [ -z "$id" ] || [ -z "$lop" ] || [ -z "$ca_dot" ]; then khai_sai=$((khai_sai+1)); echo "ĐỎ — khai sai (thiếu trường): $id ($f)"; continue; fi
  # Script của ta: token đầu (bỏ bash/sh/python3) phải là đường dẫn .sh/.py. Có tồn tại không để lúc chạy trả 127.
  s=$(echo "$lenh" | awk '{i=1; if($1 ~ /^(bash|sh|python3)$/) i=2; print $i}')
  case $s in *.sh|*.py) ;; *) khai_sai=$((khai_sai+1)); echo "ĐỎ — khai sai (lenh không phải script của ta: $s): $id ($f)"; continue;; esac
  if [ $L3 = 0 ]; then
    # stdout bỏ, stderr GIỮ (G2): nhãn đúng mà vứt lý do thì người đọc vẫn đi đoán.
    err=$(bash -c "$lenh" 2>&1 >/dev/null </dev/null); m=$?; err=${err##*$'\n'}
    case $m in 0) dat=$((dat+1));; 2) vi_pham=$((vi_pham+1)); echo "ĐỎ — vi phạm: $id ($f)${err:+ — $err}";;
      *) khong_do_duoc=$((khong_do_duoc+1)); echo "ĐỎ — không đo được (mã $m): $id ($f)${err:+ — $err}";; esac
  else
    # --l3 KHÔNG chạy lenh: dòng L3 gọi chính cổng này ⇒ chạy lenh ở chế độ --l3 là đệ quy vô hạn.
    if [ ! -f "$s" ] || ! grep -q -- '--selftest' "$s"; then l3=$((l3+1)); echo "ĐỎ — L3 thiếu --selftest: $s ($id)"; continue; fi
    # Chỉ khớp `exit $?` ở VỊ TRÍ CÂU LỆNH (đầu dòng / sau ; && ||) — không khớp chú thích hay chuỗi.
    # Bản đầu khớp cả chú thích + fixture selftest của chính cổng này ⇒ L3 đỏ oan trên chính nó.
    if grep -qE '(^|[;&|])[[:space:]]*exit[[:space:]]+\$\?' "$s"; then l3=$((l3+1)); echo "ĐỎ — L3 có \`exit \$?\` (mã của công cụ khác lọt ra): $s ($id)"; continue; fi
    case $s in *.py) chay=python3;; *) chay=bash;; esac
    o=$($chay "$s" --selftest 2>&1) || { l3=$((l3+1)); echo "ĐỎ — L3 --selftest hỏng: $s ($id) — ${o##*$'\n'}"; }
  fi
done < "$bang"

echo "PHAM_VI=$PHAM_VI file=$file file_luat=$file_luat ty_le=$file_luat/$file dat=$dat vi_pham=$vi_pham khong_do_duoc=$khong_do_duoc tham_khao=$tham_khao khai_sai=$khai_sai$([ $L3 = 1 ] && echo " l3=$l3")"
[ $L3 = 1 ] && [ $l3 -gt 0 ] && exit 2
[ $CHAN = 1 ] && [ $((vi_pham+khong_do_duoc+khai_sai)) -gt 0 ] && exit 2
exit 0
