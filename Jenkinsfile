pipeline {
    agent any
    
    environment {

        PATH = "C:\\WINDOWS\\SYSTEM32;C:\\Program Files\\Docker\\Docker\\resources\\bin"
    }

    stages {    
        
        stage('Build image') {
            steps {
                script{
                    dockerImage = docker.build("abdullahajaz/i190476_i190695_a2:latest")
                }
            }
        }
        
//         stage('Push image') {
//             steps {
//                 script {
//                     withDockerRegistry([credentialsId: "docker_hub", url: ""]) {
//                         dockerImage.push()
//                     }
//                 }
//             }
//         }
        
    }
}

