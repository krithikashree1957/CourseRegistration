
pipeline {
    agent any

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
    }
}
