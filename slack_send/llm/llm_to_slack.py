import os
from datetime import datetime
from dotenv import load_dotenv
from slack_sdk import WebClient

from inputs.sample_input import sample_issue
from report_generator import generate_report

def main():
    load_dotenv()

    print("[DOPLIN] 입력 이슈 로드 완료")
    print(f"[DOPLIN] 대상 아티스트: {sample_issue['idol']}")

    # 리포트 생성
    print("[DOPLIN] LLM 리포트 생성 요청 중...")
    try:
            report_text = generate_report(sample_issue)
            print("[DOPLIN] 리포트 생성 완료")
    except Exception as e:
        print("[DOPLIN][ERROR] 리포트 생성 실패")
        print(e)
        return


    # Slack 전송
    slack_client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("[DOPLIN] Slack 전송 중...")

    try:
        slack_client.chat_postMessage(
            channel=os.getenv("SLACK_CHANNEL_ID"),
            text=(
                "🚨 *Doplin 팬덤 이슈 대응 리포트*\n"
                f"_생성 시각: {timestamp}_\n\n"
                f"{report_text}"
            )
        )
        print("[DOPLIN] Slack 전송 완료")
    except Exception as e:
        print("[DOPLIN][ERROR] Slack 전송 실패")
        print(e)
        return



if __name__ == "__main__":
    main()