# 🚀 Project: Multi-Service App with Docker Compose (Flask + Redis + Nginx)

This project demonstrates how to containerize and orchestrate a **multi-service application** using **Docker Compose**.  
The architecture consists of:

- **Flask App** → Simple Python web application (backend)  
- **Redis** → In-memory database/cache  
- **Nginx** → Reverse proxy to route traffic to the Flask app  

This is a real-world DevOps pattern for deploying microservices with a proxy and DB/cache layer.

---

## 📂 Project Structure
Project-compose-app-redis/
│── app/
│ ├── app.py # Flask application
│ ├── requirements.txt # Python dependencies
│ └── Dockerfile # Backend image build
│
├── nginx/
│ ├── nginx.conf # Reverse proxy configuration
│ └── Dockerfile # Custom Nginx image
│
├── docker-compose.yaml # Multi-service orchestration file
└── README.md # Documentation


---

## ⚙️ How to Run

### 1️⃣ Clone the repo

#Start Services
docker-compose up --build

#Verifying Running COntainers
docker ps

You should see flask-app, redis, and nginx.

#Access the app

Open browser → http://localhost:8080

The request flows: Nginx → Flask app → Redis

🖼️ Architecture Diagram
           +-------------+
           |   Browser   |
           +------+------+ 
                  |
                  v
           +------+------+ 
           |    Nginx   |  (Reverse Proxy)
           +------+------+ 
                  |
        +---------+---------+
        |                   |
        v                   v
   +----+----+         +----+----+
   |  Flask  |  <----> |  Redis  |
   +---------+         +---------+

🧪 Example Output

After hitting http://localhost:8080:

Hello from Bharath Docker's portfolio!. PageViews: 1
Hello from Bharath Docker's portfolio!. PageViews: 2

Refreshing will increment the counter.

🔑 Key DevOps Concepts Showcased

Multi-container orchestration with Docker Compose

Reverse proxy setup using Nginx

Using Redis for persistence/caching

Container networking (all services share same network)

Declarative config (docker-compose.yaml)
