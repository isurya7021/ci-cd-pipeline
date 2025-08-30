pipeline {
    agent any

    environment {
        NEXUS_URL = "http://nexus.example.com:8081/repository/pypi-internal/"
        NEXUS_REPO = "pypi-internal"
        NEXUS_CREDENTIALS = "nexus-creds"   // Jenkins Credentials ID
        ANSIBLE_INVENTORY = "ansible/inventory/hosts.ini"
        APP_NAME = "my-python-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/isurya7021/ci-cd-pipeline.git'
            }
        }

        stage('Package') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip setuptools wheel
                    python setup.py sdist bdist_wheel
                '''
            }
        }

        stage('Publish to Nexus') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${NEXUS_CREDENTIALS}",
                                                 usernameVariable: 'NEXUS_USER',
                                                 passwordVariable: 'NEXUS_PASS')]) {
                    sh '''
                        PACKAGE_FILE=$(ls dist/*.tar.gz | head -n 1)
                        VERSION=$(echo $PACKAGE_FILE | sed -E 's/.*-([0-9.]+).tar.gz/\\1/')
                        echo "Package version: $VERSION" > version.txt
                        curl -v -u $NEXUS_USER:$NEXUS_PASS \
                          --upload-file $PACKAGE_FILE \
                          ${NEXUS_URL}
                    '''
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                script {
                    def version = readFile('version.txt').trim().split(': ')[1]
                    sh """
                        ansible-playbook -i ${ANSIBLE_INVENTORY} ansible/deploy.yml \
                          --extra-vars "app_name=${APP_NAME} package_version=${version}"
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful!"
        }
        failure {
            echo "❌ Deployment failed. Check logs."
        }
    }
}
