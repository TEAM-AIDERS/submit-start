# app/llm_to_slack.py
from dotenv import load_dotenv
from inputs.sample_input import sample_issue
from llm.report_generator import generate_report
from slack_app.blocks import build_blocks 
from slack_app.sender import send_blocks

def main():
    load_dotenv()

    print("[DOLPIN] 입력 이슈 로드 완료")
    print(f"[DOLPIN] 대상 아티스트: {sample_issue['idol']}")

    try:
        print("[DOLPIN] LLM 리포트 생성 중...")
        result = generate_report(sample_issue)
        print("[DOLPIN] 리포트 생성 완료")
    except Exception as e:
        print("[DOLPIN][ERROR] 리포트 생성 실패")
        print(e)
        return

    try:
        print("[DOLPIN] Slack Block Kit 생성 중...")
        blocks = build_blocks(sample_issue, result["report"], result["apology"])

        print("[DOLPIN] Slack 전송 중...")
        send_blocks(blocks)
        print("[DOLPIN] Slack 전송 완료")
    except Exception as e:
        print("[DOLPIN][ERROR] Slack 전송 실패")
        print(e)

if __name__ == "__main__":
    main()
