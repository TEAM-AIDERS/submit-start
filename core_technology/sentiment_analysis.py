#import os
#os.environ["OPENAI_API_KEY"] = "본인 API 키"

from openai import OpenAI
import numpy as np

client = OpenAI()

sentiment_prompt = 
"""
너는 K-POP 팬덤 분석 전문가다.

다음 문장을 팬덤 특화 감정 6종 중 하나로 분류하라:
[응원, 실망, 보이콧, 밈화, 팬워, 중립]

팬덤 신조어는 팬덤 내 의미 기준으로 해석한다.
(예: '찢었다', '미쳤다', '현타')

반드시 JSON 형식으로만 출력하라.

형식:
{{
  "label": "...",
  "confidence": 0~1 사이 숫자,
  "reason": "한 문장 설명"
}}

문장: "{text}"
"""

def analyze_sentiment(text):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{
            "role": "user",
            "content": sentiment_prompt.format(text=text)
        }]
    )
    return response.choices[0].message.content

text = "오늘 무대 찢었다;;"
sentiment_result = analyze_sentiment(text)
print(sentiment_result)

