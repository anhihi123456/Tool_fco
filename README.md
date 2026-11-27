# Hướng Dẫn Sử Dụng Tool Săn Cầu Thủ FC Online (Python)

Tài liệu này hướng dẫn chi tiết cách thiết lập và sử dụng bộ script Python để tự động spam mua cầu thủ trên FC Online. Tool sẽ liên tục click mua ở mức giá hiện tại, và **ngay khi giá bị thay đổi (reset), tool sẽ thực hiện mua một lần cuối cùng (để chiếm top 1) rồi tự động tắt**.

## 1. Yêu Cầu Hệ Thống (Chuẩn Bị)

* Máy tính đã cài đặt **Python** (phiên bản 3.x). *Lưu ý: Nhớ tích "Add Python to PATH" khi cài đặt.*
* Trình soạn thảo code (Khuyên dùng **Visual Studio Code**).
* Các thư viện bắt buộc. Mở Terminal/CMD và chạy lệnh sau:
  ```bash
  python -m pip install pyautogui opencv-python
  ```

## 2. Cấu Trúc Thư Mục

Bạn cần đặt tất cả các file vào cùng một thư mục làm việc. Cấu trúc chuẩn như sau:

```text
📁 Tool_San_Cau_Thu/
 ├── 📄 main.py            # Script chạy kịch bản auto chính
 ├── 📄 lay_toa_do.py      # Script phụ để dò tọa độ chuột
 └── 🖼️ gia_hien_tai.png   # Ảnh chụp mức giá mục tiêu (bạn tự cắt)
```

## 3. Chức Năng & Cách Thiết Lập Từng File

### A. File `lay_toa_do.py` (Lấy tọa độ click)

Ở kịch bản mới này, tool cần click vào 3 vị trí khác nhau. Bạn dùng script này để dò từng tọa độ (X, Y) trên màn hình của bạn.

1. Mở game FC Online (để chế độ **Cửa sổ**).
2. Chạy file `lay_toa_do.py`.
3. Lần lượt đưa chuột đến 3 vị trí sau (mỗi lần để yên 3 giây để lấy tọa độ):
   * **Vị trí 1:** Dòng giá muốn chọn (thường là dòng giá đỏ đầu tiên).
   * **Vị trí 2:** Nút "Mua cầu thủ".
   * **Vị trí 3:** Nút "Xác nhận".
4. Ghi lại 3 bộ tọa độ này để điền vào file chính.

### B. Hình ảnh `gia_hien_tai.png` (Mục tiêu nhận diện)

Đây là "con mắt" để tool biết khi nào giá bị reset.

1. Mở công cụ Snipping Tool của Windows (`Win + Shift + S`).
2. Cắt **thật gọn** phần chữ số hiển thị mức giá đang muốn săn (VD: chữ `12.1B` màu đỏ). Không cắt dính nhiều nền phía sau.
3. Lưu ảnh với tên chính xác là `gia_hien_tai.png` vào thư mục chứa code.

### C. File `main.py` (Script Auto)

Mở file này lên và điền 3 tọa độ bạn vừa lấy được ở bước A vào phần `CÀI ĐẶT TỌA ĐỘ`.

**Cách thức tool hoạt động khi chạy:**
1. Mở Terminal, gõ lệnh `python main.py` và nhanh tay click sang cửa sổ game.
2. Tool bắt đầu quét màn hình:
   * **Giai đoạn 1 (Giá chưa reset):** Khi vẫn nhìn thấy ảnh `gia_hien_tai.png`, tool sẽ lặp đi lặp lại chuỗi hành động: *Click dòng giá -> Click Mua -> Click Xác nhận*.
   * **Giai đoạn 2 (Giá đã reset):** Khi ảnh mức giá cũ biến mất, tool nhận diện đây là lúc reset giá. Nó lập tức thực hiện *Click dòng giá (giá mới) -> Click Mua -> Click Xác nhận* **đúng 1 lần duy nhất** để tranh mua sớm, sau đó in ra thông báo và **tắt hoàn toàn tool**.

## 4. Tính Năng An Toàn (Fail-Safe)

Nếu tool đang chạy và bạn muốn ép nó dừng lại ngay lập tức (dù giá chưa reset), hãy **di chuyển con trỏ chuột hất thật nhanh và mạnh vào 1 trong 4 góc cùng của màn hình máy tính**. Chương trình sẽ kích hoạt tính năng an toàn (FailSafeException) và lập tức ngắt hoạt động.

## 5. Lưu Ý Quan Trọng

* **Chế độ màn hình:** Bắt buộc chơi FC Online ở chế độ **Cửa sổ (Windowed)** hoặc **Cửa sổ không viền (Borderless)**.
* **Thời gian nghỉ (Delay):** Trong file `main.py`, lệnh `time.sleep(0.1)` có thể được điều chỉnh tăng lên (ví dụ `0.2` hoặc `0.3`) nếu máy bạn yếu hoặc game load chậm để các cú click không bị trượt nhau.
* **Vị trí chuột:** Đừng để chuột của bạn (khi thao tác tay) vô tình làm hiện lên các bảng chú thích (tooltip) che lấp đi con số mức giá mà tool đang soi.