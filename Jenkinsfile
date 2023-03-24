// pipeline {
//     agent any

//     stages {
//         stage('Build Docker Image') {
//             steps {
//                 echo "Testing"
//             }
//         }
//     }
// }
pipeline {
    agent {
        docker { image 'python:3.9.16' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}
