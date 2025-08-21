# 📊 Docker Monitoring with Prometheus & Grafana

This project demonstrates how to set up **Docker container monitoring** using:
- [Prometheus](https://prometheus.io/) → for metrics collection  
- [cAdvisor](https://github.com/google/cadvisor) → for container resource metrics  
- [Grafana](https://grafana.com/) → for visualization  

---

## 🚀 Project Setup

### 1. Clone the repo
```bash
git clone this repositoryt
cd docker-projects/Project-docker-monitoring
2. Start the monitoring stack

docker-compose up -d
This will start:

Prometheus → http://localhost:9090

cAdvisor → http://localhost:8080

Grafana → http://localhost:3000

⚙️ Configuration
Prometheus
Config file: prometheus.yml

Scrapes metrics from:

cAdvisor (Docker container metrics)

node_exporter (optional system-level metrics)

Check Prometheus targets at: http://localhost:9090/targets

Grafana
Default login:
user: admin
pass: admin

Import dashboard:

Go to Dashboards → Import

Use Docker & System Monitoring Dashboard ID: 193

Set data source = Prometheus

📊 Metrics Collected
CPU usage per container

Memory usage per container

Network I/O

Disk I/O

Running container count

🐞 Troubleshooting
If metrics show N/A in Grafana:

Check Prometheus is running at port 9090

Verify targets → http://localhost:9090/targets

Update Grafana data source → http://prometheus:9090

✅ Next Steps
Add Alertmanager for email/Slack alerts

Push metrics to remote Prometheus/Thanos for long-term storage

Add Node Exporter to monitor host machine

📂 Project Structure

Project-docker-monitoring/
│── docker-compose.yml
│── prometheus.yml
│── README.md
