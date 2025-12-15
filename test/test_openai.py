import os
from dotenv import load_dotenv
from openai import OpenAI

# .env 로드
load_dotenv()

# OpenAI 클라이언트 생성
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 테스트 요청
response = client.responses.create(
    model="gpt-4.1-mini",
    input="아이돌 팬덤 이슈 대응 전략을 한 문장으로 써줘."
)

# 결과 출력
print("=== OpenAI 응답 ===")
print(response.output_text)
print("OpenAI request completed successfully.")