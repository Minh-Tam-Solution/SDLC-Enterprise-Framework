#!/usr/bin/env bash
# Cổng Hợp đồng Luật v7 (§1, lô 1). FILE = đơn vị định tuyến · DÒNG = đơn vị thi hành.
#   File có "## Luật v7" = file luật; còn lại = tham khảo. Tỉ lệ = file_luat / file trong PHẠM VI.
#   Header bảng PHẢI là | id | lop | lenh | ca_dot | [pham_vi_chay |] — sai tên/thứ tự cột ⇒ khai_sai.
#   pham_vi_chay ∈ FRAMEWORK_REPO · PRODUCT_CI · RUNTIME_PROBE; ô/cột thiếu = FRAMEWORK_REPO, chỉ ĐẾM (cot_thieu).
#   Chỉ chạy dòng có pham_vi_chay = --pham-vi-chay (mặc định FRAMEWORK_REPO); còn lại đếm khac_pham_vi.
#   Chạy lenh ở gốc repo. Quy ước mã (plan §6.22 A):
#     0 ĐẠT · 1 KHÔNG ĐO ĐƯỢC · 2 VI PHẠM · ≥3 dành riêng (⇒ không đo được)
#   1 là mã mặc định của mọi thứ hỏng (exception, set -e, grep không khớp) ⇒ nó phải rơi vào rổ
#   trung thực; "vi phạm" chỉ khi script chạy tới cùng và cố ý trả 2.
#   Nhãn = dòng cuối STDOUT của lenh: result=pass|insufficient_evidence|violation gate=<id> reason=<slug> [fix=<phần còn lại>]
#     phải khớp mã (pass↔0 · insufficient_evidence↔1 · violation↔2); lệch/sai cú pháp ⇒ khai_sai;
#     không có nhãn ⇒ chỉ đếm thieu_nhan, xếp theo mã (nấc 1, §4 — không bật thành vách).
#   lenh PHẢI là script của ta ([bash|sh|python3] <đường dẫn trong repo> [tham số]) — công cụ ngoài
#   tự đặt nghĩa cho mã 1 (grep: không khớp · shellcheck: có lỗi) ⇒ không đọc được theo quy ước.
#   --l3: mọi script trong cột lenh phải có --selftest, --selftest phải qua, và không có `exit $?`.
# Dùng: kiem-luat-v7.sh [--goc DIR] [--pham-vi DIR] [--pham-vi-chay X] [--chan] [--l3] [--selftest]
# Mã thoát của chính cổng theo cùng quy ước; --chan: 2 nếu vi_pham+khai_sai>0, else 1 nếu khong_do_duoc>0, else 0.
# Dòng cuối stdout của chính cổng cũng là nhãn (gate=kiem-luat-v7).
# ponytail: không timeout từng lenh — thêm `timeout` khi có luật chạy lâu.
set -u
GOC=.; PHAM_VI=03-AI-GOVERNANCE; PHAM_VI_CHAY=FRAMEWORK_REPO; CHAN=0; L3=0; TU_THU=0
nhan() { echo "result=$1 gate=kiem-luat-v7 reason=$2"; }
while [ $# -gt 0 ]; do case $1 in
  --goc) GOC=$2; shift;; --pham-vi) PHAM_VI=$2; shift;; --pham-vi-chay) PHAM_VI_CHAY=$2; shift;;
  --chan) CHAN=1;; --l3) L3=1;; --selftest) TU_THU=1;;
  *) echo "KHÔNG ĐO ĐƯỢC: tham số lạ $1"; nhan insufficient_evidence tham_so_la; exit 1;; esac; shift; done
