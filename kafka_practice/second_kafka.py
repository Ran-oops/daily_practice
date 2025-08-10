from kafka import KafkaConsumer
import json


def safe_deserialize(value):
    if value is None:
        return "空消息"

    try:
        # 尝试 UTF-8 解码
        decoded = value.decode('utf-8')
    except UnicodeDecodeError:
        try:
            # 尝试其他编码
            decoded = value.decode('latin-1')
        except:
            return f"无法解码的消息: {value.hex()}"

    try:
        # 尝试 JSON 解析
        return json.loads(decoded)
    except json.JSONDecodeError:
        # 如果不是 JSON，返回原始字符串
        return decoded


# 创建消费者
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='python-consumer-group',
    value_deserializer=safe_deserialize  # 使用新的安全反序列化函数
)

print("消费者已启动，等待消息... (按 Ctrl+C 停止)")

try:
    for message in consumer:
        print(f"""
        收到消息:
        主题: {message.topic}
        分区: {message.partition}
        偏移量: {message.offset}
        键: {message.key}
        值: {message.value}
        """)
except KeyboardInterrupt:
    print("停止消费")
finally:
    consumer.close()