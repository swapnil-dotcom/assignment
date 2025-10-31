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

        stage("Install dependencies") {
            steps {
                bat '''
                %PYTHON% -m pip install -r requirements.txt
                '''
            }
        }

        stage("ETL Pipeline"){
            steps {
                bat '''
                %PYTHON% etl.py
                '''
            }
        }
    }
}