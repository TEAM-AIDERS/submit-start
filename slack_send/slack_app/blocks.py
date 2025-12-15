# slack/blocks.py
from datetime import datetime
from llm.report_generator import generate_report
from inputs.sample_input import sample_issue


def build_blocks(issue: dict, report_text: str, apology_text: str) -> list:
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
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "⚠️ *위험도:* 빠른 확산 단계 — 1차 공식 대응 권장"
            }
        ]
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*🎯  권장 대응 전략*"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "• *신속한 공식 입장 발표*\n"
                "불확실한 추측 확산 이전에 사실 기반 입장 공개\n\n"
                "• *내부 조사 및 재발 방지 커뮤니케이션*\n"
                "콘셉트 개발 프로세스 점검 및 개선 의지 명확화\n\n"
                "• *팬 소통 강화*\n"
                "SNS 및 공식 커뮤니티를 통한 감정 공감 중심 소통"
            )
        }
    },
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*💬  팬 커뮤니케이션 가이드*"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*DO*\n• 감정 공감 우선\n• 명확하고 쉬운 표현\n• 빠른 초기 반응"
            },
            {
                "type": "mrkdwn",
                "text": "*DON'T*\n• 법적·방어적 표현\n• 책임 회피성 언급\n• 기계적 반복 답변"
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
                "text": f"```{apology_text}```"
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
