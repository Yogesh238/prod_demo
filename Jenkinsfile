  
pipeline {
    agent any
  stages {   
        stage('Ok') {
            steps {
                echo "Ok"
            }
        }
      stage('Infra Sanity Check') {
          steps{
                 sh 'python3 approve.py'
                }
          } 
  }
}      
              
//          stage("Stage with input") {
//     steps {
//       def userInput = false
//         script {
//             def userInput = input(id: 'Proceed1', message: 'Promote build?', parameters: [[$class: 'BooleanParameterDefinition', defaultValue: true, description: '', name: 'Please confirm you agree with this']])
//             echo 'userInput: ' + userInput

//             if(userInput == true) {
//                 // do action
//               echo "pass"
//             } else {
//                 // not do action
//                 echo "Action was aborted."
//             }

//         }    
//     }  
//          }
//     post {
//         always {
//            emailext (
//   subject: "Waiting for your Approval! Job: '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
//   body: """<p>STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
//               <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
//  recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']]
// )
//         }
