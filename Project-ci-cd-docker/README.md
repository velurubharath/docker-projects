# 🚀 CI/CD with Docker + GitHub Actions

This project demonstrates a simple **Flask application** containerized with Docker and deployed using **GitHub Actions**.

### 🛠 Tech Stack
- Python + Flask
- Docker (multi-stage build)
- GitHub Actions for CI/CD
- DockerHub (for image storage)

### 🔄 Workflow
1. Push code to `main` branch.
2. GitHub Actions builds a Docker image.
3. The image is pushed to **DockerHub**.
4. Deployment job pulls and runs the container.

### ▶️ Run Locally
```bash
cd app
docker build -t ci-cd-flask .
docker run -p 5000:5000 ci-cd-flask

🌐 Access App

Local: http://localhost:5000

Deployed: Runs automatically via GitHub Actions