
pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/chinnabathuni/django-helloworld-jenkins.git'
            }
        }

        stage('Build') {
            steps {
                sh '''
                python3 -m venv $VENV_DIR
                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                source $VENV_DIR/bin/activate
                python manage.py test
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                echo "Deploying Django app..."
                pkill -f gunicorn || true
                source $VENV_DIR/bin/activate
                nohup gunicorn helloworld.wsgi:application --bind 0.0.0.0:8000 &
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build, Test, and Deploy completed successfully!'
        }
        failure {
            echo '❌ Build failed. Check Jenkins logs.'
        }
    }
}
