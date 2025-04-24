# 📊 Kafka Debezium Elasticsearch CDC Project

A **standalone setup** to capture changes from a **PostgreSQL database** using **Debezium**, stream them into **Apache Kafka**, and push the data into **Elasticsearch** for indexing and analytics.

---

## 🔧 Stack Used

- **PostgreSQL** – Source database for CDC
- **Debezium** – Change data capture engine
- **Apache Kafka** – Messaging system
- **Kafka Connect (Standalone)** – For Debezium and Elasticsearch connectors
- **Elasticsearch** – Target sink

---

## 🗂️ Project Structure

```
.
├── debezium-postgres.json           # Source connector config
├── es-sink.json                     # Sink connector config (Elasticsearch)
├── orders-es-sink.json             # Refined sink config
├── kafka_consumer.py                # Optional Kafka topic consumer (debugging)
├── kafka_2.13-3.7.0/                # Kafka binaries
├── plugins/                        # Debezium and Elasticsearch connector jars
├── requirements.txt
└── README.md
```

---

## 🚀 Setup Instructions (Standalone)

### 🖥️ Terminal 1 – Start Zookeeper
```bash
cd kafka_2.13-3.7.0
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### 🖥️ Terminal 2 – Start Kafka Broker
```bash
cd kafka_2.13-3.7.0
bin/kafka-server-start.sh config/server.properties
```

### 🖥️ Terminal 3 – Start Kafka Connect (Standalone)
```bash
cd kafka_2.13-3.7.0
export CLASSPATH=$(find ../plugins/ -name '*.jar' | tr '\n' ':')
bin/connect-standalone.sh config/connect-standalone.properties \
  ../debezium-postgres.json \
  ../orders-es-sink.json
```

Make sure the paths point to the correct plugin JARs.

---

## ✅ Verify the Setup

### Kafka Topic:
```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 \
  --topic dbserver1.public.orders --from-beginning
```

### Elasticsearch:
```bash
curl -X GET "http://localhost:9200/dbserver1.public.orders/_search?pretty"
```

---

## 📌 .gitignore Notes

```
venv/
*.pyc
__pycache__/
*.log
*.tgz
*.tar.gz
.DS_Store
*.dylib
kafka_2.13-3.7.0/libs/
plugins/
```

> Ensure large files (>100MB) are not pushed. GitHub blocks them. Consider using [Git LFS](https://git-lfs.github.com/) if needed.

---

## 📦 Future Improvements

- [ ] Docker-compose setup
- [ ] Health checks & dashboards
- [ ] Improved config validation

---

## 🙌 Contribution

PRs welcome! Open issues for bugs or suggestions.


