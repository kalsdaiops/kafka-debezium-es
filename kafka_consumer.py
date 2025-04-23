from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'dbserver1.public.orders',
    bootstrap_servers = 'localhost:9092',
    value_deserializer = lambda m: json.loads(m.decode('utf-8'))
    )
for msg in consumer:
    data = msg.value
    if data['op'] in ('c', 'u'):  # Create/Update ops
        print(f"New order: {data['after']['order_id']} Amount: {data['after']['amount']}")