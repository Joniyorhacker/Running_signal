import time
import requests
from datetime import datetime
import random

# ==============================
# CONFIGURATION
# ==============================
BOT_TOKEN = "8348108389:AAGrurEUGwwmozWUXuA3Aa6zN0SG2lpcW7c"
ADMINS = ["@shahedbintarek"]
REFER_LINK = "https://dkwin9.com/#/register?invitationCode=16532572738"
CHAT_IDS = [-1002713215068]  # Fixed group Chat ID

# ==============================
# FUNCTIONS
# ==============================
def send_signal(chat_id, message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Error sending message to {chat_id}: {e}")

def get_market_signal():
    """
    DK Win / Wingo 1-Minute Market Signals
    Randomly Big / Small / Red / Green / Win generate করে
    """
    options = ["Big", "Small", "Red", "Green", "Win"]
    return random.choice(options)

# ==============================
# MAIN LOOP
# ==============================
def main():
    print("DK Win / Wingo Market Signal Bot চালু হচ্ছে...")
    
    while True:
        signal = get_market_signal()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = (
            f"[{timestamp}] Signal: {signal}\n"
            f"Refer: {REFER_LINK}\n"
            f"Admin: {', '.join(ADMINS)}"
        )
        for chat_id in CHAT_IDS:
            send_signal(chat_id, message)
        print(message)
        time.sleep(60)  # প্রতি ১ মিনিটে নতুন সিগন্যাল

if __name__ == "__main__":
    main()
