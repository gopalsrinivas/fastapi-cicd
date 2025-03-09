# fastapi-cicd

provide a step-by-step guide to setting up a CI/CD pipeline for your FastAPI project. The pipeline will use Docker and GitHub Actions to automate deployment.

# Docker run commands

    docker build -t fastapi-app .
    docker run -p 8000:8000 fastapi-app
