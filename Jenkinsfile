
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'krithika2013/course-registration'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"D:\\CourseRegistration\\.venv\\Scripts\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"D:\\CourseRegistration\\.venv\\Scripts\\python.exe" -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:v1 .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKERHUB_USER',
                        passwordVariable: 'DOCKERHUB_TOKEN'
                    )
                ]) {
                    bat '''
                        echo %DOCKERHUB_TOKEN% | docker login --username %DOCKERHUB_USER% --password-stdin
                        docker push %IMAGE_NAME%:v1
                        docker logout
                    '''
                }
            }
        }
    }
}
