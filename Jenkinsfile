pipeline {
    agent any
    
    environment {

        PATH = "C:\\WINDOWS\\SYSTEM32;C:\\Program Files\\Docker\\Docker\\resources\\bin"
    }

    stages {    
        
        stage('Build, Push, Live) {
            steps {
                script{
                    dockerImage = docker.build("icyguy/i190476_i190695_mlops_a2:latest")
                    if(dockerImage){ // If the image was created successfully, then carry out the other procedures - pushing onto the registry, and making it go live.
                        withDockerRegistry([credentialsId: "dockerhub", url: ""]) {
                            dockerImage.push()
                        }
                        bat "docker run -d -p 8090:5000 icyguy/i190476_i190695_mlops_a2:latest"
                    }else{
                        error "There was an issue while trying to build a Docker image. Please try again."
                    }
                }
            }
        }        
    }
}
