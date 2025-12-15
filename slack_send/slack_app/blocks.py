# slack/blocks.py
from datetime import datetime

def build_blocks(issue: dict, report_text: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    return [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🚨 DOLPIN 팬덤 이슈 대응 리포트",
                "emoji": True
            }
        },
        {
            "type": "context",
            "elements": [
                {"type": "mrkdwn", "text": f"*아티스트:* {issue['idol']}"},
                {"type": "mrkdwn", "text": f"*생성 시각:* {timestamp}"}
            ]
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "*📌 현재 상황 요약*"}
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*이슈 유형*\n{issue['issue_summary']}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*부정 반응 비율*\n:red_circle: *{int(issue['fan_sentiment']['negative']*100)}%*"
                }
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "📍 *분석 출처:* Twitter(X), YouTube 댓글, 팬 커뮤니티 (최근 6시간)"
                }
            ]
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "*📝 공식 사과문 초안*"}
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"```{report_text}```"
            }
        },
        {"type": "divider"},
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "👀 확인 완료"},
                    "style": "primary",
                    "value": "acknowledged"
                },
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "📊 상세 분석 보기"},
                    # "url": "추후 대시보드 url 추가"
                }
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "_본 리포트는 의사결정을 보조하기 위한 AI 기반 분석 결과이며, 최종 판단 및 책임은 담당자에게 있습니다._"
                },
                {
                    "type": "mrkdwn",
                    "text": "💡 *Powered by DOLPIN*"
                }
            ]
        }
    ]
