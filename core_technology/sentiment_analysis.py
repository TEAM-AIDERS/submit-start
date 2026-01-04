#import os
#os.environ["OPENAI_API_KEY"] = "본인 API 키"

from openai import OpenAI
import numpy as np

client = OpenAI()

sentiment_prompt = """
너는 K-POP 산업에서 실제로 사용되는 팬덤 반응을 분석해
엔터테인먼트사 홍보팀의 의사결정을 돕는 감정 분석 AI Agent다.

너의 분석 결과는 다음과 같은 실무 판단에 직접 사용된다:
- 공식 SNS 대응 여부 결정
- 위기 대응(사과문, 해명) 필요성 판단
- 밈 확산 시 무대응 또는 활용 판단
- 팬덤 분열/팬워 조짐 사전 감지

따라서 단순 긍·부정이 아니라,
팬덤 내부 맥락과 은어, 비꼼, 밈, 과장 표현을 정확히 해석해야 한다.
"""

sentiment_prompt += """
다음 팬덤 특화 감정 6종 중 하나로 분류하라:

1. 응원:
- 공연/무대/콘텐츠에 대한 긍정적 반응
- 팬심 강화, 재소비·확산 의도 포함

2. 실망:
- 기대 대비 아쉬움, 피로감, 현타 표현
- 비난보다는 감정적 거리두기 성격

3. 보이콧:
- 소비 중단, 불매, 항의 의사 표현
- 집단적 행동 가능성이 있는 강한 부정 감정

4. 밈화:
- 진지한 비판이 아닌 희화화, 농담, 패러디
- 감정 강도는 낮지만 확산력은 큼

5. 팬워:
- 특정 팬덤/멤버/그룹 간의 공격적 비교, 비난
- 갈등과 분열을 유발하는 표현

6. 중립:
- 정보 전달, 단순 언급, 감정 판단 어려움
"""

sentiment_prompt += """
다음 해석 규칙을 반드시 따른다:

- 팬덤 신조어는 일반 사전 의미가 아니라 팬덤 내 사용 맥락 기준으로 해석한다.
  예: 
  - '찢었다', '미쳤다' → 강한 응원
  - '현타' → 실망
  - '이게 맞나' → 실망 또는 보이콧 맥락

- 욕설이나 과격한 표현이 있더라도,
  팬덤 내부 농담이나 밈일 경우 감정 강도를 낮춰 판단한다.

- 짧은 문장, 초성, 이모지 위주의 문장도 맥락을 추론해 분류한다.
"""

sentiment_prompt += """
문장에 사진, 영상, 직캠, 무대 캡처 등에 대한 반응이 포함된 경우:

- 외형/의상/비주얼 칭찬 → 응원
- 표정/스타일 조롱, 캡처 밈 → 밈화
- 노출, 콘셉트, 연출 논란 → 실망 또는 보이콧 맥락 고려

예:
- '오늘 착장 미쳤다' → 응원
- '이 사진 또 돌아다니네 ㅋㅋ' → 밈화
- '이런 사진을 왜 올린 거지' → 실망
"""

sentiment_prompt = """
반드시 아래 JSON 형식으로만 출력하라.

형식:
{{
  "label": "응원 | 실망 | 보이콧 | 밈화 | 팬워 | 중립",
  "confidence": 0과 1 사이의 소수,
  "reason": "팬덤 맥락을 반영한 한 문장 설명"
}}

문장: "{text}"

추가 정보:
- 플랫폼: {platform}
- 이미지 포함 여부: {has_image}
- 영상 포함 여부: {has_video}
- 작성자 유형: {author_type}
"""

def analyze_sentiment(message):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{
            "role": "user",
            "content": sentiment_prompt.format(
                text=message["text"],
                platform=message["platform"],
                has_image=message["has_image"],
                has_video=message["has_video"],
                author_type=message["author_type"]
            )
        }]
    )
    return response.choices[0].message.content

fan_message = {
    "text": "오늘 무대 찢었다;;",
    "lang": "ko",
    "platform": "X",
    "has_image": False,
    "has_video": True,
    "author_type": "fan",
    "is_reply": False,
    "is_quote": False
}

result = analyze_sentiment(fan_message)
print(result)
