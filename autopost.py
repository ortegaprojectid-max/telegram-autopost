import requests, schedule, time

TOKEN = "8458918879:AAH4WYwVC8UCv9c_FvPs8EfrZ2NVXWEaWOk"
CHAT_ID = "@temancerita_kmu"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def post_message():
    text = "🌙 Selamat malam semua...\nSemoga tidurmu nyenyak dan mimpi indah menemanimu ✨"
    requests.post(URL, data={"chat_id": CHAT_ID, "text": text})
    print("Pesan terkirim ke channel!")

# auto kirim jam 22:00
schedule.every().day.at("22:00").do(post_message)

while True:
    schedule.run_pending()
    time.sleep(1)
