pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from GitHub
                git branch: 'main', url: 'https://github.com/Sample1forgit/Sample.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Bulding...'
                sh 'npm install'
            }
        }

        stage('Test') {
            steps {
               echo 'Testing...'
                sh 'npm test'
            }
        }
    }


}
