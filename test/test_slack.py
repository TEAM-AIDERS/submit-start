import os
from dotenv import load_dotenv
from slack_sdk import WebClient

load_dotenv()

client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

client.chat_postMessage(
    channel=os.getenv("SLACK_CHANNEL_ID"),
    text="Dolpin Slack Bot 테스트 성공!"
)
print("Slack message sent successfully.")