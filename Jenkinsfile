pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'chinmaytikole/devops_project:latest'
        DOCKERHUB_USERNAME = 'chinmaytikole'
        DOCKERHUB_PASSWORD = '123456789'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Chinmaytikole/money_transfer-fraud-detection.git', branch: 'main'
            }
        }

        stage('Install') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }


        stage('Build Docker Image') {
            steps {
                bat """
                docker build -t fraud-app:latest .
                """
            }
        }
        
        stage('Compose & Deploy') {
            steps {
                bat 'docker-compose down'
                bat 'docker-compose up -d'
            }
        }
    }
}
