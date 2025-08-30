pipeline {
    agent any
    environment {
        IMAGE_NAME = "myapp"
        IMAGE_TAG = "latest"
        DOCKER_REGISTRY = "localhost:8082/docker_local"
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'file:///media/suryasen/New Volume/workspace/cicd-lab/sample-app'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME:$IMAGE_TAG .
                docker tag $IMAGE_NAME:$IMAGE_TAG $DOCKER_REGISTRY/$IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }
        stage('Push to Nexus Registry') {
            steps {
                sh '''
                docker push $DOCKER_REGISTRY/$IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }
        stage('Deploy with Ansible') {
            steps {
                sh '''
                ansible-playbook -i hosts.ini deploy.yml
                '''
            }
        }
    }
}
