pipeline {
    agent any
    
    environment {

        PATH = "C:\\WINDOWS\\SYSTEM32;C:\\Program Files\\Docker\\Docker\\resources\\bin"
    }

    stages {    
        
        stage('Build image, Push to Hub, Go Live') {
            steps {
                script{
                    dockerImage = docker.build("abdullahajaz/i190476_i190695_mlops_a2:latest")
                    if(dockerImage){
                        withDockerRegistry([credentialsId: "dockerhub", url: ""]) {
                            dockerImage.push()
                        }
                        bat "docker run -d -p 8090:5000 abdullahajaz/i190476_i190695_mlops_a2:latest"
                    }else{
                        error "Docker image build failed."
                    }
                }
            }
        }        
    }
}

