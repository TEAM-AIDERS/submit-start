from kafka import KafkaProducer
import json
import time

# Kafka Producer 설정
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# 더미 트윗 5개 생성
dummy_tweets = [
    {"author_id": "user_1", "text": "리쿠 너무 귀여워!", "created_at": "2025-12-15T18:00:00Z"},
    {"author_id": "user_2", "text": "팬싸 후기 미쳤다 ㄹㅇ", "created_at": "2025-12-15T18:01:00Z"},
    {"author_id": "user_3", "text": "총공 언제 시작이야?", "created_at": "2025-12-15T18:02:00Z"},
    {"author_id": "user_4", "text": "이번 컨셉 대박이다", "created_at": "2025-12-15T18:03:00Z"},
    {"author_id": "user_5", "text": "보이콧 얘기 나오는 거 실화냐", "created_at": "2025-12-15T18:04:00Z"},
]

for tweet in dummy_tweets:
    producer.send("socialpulse_topic", value=tweet)
    print("📤 [Producer] 더미 트윗 발행:", tweet)
    time.sleep(1)

producer.flush()
print("✅ 더미 트윗 발행 완료")
