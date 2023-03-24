pipeline {
    agent any
    tools {
        docker { image 'python:3.9.16' }
    }
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
