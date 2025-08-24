# Project: Docker Volumes & Persistence

## 📖 Overview
This project demonstrates how to persist data in Docker using:
- **Named Volumes** → for MySQL database persistence
- **Bind Mounts** → for accessing Nginx logs on the host machine

---

## 🛠️ Setup

### 1. MySQL with Volume Persistence
```bash
docker run -d \
  --name mysql-db \
  -e MYSQL_ROOT_PASSWORD=root \
  -v mysql_data:/var/lib/mysql \
  mysql:8.0
✅ Steps to test:

Create a database/table inside MySQL.

Stop and remove the container:
docker stop mysql-db && docker rm mysql-db
Restart the container with the same volume.

Confirm your DB data still exists.

2. Nginx with Bind Mount Logs
docker run -d \
  --name nginx-logs \
  -p 8081:80 \
  -v $(pwd)/logs:/var/log/nginx \
  nginx:alpine
Access http://localhost:8081

Check logs on host:


cat logs/access.log
📊 Expected Outputs
MySQL data persists even after container deletion.

Logs from Nginx appear in the host logs/ folder.