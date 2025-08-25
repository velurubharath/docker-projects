## 📌 Day 14 – `Project-docker-performance/README.md`

# Project: Docker Performance & Resource Control

## 📖 Overview
This project explores performance tuning and reliability:
- CPU & Memory Limits
- Healthchecks
- Multi-arch builds

---

## 🛠️ Setup

### 1. Resource Limits
```bash
docker run -d \
  --name stress-test \
  --cpus="0.5" \
  --memory="256m" \
  polinux/stress --cpu 1 --vm 1 --vm-bytes 128M --timeout 30s
Check usage:

docker stats
2. Healthcheck
Add to Dockerfile:

HEALTHCHECK --interval=30s --timeout=5s \
  CMD curl -f http://localhost:5000/health || exit 1
Check container health:
docker ps
3. Multi-arch Build

docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t myapp:multiarch .

📊 Expected Outputs
Resource usage is capped (via docker stats).

Healthcheck shows healthy/unhealthy.

Multi-arch image is built and pushed.