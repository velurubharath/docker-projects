# Project 1 – Hello Docker 🚀

## 📌 Objective
This project demonstrates a basic Flask web app running inside a Docker container.

---

## 🔹 Steps to Run

1. **Build the image**
   ```bash
   docker build -t hello-docker .
2. Run  Conainer
docker run -d -p 8080:5000 --name myapp hello-docker

3. Test in Browser or Curl
   curl http://localhost:8080

  Expected Code: Hello from Bharath! Running inside Docker
4. View Logs:
    docker logs myapp

5. Cleanup:
     docker stop myapp && docker rm myapp
     docker rmi hello-docker
