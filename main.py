import pyautogui
import time
import sys

# Đặt độ trễ nhỏ để click mượt, không bị miss thao tác trong game
pyautogui.PAUSE = 0.1 
pyautogui.FAILSAFE = True 

print("Đang khởi động tool... (Nhớ chuyển sang màn hình game nhé!)")
time.sleep(3) 

# ==========================================
# CÀI ĐẶT TỌA ĐỘ (Thay đổi cho khớp màn hình của bạn)
# ==========================================
TOA_DO_GIA = (600, 450)       # Vị trí dòng giá bạn muốn click (Ví dụ: dòng giá đỏ đầu tiên)
TOA_DO_MUA = (850, 900)       # Vị trí nút "Mua cầu thủ"
TOA_DO_XAC_NHAN = (950, 900)  # Vị trí nút "Xác nhận"
# ==========================================

while True:
    try:
        # Quét tìm ảnh giá cũ
        gia_cu = pyautogui.locateOnScreen('gia_hien_tai.png', confidence=0.85)
        
        if gia_cu is not None:
            # --- TRƯỜNG HỢP 1: GIÁ CHƯA RESET ---
            print("[+] Giá chưa reset. Đang lặp lại vòng mua...")
            
            # 1. Click chọn mức giá
            pyautogui.click(x=TOA_DO_GIA[0], y=TOA_DO_GIA[1])
            time.sleep(0.1) # Chờ game nhận diện click
            
            # 2. Click nút Mua
            pyautogui.click(x=TOA_DO_MUA[0], y=TOA_DO_MUA[1])
            time.sleep(0.1)
            
            # 3. Click Xác nhận
            pyautogui.click(x=TOA_DO_XAC_NHAN[0], y=TOA_DO_XAC_NHAN[1])
            
            time.sleep(0.5) # Nghỉ 0.5s rồi mới bắt đầu vòng lặp tiếp theo (chống lag game)
            
        else:
            # --- TRƯỜNG HỢP 2: GIÁ ĐÃ RESET ---
            print("[!] PHÁT HIỆN RESET GIÁ! Thực hiện mua 1 lần cuối...")
            
            # Click vào vị trí giá mới (thường mặc định là dòng giá đầu tiên / giá min)
            pyautogui.click(x=TOA_DO_GIA[0], y=TOA_DO_GIA[1])
            time.sleep(0.1)
            
            pyautogui.click(x=TOA_DO_MUA[0], y=TOA_DO_MUA[1])
            time.sleep(0.1)
            
            pyautogui.click(x=TOA_DO_XAC_NHAN[0], y=TOA_DO_XAC_NHAN[1])
            
            print("[+] Đã hoàn tất lượt mua cuối cùng. Tự động tắt tool!")
            sys.exit() # Thoát chương trình lập tức
            
    except pyautogui.ImageNotFoundException:
        # Xử lý ngoại lệ giống hệt "TRƯỜNG HỢP 2" dành cho thư viện PyAutoGUI bản mới
        print("[!] PHÁT HIỆN RESET GIÁ! Thực hiện mua 1 lần cuối...")
        
        pyautogui.click(x=TOA_DO_GIA[0], y=TOA_DO_GIA[1])
        time.sleep(0.1)
        pyautogui.click(x=TOA_DO_MUA[0], y=TOA_DO_MUA[1])
        time.sleep(0.1)
        pyautogui.click(x=TOA_DO_XAC_NHAN[0], y=TOA_DO_XAC_NHAN[1])
        
        print("[+] Đã hoàn tất lượt mua cuối cùng. Tự động tắt tool!")
        sys.exit()