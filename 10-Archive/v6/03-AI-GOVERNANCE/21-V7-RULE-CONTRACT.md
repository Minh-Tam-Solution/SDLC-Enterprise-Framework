> Archived 2026-09-25. Superseded by `v7/01-rule-contract.md` (the single rule register).

# 21 — Hợp đồng Luật v7

**Version**: 1.0.0
**SDLC Framework Version**: 6.5.0
**Status**: ACTIVE
**Date**: 2026-09-25
**Authority**: CEO ratified 2026-09-25

---

## v7 là gì, và KHÔNG là gì

v7 **không phải** một đợt viết tài liệu. Khung đã có **189 file sống** *(312 file nữa đã ở `10-Archive/`)*. Thêm tài liệu làm dev team **chậm hơn và tốn hơn** — ngược đúng mục đích.

> **v7 là lúc khung lần đầu ĐO ĐƯỢC CHÍNH NÓ.**

Tiêu chí nghiệm thu của v7 do CEO đặt: **làm ra sản phẩm tốt, nhanh, tốn ít thời gian · ít token · ít tiền.** Mọi đề xuất v7 phải trả lời được nó rút ngắn cái gì. Không trả lời được ⇒ không vào v7.

**Lời hứa đo được của v7: ÍT LUẬT HƠN, NHIỀU LUẬT ĐƯỢC THI HÀNH HƠN.**

---

## §1 — Hợp đồng Luật *(điều khoản nền)*

> **Một luật không có lệnh chạy được thì không phải luật. Nó là tài liệu tham khảo.**

Mọi luật trong khung phải khai **ba** thứ; thiếu một là tham khảo, không phải luật:

| Trường | Nội dung |
|---|---|
| `class` | `MACHINE` · `REVIEW` · `ADVISORY` |
| `cmd` | lệnh chạy được, trả mã thoát |
| `burn_case` | ca thật đã trả giá — vì sao luật này tồn tại |

**Cột thứ 5 `run_scope`** — `cmd` chạy được ở đâu: `FRAMEWORK_REPO` (gốc repo khung) · `PRODUCT_CI` (CI của repo áp dụng khung) · `RUNTIME_PROBE` (máy đang chạy dịch vụ). Runner chỉ chạy dòng khớp `--run-scope` (mặc định `FRAMEWORK_REPO`), **lọc trước khi chạy** — lệnh cần env của nơi khác chạy ở đây là đỏ oan. Cột/ô thiếu = `FRAMEWORK_REPO`, **chỉ đếm, không đỏ** (bảng 4 cột hiện có vẫn hợp lệ — §4 quỹ đạo). Giá trị ngoài ba giá trị trên ⇒ `misdeclared`. Header bảng phải là đúng tên cột theo thứ tự `id | class | cmd | burn_case [| run_scope]`; sai ⇒ `misdeclared`.

> **Đổi tên cột (F4, 2026-09-25, CEO ratified)**: `lop→class` · `lenh→cmd` · `ca_dot→burn_case` · `pham_vi_chay→run_scope`; tiêu đề mục `## Luật v7` → `## Rules v7`. Header **cũ** (`id|lop|lenh|ca_dot[|pham_vi_chay]`, heading `## Luật v7`) vẫn được runner chấp nhận, kèm cảnh báo deprecation ra stderr, tới **2026-12-31**. Giá trị của `class` (MACHINE/REVIEW/ADVISORY) và `run_scope` (FRAMEWORK_REPO/PRODUCT_CI/RUNTIME_PROBE) **không đổi**. Bảng luật thật không còn nằm rải rác trong nhiều tài liệu — nó chuyển về **một** file: [`v7/01-rule-contract.md`](../v7/01-rule-contract.md) (F1). Script sống ở `scripts/` (trước đây `05-Templates-Tools/07-Scripts/`, 2 shim deprecated còn lại ở đường cũ tới 2026-12-31).

**Dòng nhãn** — dòng cuối **stdout** của `cmd`:

```
result=pass|insufficient_evidence|violation gate=<id> reason=<slug> [fix=<phần còn lại dòng>]
```

