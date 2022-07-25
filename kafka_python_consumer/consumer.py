from kafka import KafkaConsumer

consumer = KafkaConsumer('rover-metrics', bootstrap_servers='rover-cluster-kafka-bootstrap:9092')

for msg in consumer:
    print (msg)