🚀 Flask App with Docker Multi-Stage Builds

📌 Overview

This project demonstrates how to containerize a simple Flask web application using Docker multi-stage builds.
The goal is to showcase best practices for building lightweight, production-ready images.

![Build Status](https://github.com/velurubharath/docker-projects/actions/workflows/docker-build.yml/badge.svg)
Hello from Bharath. MultiStages!

🛠 Tech Stack
Language: Python 3.9
Framework: Flask
Containerization: Docker (multi-stage builds)
Base Images: python:3.9, python:3.9-slim
CI/CD: GitHub Actions (build & test workflow)

🔧 Build the Image
docker build -t flask-Multistage Dockerfile .

▶️ Run the Container
docker run -d -p 5000:5000 flask-Multistage

🌍 Test the App
curl http://localhost:5000

#Difference in sizes:
$ docker images | grep flask
flask                         latest    3a6380b24bab   About a minute ago   125MB
flask.normal                  latest    029abd7bc3e8   34 minutes ago       1.1GB



✅ Why Multi-Stage Builds?

Reduce image size (only copy runtime deps)
Isolate build tools from production runtime
Cleaner & more secure Docker images