case $PHAM_VI_CHAY in FRAMEWORK_REPO|PRODUCT_CI|RUNTIME_PROBE) ;;
  *) echo "KHÔNG ĐO ĐƯỢC: --pham-vi-chay lạ: $PHAM_VI_CHAY"; nhan insufficient_evidence pham_vi_chay_la; exit 1;; esac

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
  nhan_cuoi=${out##*$'\n'}   # dòng cuối stdout của chính cổng phải là nhãn khớp mã
  bash "$0" --goc "$t" --pham-vi pv --chan >/dev/null; rc_chan=$?
  bash "$0" --goc "$t" --pham-vi khong-ton-tai >/dev/null; rc_mu=$?
  printf 'case $1 in --selftest) exit 0;; esac\nexit $?\n' > "$t/s/nuot.sh"
  printf '## Luật v7\n| id | lop | lenh | ca_dot |\n|---|---|---|---|\n| Z | MACHINE | `bash s/nuot.sh` | ca |\n' > "$t/pv/co-luat.md"
  bash "$0" --goc "$t" --pham-vi pv --l3 >/dev/null; rc_l3=$?

  # Ca v7: cột thứ 5 · lọc pham_vi_chay · nhãn khớp/lệch mã · lô chỉ "không đo được" · header sai.
  d() { grep -oE 'dat=[0-9]+ vi_pham=.*thieu_nhan=[0-9]+'; }
  B='## Luật v7\n| id | lop | lenh | ca_dot | pham_vi_chay |\n|---|---|---|---|---|\n'
  printf 'echo "result=pass gate=x reason=ok"; exit 0\n' > "$t/s/n-dat.sh"
  printf 'echo "result=pass gate=x reason=noi_doi"; exit 2\n' > "$t/s/n-lech.sh"
  printf 'echo "result=violation gate=x reason=co_loi fix=sua lai a b"; exit 2\n' > "$t/s/n-vp.sh"
  printf 'echo "result=insufficient_evidence gate=x reason=thieu_cong_cu"; exit 1\n' > "$t/s/n-kdd.sh"
  printf "$B"'| P1 | MACHINE | `bash s/n-dat.sh` | ca | FRAMEWORK_REPO |\n| P2 | MACHINE | `bash s/n-lech.sh` | ca | FRAMEWORK_REPO |\n| P3 | MACHINE | `bash s/n-vp.sh` | ca | PRODUCT_CI |\n| P4 | MACHINE | `bash s/n-dat.sh` | ca | XYZ |\n| P5 | MACHINE | `bash s/n-dat.sh` | ca |  |\n' > "$t/pv/co-luat.md"
  # P1,P5 đạt (P5 ô trống ⇒ FRAMEWORK_REPO, cot_thieu) · P2 nhãn pass + mã 2 ⇒ khai_sai · P3 khác phạm vi · P4 giá trị lạ ⇒ khai_sai
  v1=$(bash "$0" --goc "$t" --pham-vi pv | d)
  v2=$(bash "$0" --goc "$t" --pham-vi pv --pham-vi-chay PRODUCT_CI | d)   # chỉ P3 chạy ⇒ vi_pham, fix= có dấu cách
  bash "$0" --goc "$t" --pham-vi pv --pham-vi-chay SAI >/dev/null; rc_pvc=$?
  printf '## Luật v7\n| id | lop | lenh | ca_dot |\n|---|---|---|---|\n| Q | MACHINE | `bash s/n-dat.sh` | ca |\n' > "$t/pv/co-luat.md"
  v3=$(bash "$0" --goc "$t" --pham-vi pv --chan | d)                     # bảng 4 cột ⇒ chỉ đếm, không đỏ
  bash "$0" --goc "$t" --pham-vi pv --chan >/dev/null; rc_cot=$?
  printf "$B"'| K | MACHINE | `bash s/n-kdd.sh` | ca | FRAMEWORK_REPO |\n' > "$t/pv/co-luat.md"
  bash "$0" --goc "$t" --pham-vi pv --chan >/dev/null; rc_kdd=$?         # chỉ "không đo được" ⇒ 1, không 2
  printf '## Luật v7\n| id | lenh | lop | ca_dot |\n|---|---|---|---|\n| H | `bash s/n-dat.sh` | MACHINE | ca |\n' > "$t/pv/co-luat.md"
  v4=$(bash "$0" --goc "$t" --pham-vi pv | d)
  bash "$0" --goc "$t" --pham-vi pv --chan >/dev/null; rc_hd=$?           # header sai ⇒ khai_sai ⇒ 2
  rm -rf "$t"
  w1='dat=2 vi_pham=0 khong_do_duoc=0 tham_khao=0 khai_sai=2 pham_vi_chay=FRAMEWORK_REPO cot_thieu=1 khac_pham_vi=1 thieu_nhan=0'
  w2='dat=0 vi_pham=1 khong_do_duoc=0 tham_khao=0 khai_sai=1 pham_vi_chay=PRODUCT_CI cot_thieu=1 khac_pham_vi=3 thieu_nhan=0'
  w3='dat=1 vi_pham=0 khong_do_duoc=0 tham_khao=0 khai_sai=0 pham_vi_chay=FRAMEWORK_REPO cot_thieu=1 khac_pham_vi=0 thieu_nhan=0'
  w4='dat=0 vi_pham=0 khong_do_duoc=0 tham_khao=0 khai_sai=1 pham_vi_chay=FRAMEWORK_REPO cot_thieu=0 khac_pham_vi=0 thieu_nhan=0'
  [ "$got" = "$want" ] && [ $rc = 0 ] && [ $rc_chan = 2 ] && [ $rc_mu = 1 ] && [ $rc_l3 = 2 ] \
    && [ "$nhan_cuoi" = "result=pass gate=kiem-luat-v7 reason=nac1_chi_dem" ] \
    && [ "$v1" = "$w1" ] && [ "$v2" = "$w2" ] && [ "$v3" = "$w3" ] && [ "$v4" = "$w4" ] \
    && [ $rc_pvc = 1 ] && [ $rc_cot = 0 ] && [ $rc_kdd = 1 ] && [ $rc_hd = 2 ] && { echo "selftest OK"; nhan pass selftest_ok; exit 0; }
  echo "selftest HỎNG: got=[$got] rc=$rc chan=$rc_chan mu=$rc_mu l3=$rc_l3 nhan=[$nhan_cuoi] pvc=$rc_pvc cot=$rc_cot kdd=$rc_kdd hd=$rc_hd"
  printf '  v1=[%s]\n  v2=[%s]\n  v3=[%s]\n  v4=[%s]\n' "$v1" "$v2" "$v3" "$v4"
  nhan insufficient_evidence selftest_hong; exit 1  # selftest hỏng = CỔNG hỏng ⇒ không đo được (1), không phải vi phạm (2)
fi

cd "$GOC" || { echo "KHÔNG ĐO ĐƯỢC: không vào được $GOC"; nhan insufficient_evidence khong_vao_duoc_goc; exit 1; }
[ -d "$PHAM_VI" ] || { echo "KHÔNG ĐO ĐƯỢC: phạm vi $PHAM_VI không tồn tại"; nhan insufficient_evidence pham_vi_khong_ton_tai; exit 1; }

# Dòng bảng luật trong MỌI file .md (luật có thể sống ngoài phạm vi); bỏ 10-Archive.
# \037 (unit separator), KHÔNG dùng tab: tab là khoảng trắng trong IFS ⇒ ô rỗng bị gộp, cột lệch.
# Dòng | đầu tiên của mỗi bảng = header, kiểm theo TÊN cột (không theo vị trí) — sai ⇒ một bản ghi __HEADER_SAI__.
bang=$(mktemp); loi=$(mktemp); trap 'rm -f "$bang" "$loi"' EXIT
find . -name '*.md' -not -path './10-Archive/*' -not -path './.git/*' -print0 | while IFS= read -r -d '' f; do
  awk -v f="$f" '/^## /{t=($0 ~ /^## Luật v7[[:space:]]*$/); b=0; next}
    !/^\|/ {b=0; next}
    !t || /^\|[-: |]+\|$/ {next}
    { n=split($0,c,"|"); hd=""; for(i=2;i<n;i++){ gsub(/^[[:space:]]+|[[:space:]]+$/,"",c[i]); hd=hd "|" c[i] }
      if (!b) { b=1; h=(hd=="|id|lop|lenh|ca_dot") ? 4 : (hd=="|id|lop|lenh|ca_dot|pham_vi_chay") ? 5 : 0
        if (!h) print f "\037__HEADER_SAI__\037" hd "\037\037\037"; next }
      if (h) print f "\037" c[2] "\037" c[3] "\037" c[4] "\037" c[5] "\037" (h==5 ? c[6] : "") }' "$f"
done > "$bang"

file=0; file_luat=0
while IFS= read -r -d '' f; do file=$((file+1)); grep -q '^## Luật v7[[:space:]]*$' "$f" && file_luat=$((file_luat+1)); done \
  < <(find "$PHAM_VI" -name '*.md' -print0)

re='^result=(pass|insufficient_evidence|violation) gate=[^ ]+ reason=[^ ]+( fix=.*)?$'
dat=0; vi_pham=0; khong_do_duoc=0; tham_khao=0; khai_sai=0; l3=0; cot_thieu=0; khac_pham_vi=0; thieu_nhan=0
while IFS=$'\037' read -r f id lop lenh ca_dot pv; do
  if [ "$id" = __HEADER_SAI__ ]; then khai_sai=$((khai_sai+1)); echo "ĐỎ — khai sai (header phải là |id|lop|lenh|ca_dot[|pham_vi_chay], thấy $lop): $f"; continue; fi
  lenh=${lenh#\`}; lenh=${lenh%\`}
  if [ -z "$lenh" ]; then tham_khao=$((tham_khao+1)); continue; fi
  if [ -z "$id" ] || [ -z "$lop" ] || [ -z "$ca_dot" ]; then khai_sai=$((khai_sai+1)); echo "ĐỎ — khai sai (thiếu trường): $id ($f)"; continue; fi
  [ -n "$pv" ] || { cot_thieu=$((cot_thieu+1)); pv=FRAMEWORK_REPO; }
  case $pv in FRAMEWORK_REPO|PRODUCT_CI|RUNTIME_PROBE) ;;
    *) khai_sai=$((khai_sai+1)); echo "ĐỎ — khai sai (pham_vi_chay lạ: $pv): $id ($f)"; continue;; esac
  # Lọc TRƯỚC khi chạy: lệnh PRODUCT_CI/RUNTIME_PROBE cần env của repo sản phẩm/máy chạy — chạy ở đây là đỏ oan.
  [ "$pv" = "$PHAM_VI_CHAY" ] || { khac_pham_vi=$((khac_pham_vi+1)); continue; }
  # Script của ta: token đầu (bỏ bash/sh/python3) phải là đường dẫn .sh/.py. Có tồn tại không để lúc chạy trả 127.
  s=$(echo "$lenh" | awk '{i=1; if($1 ~ /^(bash|sh|python3)$/) i=2; print $i}')
  case $s in *.sh|*.py) ;; *) khai_sai=$((khai_sai+1)); echo "ĐỎ — khai sai (lenh không phải script của ta: $s): $id ($f)"; continue;; esac
  if [ $L3 = 0 ]; then
    # stdout: dòng cuối = NHÃN · stderr: dòng cuối = LÝ DO (G2: nhãn đúng mà vứt lý do thì người đọc vẫn đi đoán).
    out=$(bash -c "$lenh" 2>"$loi" </dev/null); m=$?; err=$(tail -n 1 "$loi"); nh=${out##*$'\n'}
    if [[ $nh =~ $re ]]; then
      case ${BASH_REMATCH[1]} in pass) k=0;; insufficient_evidence) k=1;; violation) k=2;; esac
      if [ "$k" != "$m" ]; then khai_sai=$((khai_sai+1)); echo "ĐỎ — khai sai (nhãn ${BASH_REMATCH[1]} ≠ mã $m): $id ($f)"; continue; fi
    elif [[ $nh == result=* ]]; then khai_sai=$((khai_sai+1)); echo "ĐỎ — khai sai (nhãn sai cú pháp: $nh): $id ($f)"; continue
    else thieu_nhan=$((thieu_nhan+1)); nh=""; fi
    ly_do="${nh:+ — $nh}${err:+ — $err}"
    case $m in 0) dat=$((dat+1));; 2) vi_pham=$((vi_pham+1)); echo "ĐỎ — vi phạm: $id ($f)$ly_do";;
      *) khong_do_duoc=$((khong_do_duoc+1)); echo "ĐỎ — không đo được (mã $m): $id ($f)$ly_do";; esac
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

echo "PHAM_VI=$PHAM_VI file=$file file_luat=$file_luat ty_le=$file_luat/$file dat=$dat vi_pham=$vi_pham khong_do_duoc=$khong_do_duoc tham_khao=$tham_khao khai_sai=$khai_sai pham_vi_chay=$PHAM_VI_CHAY cot_thieu=$cot_thieu khac_pham_vi=$khac_pham_vi thieu_nhan=$thieu_nhan$([ $L3 = 1 ] && echo " l3=$l3")"
[ $L3 = 1 ] && [ $l3 -gt 0 ] && { nhan violation "l3_$l3"; exit 2; }
if [ $CHAN = 1 ]; then
  [ $((vi_pham+khai_sai)) -gt 0 ] && { nhan violation "vi_pham_${vi_pham}_khai_sai_$khai_sai"; exit 2; }
  [ $khong_do_duoc -gt 0 ] && { nhan insufficient_evidence "khong_do_duoc_$khong_do_duoc"; exit 1; }
  nhan pass sach; exit 0
fi
nhan pass nac1_chi_dem; exit 0
