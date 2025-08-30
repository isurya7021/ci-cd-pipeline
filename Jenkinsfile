pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/isurya7021/ci-cd-pipeline.git'
        APP_NAME = 'myapp'
        VERSION = "1.0.${BUILD_NUMBER}"
        NEXUS_URL = 'http://localhost:8081'
        NEXUS_REPO = 'python-packages'
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
                set -e  # stop on first error

                # Create and activate virtual environment
                python3 -m venv venv
                source venv/bin/activate

                # Upgrade packaging tools
                pip install --upgrade pip setuptools wheel

                # Build package with Jenkins VERSION
                BUILD_VERSION=${VERSION} python setup.py sdist bdist_wheel

                echo "Build complete. Artifacts:"
                ls -lh dist/
                '''
            }
        }

        stage('Upload to Nexus') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'nexus-credentials', 
                                                passwordVariable: 'NEXUS_PASS', 
                                                usernameVariable: 'NEXUS_USER')]) {
                    sh '''#!/bin/bash
                    set -e
                    source venv/bin/activate || true

                    # Find the built wheel
                    ARTIFACT=$(ls dist/myapp-${VERSION}-py3-none-any.whl | head -n 1)

                    if [ ! -f "$ARTIFACT" ]; then
                        echo "ERROR: Artifact not found for version ${VERSION}"
                        exit 1
                    fi

                    BASENAME=$(basename $ARTIFACT)

                    echo "Uploading $BASENAME to Nexus..."
                    curl -u $NEXUS_USER:$NEXUS_PASS --upload-file $ARTIFACT \
                        $NEXUS_URL/repository/$NEXUS_REPO/$BASENAME
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
