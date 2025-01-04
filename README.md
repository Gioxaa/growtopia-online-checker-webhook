# 🌐 Growtopia Online Players Webhook

This project is a Python script that monitors the number of online players in Growtopia and sends updates to a Discord channel via a webhook. The script also calculates changes in player count and detects significant drops (ban waves).

## 📫 Features

- **Real-Time Player Count**: Fetches the current online player count from the Growtopia website.
- **Change Detection**: Calculates the difference in player count (absolute and percentage) from the previous update.
- **Ban Wave Alerts**: Detects and notifies about significant drops in player count (e.g., ban waves).
- **Discord Webhook Integration**: Sends formatted messages to a specified Discord channel.

## ⏳ Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Gioxaa/growtopia-online-checker-webhook.git
    cd growtopia-online-checker-webhook
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate # For Linux/Mac
    venv\Scripts\activate    # For Windows
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure the webhook:
   - Open the script file (`main.py`) and replace the placeholder with your Discord webhook URL:
     ```python
     webhook_url = "https://discord.com/api/webhooks/..."
     ```
   - Optionally, customize the webhook name (`webhook_name`) and avatar URL (`avatar_url`) to fit your needs.

5. Run the script:
    ```bash
    python main.py
    ```
### Example:
![png](https://cdn.discordapp.com/attachments/1314910846803247217/1325057772492029983/image.png?ex=677a67b7&is=67791637&hm=cfb408a2e1f351ff484aaea075085ad09719c5ff354f36901b01894f494d449c&)

## 💡 Tips

- **Adjust Update Interval**: Modify the `time.sleep(60)` line in the script to change the frequency of updates (default is 60 seconds).
- **Keep Webhook Secure**: Ensure that your webhook URL is private to prevent unauthorized use.
- **Network Errors**: If there are connection issues, check your internet connection or ensure the Growtopia website is accessible.

## 🔧 Customization

You can further customize the script:
- **Message Formatting**: Modify the `message` variable in the script for different notification styles.
- **Thresholds**: Adjust the ban wave detection logic to change the sensitivity of alerts.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute or provide suggestions to enhance the functionality of this project!
