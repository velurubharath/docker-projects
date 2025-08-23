🟦🟩 Blue-Green Deployment with Docker & NGINX

This project demonstrates the Blue-Green Deployment Strategy using Docker Compose, Flask, and NGINX.
Blue-Green deployment allows zero-downtime releases by running two application versions (Blue & Green) in parallel, and routing traffic between them.

📂 Project Structure
Project-blue-green-deployment/
│── Dockerfile.blue       # Builds Blue version of app
│── Dockerfile.green      # Builds Green version of app
│── requirements.txt      # Flask dependency
│── docker-compose.blue.yaml
│── docker-compose.green.yaml
│── nginx.conf
│── app_v1.py             # Blue app
│── app_v2.py             # Green app
│── README.md

⚙️ Setup & Run
1️⃣ Build and Run Blue Environment
docker-compose -f docker-compose.blue.yaml up --build -d

2️⃣ Build and Run Green Environment
docker-compose -f docker-compose.green.yaml up --build -d

🌐 Access the Application

NGINX Proxy (Main Entry Point) → http://localhost:8080

Internally:

Blue app runs at app_blue:5000

Green app runs at app_green:5000

🔄 Switching Traffic

Start with Blue Deployment (stable version).

Deploy Green Deployment with new version (app_v2.py).

Update nginx.conf to switch upstream from app_blue → app_green.

Reload NGINX inside the container:

docker exec -it nginx_proxy nginx -s reload

✅ Verify

Curl test:

curl http://localhost:8080


Response will change depending on which app version (Blue/Green) NGINX routes to.