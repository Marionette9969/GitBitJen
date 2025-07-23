@Library('jenkins-shared-library') _
def deploy = new Vanillara()

pipeline {
    agent { label 'agent1' }

    parameters {
        string( name: 'PRODUCT_NAME', description: 'Product Name', defaultValue: 'webdriver' )
        string( name: 'SERVICE_NAME', description: 'Service Name', defaultValue: 'webdriver' )
    }

    stages {
        stage('Checkout scm') {
            steps {
                checkout scm
                script {
                    sh 'echo -n $(git rev-parse --short HEAD) > ./commit-id'
                    commitId = readFile('./commit-id')
                }
            }
        }
        stage('FS and IaC Scan') {
            steps {
                script {
                    deploy.fsnIacScan(service: "${params.SERVICE_NAME}")
                }
            }
        }
        stage('Build Image') {
            steps {
                script {
                    deploy.buildImage(service: "${params.SERVICE_NAME}", tag: "${BUILD_NUMBER}-${commitId}")
                }
            }
        }
        stage('Image Scan') {
            steps {
                script {
                    deploy.imageScan(service: "${params.SERVICE_NAME}", tag: "${BUILD_NUMBER}-${commitId}")
                }
            }
        }
        stage('Push Registry') {
            steps {
                script {
                    deploy.pushRegistry(service: "${params.SERVICE_NAME}", tag: "${BUILD_NUMBER}-${commitId}")
                }
            }
        }
        stage('Deployment') {
            steps {
                script {
                    deploy.deployment(service: "${params.SERVICE_NAME}")
                }
            }
        }
    }
}
