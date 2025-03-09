# fastapi-cicd

provide a step-by-step guide to setting up a CI/CD pipeline for your FastAPI project. The pipeline will use Docker and GitHub Actions to automate deployment.

# Docker run commands

    docker build -t fastapi-app .
    docker run -p 8000:8000 fastapi-app

# Docker hub

docker pull gopalsrinivas/fastapi-app:9d6b31b32c6123952f8ab7f52f8d1adf6ac797ba
docker run -d -p 8000:8000 gopalsrinivas/fastapi-app:9d6b31b32c6123952f8ab7f52f8d1adf6ac797ba
