# file: app.py

import threading
import time
from flask import Flask

# Import logic và cấu hình bot từ file run_all_bots
from run_all_bots import BOT_CONFIGURATIONS, TelegramBotPersona, VN_TZ, GLOBAL_ACTIVE_START, GLOBAL_ACTIVE_END

# Khởi tạo ứng dụng web Flask
app = Flask(__name__)

# Tạo một route cơ bản để UptimeRobot có thể truy cập
@app.route('/')
def home():
    now_vn = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return f"Hệ thống bot đang hoạt động. Thời gian hiện tại: {now_vn} (UTC+7)"

# Hàm để khởi động tất cả các luồng bot
def start_bots():
    threads = []
    for config in BOT_CONFIGURATIONS:
        bot_persona = TelegramBotPersona(config)
        if hasattr(bot_persona, 'bot'):
            # Tạo mỗi bot trên một luồng riêng
            thread = threading.Thread(target=bot_persona.run_logic, daemon=True)
            threads.append(thread)
            thread.start()
            time.sleep(2) # Chờ một chút giữa mỗi lần khởi động bot

    if threads:
        print(f"🚀 Đã khởi động thành công {len(threads)} bot trong background.")
        print(f"ℹ️ Giờ hoạt động chung được thiết lập từ {GLOBAL_ACTIVE_START.strftime('%H:%M')} đến {GLOBAL_ACTIVE_END.strftime('%H:%M')}.")
    else:
        print("🔴 Không có bot nào được khởi động. Vui lòng kiểm tra lại cấu hình và file .env.")

# Đoạn code này đảm bảo các bot chỉ khởi động MỘT LẦN khi server bắt đầu
if __name__ != '__main__':
    start_bots()