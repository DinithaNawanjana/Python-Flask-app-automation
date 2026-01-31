pipeline {
    agent any 

    environment(
        DOCKER_CREDS= credentials('docker-hub-login')
        REGISTRY_USER ='dinitha282'

    )

    stages {
        stage ('checkout from github'){
            echo "Checking from Github..."
        }
        stage ('Build image'){
            echo "Building image..."
            sh "docker build -t ${REGISTRY_USER}/my-web-app:v1 ."
        }
        stage ('Login and push'){
            sh 'echo $DOCKER_CREDS_PSW | docker login -u $DOCKER_CREDS_USR --password-stdin'
            sh "docker push ${REGISTRY_USER}/my-web-app:v1"
        }
        stage ('Run image'){
            echo "Deployoing image..."
            sh 'docker stop my-website || true'
            sh 'docker rm my-website || true'

            sh "docker run -d -p 5000:5000 --name my-website ${REGISTRY_USER}/my-web-app:v1"
        }
    }
}