Khớp mã thoát: `pass ↔ 0` · `insufficient_evidence ↔ 1` · `violation ↔ 2`. `reason` là slug không dấu cách; `fix=` nếu có là trường **cuối**, lấy hết phần còn lại của dòng (được chứa dấu cách). Nhãn không khớp mã hoặc sai cú pháp ⇒ runner đếm `misdeclared`. Thiếu nhãn ⇒ runner xếp theo mã thoát và đếm `missing_label` (chỉ đếm). Lý do đọc từ dòng cuối **stderr**. `cmd` chạy bằng cách tách argv (không qua `bash -c`) — chứa `;` `|` `&&` backtick hoặc `$(` ⇒ `misdeclared` (chặn chèn lệnh) thay vì được diễn giải lại.

Không có `cmd` ⇒ **xuống mục tham khảo**, không nằm trong danh sách luật. Đây không phải hạ cấp giá trị: tài liệu tham khảo vẫn hữu ích. Nó chỉ thôi được **giả vờ là cổng**.

---

## §2 — Ba lớp luật *(định nghĩa, KHÔNG phải ví dụ)*

| Lớp | Định nghĩa | Hỏng thì |
|---|---|---|
| **MACHINE** | tất định · cùng đầu vào ra cùng kết quả · không cần người phán | **fail-closed**, chặn |
| **REVIEW** | cần người phán, nhưng **ai phán và phán gì** thì xác định | gắn cờ, không chặn |
| **ADVISORY** | gợi ý; không có tiêu chí đạt/không đạt | **đếm**, kèm hạn *(xem G4)* |

🔴 **Model xác suất KHÔNG BAO GIỜ thuộc `MACHINE`** — dù độ chính xác bao nhiêu. Xếp vào đó là **lỗi phạm trù**, nó phá chính trục làm v7 có nghĩa. Model đứng ở `REVIEW`/`ADVISORY`, và **THÊM một dụng cụ mù kiểu khác**, không **THAY** dụng cụ tất định.
*Căn cứ đo: kiểm thử Laya/Jev 24/09 — tiếng Việt `0.260`, `ECE 0.521`: sai mà tự tin, không phát tín hiệu cảnh báo.*

---

## §3 — G1–G4: bốn luật về CỔNG, áp cho mọi cổng kể cả cổng người chạy

### G1 — Kết quả ÂM cần CA DƯƠNG
Kết quả *"không tìm thấy / 0 / sạch"* **không dùng làm căn cứ** nếu thiếu một ca dương chứng minh dụng cụ **nhìn thấy được** thứ nó đang tìm. Thiếu ⇒ ghi **"chưa đo được"**, không ghi `0`.
*Ca đốt: `gitleaks --redact` rồi grep chính chuỗi `REDACTED` ⇒ ra `0`, thật là **49**. `gh api search/*` mù repo private ⇒ một người có 4 PR merged bị báo "hoạt động 0", suýt gỡ quyền.*

### G2 — Cổng phải có giá trị riêng cho "KHÔNG ĐO ĐƯỢC"
Tách khỏi *"đo được và thấy lỗi"*. Thiếu phân biệt ⇒ hỏng **hai chiều**:
- **fail-open**: kiểu đầu ra không có ô cho "không biết" ⇒ trả giá trị gần nhất, **luôn về phía trông sạch**.
  *Ca: phán đoán boolean `noul` với đầu vào rỗng → `0.08` đọc ra "sạch" · monitor đọc sai đường dẫn → **báo lành 25 ngày** · scanner quét `0` file → **báo sạch**.*
- **fail-closed đúng nhưng NHÃN SAI**: cổng đỏ đúng, nêu **sai nguyên nhân** ⇒ người ta **đi sửa nhầm thứ**.
  *Ca 24/09: một cổng gọi script kiểm, `2>/dev/null` nuốt `ModuleNotFoundError`, cổng in ra **"README lệch YAML"**. Thật là **thiếu thư viện trên máy**. Hai người đọc cùng đi sửa nhầm thứ.*
⇒ **Không `2>/dev/null` trên lệnh mà kết quả sẽ thành căn cứ.** Một biến không mang hai nghĩa.

### G3 — Viết cổng từ ĐỊNH NGHĨA, không từ VÍ DỤ; và phải có ca làm nó ĐỎ
Mỗi cổng phải kèm **một ca cố ý làm nó đỏ** và **một ca sạch phải xanh**. **Chưa ai làm nó đỏ thì "xanh" nghĩa là "chưa đo được".**
*Ca: một cổng chống trùng lặp tài liệu so **tên file** giữa các cây. Trùng lặp thật không bao giờ trùng tên ⇒ cổng **xanh 100% trong khi việc chưa xong**, và người được giao **không có cách nào biết mình còn nợ gì**.*

