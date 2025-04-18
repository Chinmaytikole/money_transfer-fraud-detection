pipeline {
    agent none

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
                docker build -t fraud-app:latest .
                """
            }
        }
    }
}
