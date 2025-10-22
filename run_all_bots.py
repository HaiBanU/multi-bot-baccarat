# file: run_all_bots.py

import telegram
import asyncio
import random
import time
import os
from dotenv import load_dotenv
from collections import deque
from datetime import datetime, timedelta, timezone, time as dt_time
from telegram.request import HTTPXRequest

# Import các kịch bản từ thư mục con
from kịch_bản.kho_kich_ban_sinh_vien import SCENARIOS_SINH_VIEN
from kịch_bản.kho_kich_ban_tho_ho import SCENARIOS_THO_HO
from kịch_bản.kho_kich_ban_me_bim import SCENARIOS_NOI_TRO_VY

load_dotenv()

CHAT_ID = os.getenv("CHAT_ID")
VN_TZ = timezone(timedelta(hours=7))

GLOBAL_ACTIVE_START = dt_time(6, 30)
GLOBAL_ACTIVE_END = dt_time(23, 59)

# Lớp TelegramBotPersona và cấu hình BOT_CONFIGURATIONS giữ nguyên như cũ
# ... (Toàn bộ nội dung lớp TelegramBotPersona và biến BOT_CONFIGURATIONS ở đây) ...
# ... (Copy và dán toàn bộ nội dung của chúng từ file cũ vào đây) ...
class TelegramBotPersona:
    def __init__(self, config):
        self.bot_name = config['name']
        self.token = os.getenv(config['token_env_var'])
        self.scenarios = config['scenarios']
        self.time_windows = config['time_windows']
        self.message_interval = config['message_interval']
        self.cooldown = config['cooldown']
        self.avoid_last_n = 50
        
        if not self.token:
            print(f"❌ LỖI: Không tìm thấy token cho bot '{self.bot_name}'. Vui lòng kiểm tra file .env.")
            return

        request_handler = HTTPXRequest(connect_timeout=30.0, read_timeout=30.0)
        self.bot = telegram.Bot(token=self.token, request=request_handler)
        
        self.recent_messages = {category: deque(maxlen=self.avoid_last_n) for category in self.scenarios.keys()}
        self.next_send_time = {}

    def get_unique_random_message(self, category):
        possible_messages = self.scenarios.get(category, [])
        if not possible_messages: return None
        shuffled_messages = random.sample(possible_messages, len(possible_messages))
        for message in shuffled_messages:
            if message not in self.recent_messages[category]:
                self.recent_messages[category].append(message)
                return message
        return random.choice(possible_messages)

    async def send_message_async(self, message):
        try:
            now_vn = datetime.now(VN_TZ)
            await self.bot.send_message(chat_id=CHAT_ID, text=message)
            print(f"✅ [{self.bot_name.upper()}] [{now_vn.strftime('%H:%M:%S')}] Đã gửi: {message}")
        except telegram.error.TimedOut:
            print(f"❌ [{self.bot_name.upper()}] Lỗi khi gửi tin nhắn: Timed out.")
        except Exception as e:
            print(f"❌ [{self.bot_name.upper()}] Lỗi khi gửi tin nhắn: {e}")

    def run_logic(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        if not hasattr(self, 'bot'):
            return
            
        initial_delay = random.randint(5, 25)
        print(f"[{self.bot_name.upper()}] Logic của Bot đang khởi động... Chờ {initial_delay} giây.")
        time.sleep(initial_delay)
        
        now_for_scheduling = datetime.now(VN_TZ)
        for category in self.scenarios.keys():
            min_delay = 5 
            max_delay = self.message_interval[1] // 3
            delay_minutes = random.randint(min_delay, max_delay)
            self.next_send_time[category] = now_for_scheduling + timedelta(minutes=delay_minutes)
        print(f"[{self.bot_name.upper()}] Đã lên lịch gửi tin nhắn đầu tiên.")

        while True:
            try:
                now = datetime.now(VN_TZ)
                current_time = now.time()

                if GLOBAL_ACTIVE_START <= current_time <= GLOBAL_ACTIVE_END:
                    for category, (start_hour, end_hour) in self.time_windows.items():
                        in_window = False
                        if start_hour <= end_hour:
                            if start_hour <= now.hour < end_hour: in_window = True
                        else:
                            if now.hour >= start_hour or now.hour < end_hour: in_window = True
                        
                        if in_window and now >= self.next_send_time.get(category):
                            message = self.get_unique_random_message(category)
                            if message:
                                loop.run_until_complete(self.send_message_async(message))
                                delay_minutes = random.randint(*self.message_interval)
                                self.next_send_time[category] = now + timedelta(minutes=delay_minutes)
                                cooldown_seconds = random.randint(*self.cooldown)
                                time.sleep(cooldown_seconds)
                                break
                    time.sleep(10)
                else:
                    print(f"[{self.bot_name.upper()}] Ngoài giờ hoạt động chung. Tạm nghỉ đến {GLOBAL_ACTIVE_START.strftime('%H:%M')} sáng mai...")
                    
                    tomorrow = now.date() + timedelta(days=1)
                    next_start_datetime = datetime.combine(tomorrow, GLOBAL_ACTIVE_START, tzinfo=VN_TZ)
                    
                    today_start_datetime = datetime.combine(now.date(), GLOBAL_ACTIVE_START, tzinfo=VN_TZ)
                    if now < today_start_datetime:
                         next_start_datetime = today_start_datetime

                    sleep_duration = (next_start_datetime - now).total_seconds()
                    sleep_duration += random.randint(1, 60)
                    
                    time.sleep(sleep_duration)

            except Exception as e:
                print(f"🔴 LỖI NGHIÊM TRỌNG trong vòng lặp của bot '{self.bot_name}': {e}")
                time.sleep(60)

BOT_CONFIGURATIONS = [
    {
        'name': "Minh Khoa",
        'token_env_var': "BOT_TOKEN_SINH_VIEN",
        'scenarios': SCENARIOS_SINH_VIEN,
        'time_windows': { "morning": (9, 12), "noon": (12, 14), "evening": (20, 2), "interaction": (0, 24), "experience_motivation": (0, 24) },
        'message_interval': (20, 50),
        'cooldown': (15, 60)
    },
    {
        'name': "Chú Ba",
        'token_env_var': "BOT_TOKEN_THO_HO",
        'scenarios': SCENARIOS_THO_HO,
        'time_windows': { "morning": (5, 8), "noon": (12, 13), "evening": (19, 22), "interaction": (0, 24), "experience_motivation": (0, 24) },
        'message_interval': (45, 90),
        'cooldown': (15, 60)
    },
    {
        'name': "Vy",
        'token_env_var': "BOT_TOKEN_VY",
        'scenarios': SCENARIOS_NOI_TRO_VY,
        'time_windows': { "morning": (8, 11), "noon": (13, 15), "evening": (21, 1), "interaction": (0, 24), "experience_motivation": (0, 24) },
        'message_interval': (30, 60),
        'cooldown': (15, 60)
    }
]

# Xóa hoàn toàn khối if __name__ == "__main__": ở đây.