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
        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_HUB_USR', passwordVariable: 'DOCKER_HUB_PSW')]) {
                        sh "echo ${DOCKER_HUB_PSW} | docker login -u ${DOCKER_HUB_USR} --password-stdin"
                        sh "docker push ${DOCKER_IMAGE}"
                    }
                }
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
