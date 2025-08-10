from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    security_protocol='PLAINTEXT'  # 生产环境用 SASL_SSL
)

producer.send('test-topic', b'Hello dayu!')
producer.flush()