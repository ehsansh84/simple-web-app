docker build -t webapp .
docker stop webapp || true
docker rm webapp || true
docker run -d --name webapp -p 8001:8000 webapp

