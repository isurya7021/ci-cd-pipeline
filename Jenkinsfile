pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/isurya7021/ci-cd-pipeline.git'
        APP_NAME = 'myapp'
        VERSION = "1.0.${BUILD_NUMBER}"
        NEXUS_URL = 'http://localhost:8081'
        NEXUS_REPO = 'pypi-releases'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-credentials',
                    url: "${REPO_URL}"
            }
        }

        stage('Build Package') {
            steps {
                sh '''#!/bin/bash
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip setuptools wheel
                BUILD_VERSION=$VERSION python setup.py sdist bdist_wheel
                '''
            }
        }

        stage('Upload to Nexus') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'nexus-credentials', passwordVariable: 'NEXUS_PASS', usernameVariable: 'NEXUS_USER')]) {
                    sh '''
                    ARTIFACT=$(ls dist/*.whl | head -n 1)
                    curl -u $NEXUS_USER:$NEXUS_PASS --upload-file $ARTIFACT \
                        $NEXUS_URL/repository/$NEXUS_REPO/$APP_NAME-$VERSION-py3-none-any.whl
                    '''
                }
            }
        }

        stage('Trigger Ansible Deployment') {
            steps {
                sh '''
                ansible-playbook -i ansible/inventory ansible/deploy.yml \
                    --extra-vars "version=$VERSION app_name=$APP_NAME nexus_url=$NEXUS_URL repo=$NEXUS_REPO"
                '''
            }
        }
    }
}
