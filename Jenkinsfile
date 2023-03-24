pipeline {
    agent any
    stages {
        stage('Build Dockerfile') {
            steps {
                script{
                    sh 'docker build -t i190476_i190695_a2 .'
                }
            }
        }
    }
}
