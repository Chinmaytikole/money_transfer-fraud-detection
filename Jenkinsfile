pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = credentials('dockerhub-username')
        DOCKERHUB_PASSWORD = credentials('dockerhub-password')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Chinmaytikole/money_transfer-fraud-detection.git'
            }
        }

        stage('Install') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest > test_results.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat """
                echo %DOCKERHUB_PASSWORD% | docker login -u %DOCKERHUB_USERNAME% --password-stdin
                docker build -t %DOCKERHUB_USERNAME%/fraud-app:latest .
                docker push %DOCKERHUB_USERNAME%/fraud-app:latest
                """
            }
        }
    }
}
