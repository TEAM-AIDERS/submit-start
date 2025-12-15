# llm/report_generator.py
from openai import OpenAI
import os

def build_prompt(issue: dict) -> str:
    return f"""
당신은 K-POP 팬덤 이슈 대응을 전문으로 하는 PR 전략 AI입니다.

[이슈 정보]
- 아티스트: {issue['idol']}
- 플랫폼: {issue['platform']}
- 이슈 요약: {issue['issue_summary']}
- 팬 감정 비율:
  - 긍정 {issue['fan_sentiment']['positive']*100:.0f}%
  - 중립 {issue['fan_sentiment']['neutral']*100:.0f}%
  - 부정 {issue['fan_sentiment']['negative']*100:.0f}%
- 주요 키워드: {", ".join(issue['top_keywords'])}
- 유사 과거 이슈: {issue['similar_past_issue']}
- 긴급도: {issue['urgency']}

[요청]
1. 현재 상황 요약 (1문장)
2. 기획사 대응 전략 2~3가지
3. 팬 커뮤니케이션 시 유의점
4. 위 전략을 바탕으로,
   - 팬들에게 공개 가능한 공식 사과문 초안을 작성하세요.
   - 과도한 법적 표현은 피하고, 공감과 책임 인식이 드러나게 작성하세요.
   - 5~6문장 이내로 간결하게 작성하세요.
   
한국어로 존댓말을 유지하며 작성해 주세요.

[출력 형식]
아래 형식을 반드시 지켜서 출력하세요.
---REPORT_START---
1. 현재 상황 요약
2. 기획사 대응 전략 2~3가지
3. 팬 커뮤니케이션 시 유의점
---REPORT_END---

---APOLOGY_START---

---APOLOGY_END---

"""
    

def generate_report(issue: dict) -> dict:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = build_prompt(issue)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    text = response.output_text

    report = text.split("---REPORT_START---")[1].split("---REPORT_END---")[0].strip()
    apology = text.split("---APOLOGY_START---")[1].split("---APOLOGY_END---")[0].strip()

    return {
        "report": report,
        "apology": apology
    }
