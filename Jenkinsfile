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
        
        stage('Push image') {
            steps {
                script {
                    if (dockerImage) {
                        withDockerRegistry([credentialsId: "dockerhub", url: ""]) {
                            dockerImage.push()
                        }
                    else {
                        error "Could not build a Docker image."   
                    }
                }
            }
        }

        stage('Go live') {
            steps {
                if (dockerImage) {
                    bat "docker run -d -p 8090:5000 icyguy/i190476_i190695_mlops_a2:latest"
                }
                else {
                    error "Could not run the docker image; check if the docket image has been built first.   
                }
            }
        }
        
    }
}

