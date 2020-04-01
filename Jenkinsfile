stages {
  stage('Development') {
    steps {
      // One or more steps need to be included within the steps block.
    }

    input {
      message 'What do you want?'
    }
  }

  stage('QA') {
    stages {
      // One or more stages need to be included within the stages block.
    }

    environment {
      env = "QA"
    }
  }

  stage('Bench') {
    stages {
      // One or more stages need to be included within the stages block.
    }

    environment {
      env = "QA"
    }
  }

}
