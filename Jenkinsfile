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
            }
        }

        stage('Test') {
            steps {
               echo 'Testing...'
            }
        }
    }


}
