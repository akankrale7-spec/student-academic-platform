pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
        DOCKER_IMAGE_NAME = 'student-academic-platform'
        IMAGE_TAG = "v1.${BUILD_NUMBER}"
    }

    stages {
        stage('SCM Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Environment Setup') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Linting') {
            steps {
                sh '''
                    . venv/bin/activate
                    flake8 app/ database/ --count --select=E9,F63,F7,F82 --show-source --statistics
                '''
            }
        }

        stage('Automated Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    mkdir -p reports
                    pytest -v --cov=app --junitxml=reports/test-results.xml tests/
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t ${DOCKER_IMAGE_NAME}:${IMAGE_TAG} .
                    docker tag ${DOCKER_IMAGE_NAME}:${IMAGE_TAG} ${DOCKER_IMAGE_NAME}:latest
                '''
            }
        }

        stage('Kubernetes Deployment') {
            steps {
                sh '''
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/test-results.xml'
        }
        success {
            echo "CI/CD pipeline completed successfully."
        }
        failure {
            echo "CI/CD pipeline failed. Check the console log."
        }
    }
}
