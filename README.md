# Enterprise Student Record & Academic Management Platform

A Flask-based academic management application demonstrating Git, GitHub, Pytest, Jenkins CI, Docker and Kubernetes/Minikube.

## Features
- Student registration and lookup
- Faculty and course management
- Course enrollment
- Maximum 18 credits per semester
- Grade recording
- REST API
- Automated tests
- Docker containerization
- Jenkins CI pipeline
- Kubernetes deployment with 3 replicas

## Run locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

Open:
`http://localhost:5000/api/health`

## Test

```bash
pytest -v --cov=app --junitxml=reports/test-results.xml tests/
```

## Docker

```bash
docker build -t student-academic-platform:v1.0.0 .
docker run -d -p 5000:5000 --name academic-container student-academic-platform:v1.0.0
curl http://localhost:5000/api/health
```

## Kubernetes / Minikube

```bash
minikube start --driver=docker
eval $(minikube docker-env)
docker build -t student-academic-platform:v1.0.0 .
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods
kubectl get svc academic-service
minikube service academic-service --url
```

## Suggested GitHub branches

- feature/foundation
- feature/core-app
- feature/automated-tests
- feature/jenkins-ci
- feature/dockerization
- feature/kubernetes-orchestration
- main

## Academic mapping

The trainer case study uses books, users and loans. This student version uses students, faculty, courses, enrollments and grades, with an 18-credit semester limit.
