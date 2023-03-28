pipeline {
    agent any
    
    environment {

        PATH = "C:\\WINDOWS\\SYSTEM32;C:\\Program Files\\Docker\\Docker\\resources\\bin"
    }

    stages {    
        
        stage('Build image') {
            steps {
                script{
                    dockerImage = docker.build("icyguy/i190476_i190695_mlops_a2:latest")
                }
            }
        }
        
        if (dockerImage) {
            stage('Push image') {
                steps {
                    script {
                        withDockerRegistry([credentialsId: "dockerhub", url: ""]) {
                            dockerImage.push()
                        }
                    }
                }
            }
        
            stage('Go live') {
                steps {
                    bat "docker run -d -p 8090:5000 icyguy/i190476_i190695_mlops_a2:latest"
                }
            }
        }
        
    }
}

