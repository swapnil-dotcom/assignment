pipeline {
    agent any 
    environment {
        PYTHON="C:\\Users\\Hp\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
    }

    stages {
        stage("Checkout") {
            steps{
                checkout scm
            }
        }

        stage("Build Image") {
            steps {
                bat 'docker build =t myimage .'
            }
        }

        stage("ETL Pipeline"){
            steps {
                bat 'docker run -d -p 8501:8501 myimage'
            }
        }
    }
}