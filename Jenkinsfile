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
                // Use Gradle to build the project
                sh './gradlew build'
            }
        }

        stage('Test') {
            steps {
                // Run tests using Gradle
                sh './gradlew test'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
