pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('Initialize'){
            def dockerHome = tool 'myDocker'
            env.PATH = "${dockerHome}/bin:${env.PATH}"
        }
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
