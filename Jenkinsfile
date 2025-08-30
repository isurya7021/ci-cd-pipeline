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
                git url: 'https://github.com/isurya7021/ci-cd-pipeline.git', branch: 'main', credentialsId: 'github-token'
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
