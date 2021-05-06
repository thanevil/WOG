pipeline {			
    agent {label 'mac'}			
    stages {
        stage ("clone") {	
            steps {
                git "https://github.com/thanevil/WOG.git"
               
            }
        }
        stage ("tar gz and rotate versions") {
            steps {
                script {
                sh '''

                cd /Users/admin/jenkins-node/workspace/WOG-pipeline
                tar -czvf WOG.tar.gz ./*
                cd /Users/admin/Desktop/WOG-rotation
                sh rotation.sh
                cd /Users/admin/jenkins-node/workspace/WOG-pipeline
                mv -v WOG.tar.gz /Users/admin/Desktop/WOG-rotation/'''
                }
            }
        }
    }
}
