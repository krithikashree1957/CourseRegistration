
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'krithika2013/course-registration'
        DOCKER_EXE = 'C:\\Users\\LENOVO\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
        PYTHON_EXE = 'D:\\CourseRegistration\\.venv\\Scripts\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON_EXE%" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"%PYTHON_EXE%" -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"%DOCKER_EXE%" build -t %IMAGE_NAME%:v1 .'
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
                        echo %DOCKERHUB_TOKEN% | "%DOCKER_EXE%" login --username %DOCKERHUB_USER% --password-stdin
                        if errorlevel 1 exit /b 1

                        "%DOCKER_EXE%" push %IMAGE_NAME%:v1
                        if errorlevel 1 exit /b 1

                        "%DOCKER_EXE%" logout
                    '''
                }
            }
        }
    }
}
