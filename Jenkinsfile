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
         
         
        stage('Clone repository') {
            steps {
                bat '''git clone https://github.com/NUCES-ISB/i190476_i190695_MLOps_Assignment-02.git .'''
            }
        }
        
        
        stage('Build image') {
            steps {
                bat '''docker -v'''
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
