# Project 5 – Private Docker Registry with Flask App

This project demonstrates how to:
- Build a simple Flask application using Docker.
- Push the image to a **local private Docker registry**.
- Pull the image from the registry and run it as a container.

---

## 📂 Project Structure
Project-docker-registry/
│── Dockerfile
│── requirements.txt
│── app.py


---

## 🛠️ Steps to Run

### 1️⃣ Start a Local Docker Registry
```bash
docker run -d -p 5000:5000 --name registry registry:2
This runs a registry on http://localhost:5000.

2️⃣ Build the Flask Application Image

docker build -t myapp:v1 .
3️⃣ Tag the Image for Local Registry

docker tag myapp:v1 localhost:5000/myapp:v1
4️⃣ Push the Image to the Registry

docker push localhost:5000/myapp:v1
5️⃣ Pull the Image from the Registry

docker pull localhost:5000/myapp:v1
6️⃣ Run the Container

docker run -d -p 5001:5000 localhost:5000/myapp:v1
Now the Flask app should be accessible at:

👉 http://localhost:5001