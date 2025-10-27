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
# MỚI: Import các cấu trúc câu đã được nâng cấp
from kịch_bản.cau_truc_cau import SINH_VIEN_COMPONENTS, THO_HO_COMPONENTS, ME_BIM_COMPONENTS

load_dotenv()

CHAT_ID = os.getenv("CHAT_ID")
VN_TZ = timezone(timedelta(hours=7))

# =================================================================
# THỜI GIAN HOẠT ĐỘNG CHUNG ĐÃ ĐƯỢC CẬP NHẬT TẠI ĐÂY
# =================================================================
GLOBAL_ACTIVE_START = dt_time(6, 30)
GLOBAL_ACTIVE_END = dt_time(23, 30)


class TelegramBotPersona:
    def __init__(self, config):
        self.bot_name = config['name']
        self.token = os.getenv(config['token_env_var'])
        self.scenarios = config['scenarios']
        self.components = config.get('components', {})
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
        
        available_messages = [m for m in possible_messages if m not in self.recent_messages[category]]
        if not available_messages:
            self.recent_messages[category].clear()
            available_messages = possible_messages

        message = random.choice(available_messages)
        self.recent_messages[category].append(message)
        return message

    # =================================================================
    # NÂNG CẤP LỚN: HÀM TẠO CÂU ĐA CẤU TRÚC
    # =================================================================
    def generate_human_message(self, base_message):
        if not self.components or not base_message:
            return base_message

        comp = self.components
        
        # --- ĐỊNH NGHĨA CÁC CẤU TRÚC CÂU (KỊCH BẢN NÓI CHUYỆN) ---

        # Cấu trúc 1: Chào hỏi + Nội dung chính + Câu kết cảm xúc
        def template_greeting_statement_closing(base, c):
            greeting = random.choice(c.get("greetings", [""]))
            closing = random.choice(c.get("closings", [""]))
            return f"{greeting} {base[0].lower()}{base[1:]}. {closing}"

        # Cấu trúc 2: Nội dung chính + Câu hỏi tương tác
        def template_statement_question(base, c):
            question = random.choice(c.get("questions", [""]))
            # Bỏ dấu câu cũ nếu có
            if base.endswith(('.', '!', '?')): base = base[:-1]
            return f"{base}, {question}"

        # Cấu trúc 3: Nội dung chính + Tự suy ngẫm
        def template_statement_reflection(base, c):
            reflection = random.choice(c.get("self_reflections", [""]))
            return f"{base}. {reflection}"

        # Cấu trúc 4: Lời dẫn/suy nghĩ + Nội dung chính
        def template_filler_statement(base, c):
            filler = random.choice(c.get("fillers", [""]))
            return f"{filler}, {base[0].lower()}{base[1:]}."
        
        # Cấu trúc 5: Tương tác với nhóm + Câu kết cảm xúc
        def template_interaction_closing(base, c):
            interaction = random.choice(c.get("interactions", [""]))
            closing = random.choice(c.get("closings", [""]))
            return f"{interaction} {closing}"

        # Cấu trúc 6: Chỉ một câu chào và một câu hỏi (kịch bản check-in)
        def template_greeting_question(base, c):
            greeting = random.choice(c.get("greetings", [""]))
            question = random.choice(c.get("questions", [""]))
            return f"{greeting} {question}"
            
        # Cấu trúc 7: Câu gốc đơn giản (để giữ sự đa dạng)
        def template_base_only(base, c):
            return base

        # --- CHỌN NGẪU NHIÊN MỘT CẤU TRÚC ---
        
        # Danh sách các kịch bản có thể xảy ra, một số kịch bản có trọng số cao hơn (lặp lại)
        templates = [
            template_greeting_statement_closing,
            template_statement_question,
            template_statement_question, # Tăng xác suất
            template_statement_reflection,
            template_filler_statement,
            template_interaction_closing,
            template_greeting_question,
            template_base_only,
            template_base_only # Tăng xác suất
        ]
        
        # Chọn ngẫu nhiên một template từ danh sách
        chosen_template = random.choice(templates)
        
        # Tạo câu hoàn chỉnh dựa trên template đã chọn
        return chosen_template(base_message, comp)

    async def send_message_async(self, message):
        try:
            # === THAY ĐỔI #1: SỬA LỖI MÚI GIỜ KHI IN LOG ===
            now_vn = datetime.now(timezone.utc).astimezone(VN_TZ)
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

        # === THAY ĐỔI #2: SỬA LỖI MÚI GIỜ KHI LÊN LỊCH BAN ĐẦU ===
        now_for_scheduling = datetime.now(timezone.utc).astimezone(VN_TZ)
        for category in self.scenarios.keys():
            min_delay = 5
            max_delay = self.message_interval[1] // 3
            delay_minutes = random.randint(min_delay, max_delay)
            self.next_send_time[category] = now_for_scheduling + timedelta(minutes=delay_minutes)
        print(f"[{self.bot_name.upper()}] Đã lên lịch gửi tin nhắn đầu tiên.")

        while True:
            try:
                # === THAY ĐỔI #3: SỬA LỖI MÚI GIỜ TRONG VÒNG LẶP CHÍNH ===
                # Lấy giờ UTC hiện tại (luôn chính xác trên mọi server)
                now_utc = datetime.now(timezone.utc)
                # Chuyển đổi tường minh sang múi giờ Việt Nam
                now = now_utc.astimezone(VN_TZ)
                
                current_time = now.time()

                if GLOBAL_ACTIVE_START <= current_time <= GLOBAL_ACTIVE_END:
                    for category, (start_hour, end_hour) in self.time_windows.items():
                        in_window = False
                        if start_hour <= end_hour:
                            if start_hour <= now.hour < end_hour: in_window = True
                        else:
                            if now.hour >= start_hour or now.hour < end_hour: in_window = True

                        if in_window and now >= self.next_send_time.get(category, now):
                            base_message = self.get_unique_random_message(category)
                            if base_message:
                                final_message = self.generate_human_message(base_message)
                                
                                loop.run_until_complete(self.send_message_async(final_message))
                                
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
                    if sleep_duration > 0:
                        sleep_duration += random.randint(1, 60)
                        time.sleep(sleep_duration)

            except Exception as e:
                print(f"🔴 LỖI NGHIÊM TRỌNG trong vòng lặp của bot '{self.bot_name}': {e}")
                time.sleep(60)

