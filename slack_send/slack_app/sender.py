# slack/sender.py
import os
from slack_sdk import WebClient

def send_blocks(blocks):
    client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

    client.chat_postMessage(
        channel=os.getenv("SLACK_CHANNEL_ID"),
        text="DOLPIN 팬덤 이슈 대응 리포트가 생성되었습니다.",
        blocks=blocks
    )
