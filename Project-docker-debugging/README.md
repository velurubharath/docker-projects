# 🐳 Project 6 – Docker Debugging (Troubleshooting Containers)

This project demonstrates **real-world debugging techniques** for Docker containers.  
It simulates common container issues and provides step-by-step fixes, showcasing how a DevOps engineer would troubleshoot in production.

---

## 📂 Project Structure
Project-docker-debugging/
│── Dockerfile
│── requirements.txt
│── app.py
│── README.md

---

## 🚀 Steps

### 1️⃣ Build the App
```bash
docker build -t debug-app .
2️⃣ Run the App
docker run -p 5002:5000 debug-app
Initially, the container will fail — we will debug and fix step by step.

🔍 Debugging Scenarios
🐞 1. Missing Dependencies
Problem: Flask not installed → ModuleNotFoundError: No module named 'flask'

Debugging:

docker logs <container_id>
docker exec -it <container_id> sh
Fix:
Add to Dockerfile:

RUN pip install --no-cache-dir -r requirements.txt
🐞 2. Port Mismatch
Problem: Container runs but app not reachable.

Debugging:

docker logs <container_id>
docker inspect <container_id> | grep -i port
Fix:
Expose the correct port:

dockerfile

EXPOSE 5000
Run with:

docker run -p 8080:5000 debug-app
🐞 3. Wrong CMD
Problem: Container exits immediately with error.

Debugging:

docker ps -a
docker logs <container_id>
Fix:
Ensure CMD is correct:

dockerfile

CMD ["python", "app.py"]
🐞 4. Permission Errors
Problem: App files copied with wrong permissions.

Debugging:

docker exec -it <container_id> sh
ls -l

Fix:

dockerfile

RUN chmod +x app.py

🛠️ Debugging Tools Cheat Sheet
Command	Purpose
docker ps -a	List running/stopped containers
docker logs <id>	View container logs
docker exec -it <id> sh	Get interactive shell inside container
docker inspect <id>	Inspect metadata (ports, env, volumes)
docker stats	Monitor CPU, memory usage
docker events	View real-time events
docker system df	Disk space usage of Docker