# Cấu hình Bot, không cần thay đổi gì ở đây
BOT_CONFIGURATIONS = [
    {
        'name': "Minh Khoa",
        'token_env_var': "BOT_TOKEN_SINH_VIEN",
        'scenarios': SCENARIOS_SINH_VIEN,
        'components': SINH_VIEN_COMPONENTS,
        'time_windows': { "morning": (9, 12), "noon": (12, 14), "evening": (20, 2), "interaction": (0, 24), "experience_motivation": (0, 24) },
        'message_interval': (20, 50),
        'cooldown': (15, 60)
    },
    {
        'name': "Chú Ba",
        'token_env_var': "BOT_TOKEN_THO_HO",
        'scenarios': SCENARIOS_THO_HO,
        'components': THO_HO_COMPONENTS,
        'time_windows': { "morning": (5, 8), "noon": (12, 13), "evening": (19, 22), "interaction": (0, 24), "experience_motivation": (0, 24) },
        'message_interval': (45, 90),
        'cooldown': (15, 60)
    },
    {
        'name': "Vy",
        'token_env_var': "BOT_TOKEN_VY",
        'scenarios': SCENARIOS_NOI_TRO_VY,
        'components': ME_BIM_COMPONENTS,
        'time_windows': { "morning": (8, 11), "noon": (13, 15), "evening": (21, 1), "interaction": (0, 24), "experience_motivation": (0, 24) },
        'message_interval': (30, 60),
        'cooldown': (15, 60)
    }
]