### G4 — `ADVISORY` phải có BỘ ĐẾM + HẠN
Phát hiện tồn đọng trong cổng chỉ-báo ⇒ **cổng đã chết**; người ta đã học cách không đọc. Hết hạn mà đếm vẫn > 0 ⇒ hoặc lên `REVIEW`, hoặc **xoá luật**. Không có nấc thứ ba "để đó".

---

## §4 — Bật cổng theo QUỸ ĐẠO, không bật thành vách

Cổng bật lúc đang có nhiều vi phạm ⇒ CI đỏ ngày đầu ⇒ **bị tắt trong một ngày**, và mất cả cổng lẫn đường an toàn.

| Nấc | Trạng thái | Điều kiện lên nấc sau |
|---|---|---|
| 1 | `ADVISORY` + bộ đếm, in số mỗi tuần | tỉ lệ vi phạm **< 20%** |
| 2 | `REVIEW` — gắn cờ, không chặn | **< 5%** trong **2 tuần liên tiếp** |
| 3 | `MACHINE` — chặn thật | — |

**Ngưỡng công bố TRƯỚC khi bật nấc 1.** Đặt ngưỡng sau khi thấy số là tự chấm mình.

---

## §5 — 189 file hiện có: đường đi, không phải đợt viết lại

Mỗi file sống đi **một trong ba** đường. **Không có đường thứ tư là "viết lại cho v7".**

1. **Luật** — có `class` + `cmd` + `burn_case` ⇒ vào danh sách luật v7
2. **Tham khảo** — nội dung đúng, không có lệnh ⇒ giữ, thôi giả vờ là cổng
3. **`10-Archive/`** — hết hiệu lực

⛔ **Không bump nhãn phiên bản hàng loạt.** Convention B đã bị bác *(Amendment B, 2026-06-03)* vì nó làm khung phạm **MM#9 Demand Before Surface**. Đã từng căn chỉnh **636 tham chiếu bằng tay** và nó trôi lại — **một lần dọn thủ công không có gì giữ nó**.

---

## §6 — Cổng `MACHINE` đầu tiên và con số khởi điểm

`scripts/check-version-declared.sh` — *"tài liệu này đã được nghiệm với phiên bản khung nào?"* *(trước đây `05-Templates-Tools/07-Scripts/kiem-nghiem-phien-ban.sh` — F4, 2026-09-25, shim deprecated còn ở đường cũ tới 2026-12-31)*

Nó kiểm trường `sdlc_framework` / `**SDLC Framework Version**` theo **Convention A**, **không** kiểm `**Version**` *(semver riêng của tài liệu — được phép và NÊN khác)*. Khai bản **cũ hơn** SSOT **không phải lỗi**; chỉ đếm.

**Tỉ lệ vi phạm** — công thức, không phải số *(số in cứng đã lệch `189→190` trước khi merge, vì chính file này cũng khai phiên bản)*:

```
ty_le = khong_khai / (tong − mien)
bash scripts/check-version-declared.sh      # lấy số tại thời điểm đọc
```

> Lần đo đầu, 25/09/2026: **82%** file sống chưa từng ghi nhận được nghiệm với phiên bản khung nào. Đó là điểm khởi đầu thật của v7 — không phải "khung thiếu nội dung", mà **khung không biết phần nào của nó còn đúng**.

**Quỹ đạo của cổng này** *(theo §4, ngưỡng công bố trước khi bật)*:

| Nấc | Điều kiện lên nấc | Trạng thái |
|---|---|---|
| 1 `ADVISORY` | — | **hiện tại**: đếm, không chặn |
| 2 `REVIEW` | `ty_le < 20%` | gắn cờ, không chặn |
| 3 `MACHINE` | `ty_le < 5%` trong **2 tuần liên tiếp** | chặn thật (`--block` ⇒ mã `2`; mất SSOT / quét 0 file ⇒ `1`; cờ cũ `--chan` vẫn nhận, deprecated tới 2026-12-31) |

*Ghi lại một lỗi trong lúc dựng chính cổng này, làm ca đốt cho G3: bản đầu đo trường `**Version**` và báo "89 file lệch". **Sai** — `**Version**` được phép khác theo Convention A. Cổng chỉ lộ ra là sai vì **đã chạy nó**, rồi đọc luật của khung trước khi tin kết quả. Bản đầu đã bỏ.*
