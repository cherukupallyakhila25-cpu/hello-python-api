pipeline {

    agent any

    stages {

        stage('Clone GitHub') {
            steps {
                git 'https://github.com/cherukupallyakhila25/hello-python-api.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t hello-python-api .'
            }
        }

        stage('Run Docker Container') {
            steps {

                bat 'docker stop hello-container || exit 0'
                bat 'docker rm hello-container || exit 0'

                bat 'docker run -d -p 5000:5000 --name hello-container hello-python-api'
            }
        }
    }
}
