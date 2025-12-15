from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "socialpulse_topic",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="latest",
    enable_auto_commit=True
)

print("✅ 메시지 수신 대기 중...")
for message in consumer:
    data = message.value

    # case 1: X API 결과(JSON 안에 result → data 배열 존재)
    if isinstance(data, dict) and "result" in data and "data" in data["result"]:
        tweets = data["result"]["data"]
        for t in tweets:
            print("📩 트윗:", t["text"])

    # case 2: 단일 트윗 객체
    elif isinstance(data, dict) and "text" in data:
        print("📩 단일 트윗:", data["text"])

    # case 3: 예상치 못한 데이터
    else:
        print("📩 원본 메시지:", data)
