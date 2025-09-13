🐳 Docker Networking Project – Docker Networking with Realtime Application
This project is designed as a practical lab to explore and understand Docker networking concepts using a real application stack involving a frontend, backend, and PostgreSQL database.

It includes interactive debugging, simulated network failures, and live testing with Docker CLI.

📚 Table of Contents
🚀 Project Overview
📁 Project Structure
🧠 Key Docker Networking Concepts
⚙️ Setup Instructions
🛠️ Docker Commands Reference
🔍 Test & Debug Networking
🔥 Simulate Network Failures
🧪 Tools for Network Debugging
✅ Learning Outcomes
🚀 Project Overview
Component	Description
frontend	NGINX container serving static content
backend	FastAPI application running on port 8000
db	PostgreSQL database container
All services are connected via a custom Docker network (app-net) to simulate real-world container communication.

📁 Project Structure
docker-networking/ ├── backend/ │ ├── main.py │ ├── requirements.txt │ └── Dockerfile ├── frontend/ │ └── Dockerfile ├── docker-compose.yml └── README.md

🧠 Key Docker Networking Concepts
Docker Networks: Bridge containers for private communication
Service Discovery: Access containers by name (backend, db) using Docker DNS
Port Publishing: Expose container ports to host using ports: in Docker Compose
Network Isolation: Containers not in same network cannot communicate
DNS Failures, Port Mapping Issues, Network Disconnects are testable in this setup
⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/<your-username>/docker-networking-lab.git
cd docker-networking-lab
docker-compose up -d --build

| Task                         | Command                                               |
| ---------------------------- | ----------------------------------------------------- |
| Start services               | `docker-compose up -d --build`                        |
| Stop all containers          | `docker-compose down`                                 |
| View logs                    | `docker-compose logs -f`                              |
| View containers              | `docker ps`                                           |
| Inspect networks             | `docker network ls` / `docker network inspect <name>` |
| Connect container to network | `docker network connect <network> <container>`        |
| Disconnect container         | `docker network disconnect <network> <container>`     |


Run a Test Container in App Network:
docker run -it --rm --network=docker-networking_app-net ubuntu bash

Install Tools in Test Container:
apt update && apt install iputils-ping curl net-tools dnsutils postgresql-client -y

Test Connectivity:
ping backend
curl http://backend:8000
psql -h db -U postgres -d testdb
