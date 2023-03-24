pipeline {
    agent any
    
    environment {

        PATH = "C:\\WINDOWS\\SYSTEM32"
        docker = "C:\Program Files\Docker\Docker\resources\bin"
    }

    stages {
//        stage('delete Existing clone') {
//             steps {
//                 catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
//                     bat '''rd /q /s .'''
//                 }
//             }
//         }        
        
        stage('Build image') {
            steps {
                bat 'docker -v'
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
