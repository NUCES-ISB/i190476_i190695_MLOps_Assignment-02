pipeline {
    agent any
    
    environment {

        PATH = "C:\\WINDOWS\\SYSTEM32"

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
                bat 'set'
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
