pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t i190476_i190695 .'
            }
        }
    }
}
