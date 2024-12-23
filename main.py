import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from discord_webhook import DiscordWebhook

url = "https://growtopiagame.com/detail"

webhook_url = "https://discord.com/api/webhooks/1319359991206908038/FnwlJy20c1pNufWP-Wg17yi1lMFfvnGe9i-vbxU2MuCjQHwcMm-an1lkXXEpRXJVGht1"
webhook_name = "Growtopia Logs"
avatar_url = "https://cdn.discordapp.com/avatars/1306112669765603432/a_73aea43cb627a5463fb050880244c06f.gif?size=4096&ignore=true"

def get_online_user():
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.text
        start_index = data.find('"online_user":"') + len('"online_user":"')
        end_index = data.find('"', start_index)
        online_user = int(data[start_index:end_index])
        return online_user
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return None

def send_to_discord(message):
    webhook = DiscordWebhook(
        url=webhook_url,
        content=message,
        username=webhook_name,
        avatar_url=avatar_url
    )
    response = webhook.execute()
    if response.status_code == 200:
        print("Pesan terkirim ke Discord.")
    else:
        print(f"Gagal mengirim pesan: {response.status_code}")

prev_online_user = None

while True:
    current_time = int(datetime.now().timestamp())
    online_user = get_online_user()

    if online_user is not None:
        if prev_online_user is not None:
            diff = online_user - prev_online_user
            diff_text = f"+{diff}" if diff > 0 else f"{diff}"
            percent_diff = (diff / prev_online_user) * 100
            percent_diff_text = f"{percent_diff:+.2f}%"

            message = f"[<t:{current_time}:F>] <a:live:1306036979124801608> **Online Players: {online_user} ({diff_text} | {percent_diff_text})**"
            if diff < -1000:
                message += f"\n[<t:{current_time}:F>] <a:alert:1306298772124336178> **Ban Wave Detected! {online_user} ({diff_text} | {percent_diff_text})**"

        else:
            message = f"[<t:{current_time}:F>] <a:live:1306036979124801608> **Online Players: {online_user}**"
        send_to_discord(message)
        prev_online_user = online_user

    time.sleep(60)
