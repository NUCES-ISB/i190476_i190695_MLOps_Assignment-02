pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t i190476_i190695 .'
            }
        }
    }
}
