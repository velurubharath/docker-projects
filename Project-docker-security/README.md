## 📌 Day 13 – `Project-docker-security/README.md`

# Project: Docker Security Best Practices

## 📖 Overview
This project focuses on improving Docker container security:
1. Running as **non-root user**
2. **Image vulnerability scanning** with Trivy
3. Handling **secrets** securely

---

## 🛠️ Setup

### 1. Non-root Flask App
Dockerfile:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd -m appuser
USER appuser
CMD ["python", "app.py"]
2. Image Scanning with Trivy

trivy image flask-app:latest
✅ Expected → Report of CVEs with severity levels.

3. Secrets Management
Option A: Using .env file

docker run --env-file .env flask-app:latest
Option B: Docker Swarm Secrets

echo "mypassword" | docker secret create db_password -
docker service create --name myapp --secret db_password flask-app:latest
📊 Expected Outputs
Container runs without root.

Trivy scan shows vulnerabilities.

App reads secret without hardcoding.