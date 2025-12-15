summary_prompt = 
"""
다음 팬덤 반응을 이슈 요약 한 문장으로 정리하라.

조건:
- 감정 상태 포함
- 논란/이슈의 핵심만 요약
- 중립적인 서술

입력:
감정 분석 결과:
{sentiment}

원문:
"{text}"
"""

def summarize_issue(text, sentiment):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{
            "role": "user",
            "content": summary_prompt.format(
                sentiment=sentiment,
                text=text
            )
        }]
    )
    return response.choices[0].message.content

issue_summary = summarize_issue(text, sentiment_result)
print(issue_summary)

past_issues = [
    "컴백 무대 퀄리티가 높아 팬덤 호응이 급증한 사례",
    "의상 논란으로 팬덤 내 실망 여론이 확산된 사례",
    "팬덤 간 비교 발언으로 팬워가 발생한 사례",
    "방송사 편집 문제로 보이콧 움직임이 생긴 사례",
    "콘셉트 변경으로 밈화되며 가볍게 소비된 사례"
]

def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

query_vec = embed(issue_summary)
past_vecs = [embed(t) for t in past_issues]

scores = [
    (past_issues[i], cosine(query_vec, past_vecs[i]))
    for i in range(len(past_issues))
]

scores.sort(key=lambda x: x[1], reverse=True)

print("입력 문장:", text)
print("이슈 요약:", issue_summary)
print("\n유사한 과거 이슈 Top 3:\n")

for issue, score in scores[:3]:
    print(f"- {issue} (유사도: {round(score, 3)})")
