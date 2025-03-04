# MLOps CI/CD Pipeline

This project automates the ML workflow using Jenkins, GitHub Actions, and Docker.

## 🔧 Tools Used
- Jenkins
- GitHub Actions
- Docker
- Flask
- Python
- Flake8

## 🚀 How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/tahahasan01/i211767_i211695.git

   # 🚀 MLOps CI/CD Pipeline for ML Model Deployment

This project implements a **CI/CD pipeline** for a Machine Learning model using **GitHub Actions, Jenkins, Docker, and Flask**.  
The pipeline ensures **automated testing, linting, and deployment** whenever new code is pushed.  

🔹 **GitHub Actions** checks code quality & runs unit tests.  
🔹 **Jenkins** builds and deploys the application in a **Docker container**.  
🔹 **Docker Hub** stores the containerized application.  
🔹 **Flask API** serves the ML model predictions.  
🔹 **Admin receives an email notification** upon successful deployment.  

## 📂 Repository Structure

i211767_i211695/        # Root directory (GitHub Repository)
│
├── .github/            # GitHub Actions workflows
│   ├── workflows/
│   │   ├── lint.yml    # Flake8 Code Quality Check
│   │   ├── test.yml    # Unit Testing
│
├── app/                # Main application directory
│   ├── model.py        # ML model script
│   ├── app.py          # Flask API for the model
│
├── tests/              # Unit testing directory
│   ├── test_model.py   # Unit tests for ML model
│
├── Dockerfile          # Containerization
├── Jenkinsfile         # Jenkins CI/CD pipeline
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
├── report.pdf          # Final report
└── .gitignore          # Ignore unnecessary files

## 🔀 Branching Strategy
This project follows the **Git Flow** strategy:

- `dev` → Active development & new features.
- `test` → Runs unit tests & code validation.
- `main` → Stable, tested code ready for deployment.
- `master` → Final production-ready code that triggers Jenkins deployment.

### **🔹 Workflow:**
1. Developers push code to **`dev`**.
2. A **GitHub Actions workflow** runs Flake8 to check code quality.
3. If successful, a **pull request (PR) to `test`** is created.
4. `test` branch runs **unit tests**.
5. If tests pass, PR is merged into **`main`**.
6. `main` is merged into **`master`**, triggering **Jenkins to deploy the app in Docker**.

## 🛠️ Technologies Used
✅ **Python (Flask, NumPy)** → ML Model & API  
✅ **GitHub Actions** → Automates linting & unit tests  
✅ **Jenkins** → Automates Docker build & deployment  
✅ **Docker** → Containerizes the application  
✅ **Git & GitHub** → Version control & collaboration  
✅ **Email Notifications** → Alerts admin on successful deployment  

## 🔍 Code Quality Check (GitHub Actions & Flake8)
Before merging any code, **GitHub Actions runs Flake8** to ensure clean, error-free Python code.


---

### **📌 7. Deployment with Jenkins & Docker**
Explain how the application is deployed.

```md
## 📦 Deployment with Jenkins & Docker
Merging into `master` triggers **Jenkins**, which:
1️⃣ **Builds a Docker image**  
2️⃣ **Pushes it to Docker Hub**  
3️⃣ **Deploys the Flask app inside a container**

📌 **File:** `Jenkinsfile`
```groovy
pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/tahahasan01/i211767_i211695.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t mymlapp .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    sh 'docker tag mymlapp username/mymlapp:latest'
                    sh 'docker push username/mymlapp:latest'
                }
            }
        }
    }
}


---

### **📌 8. Admin Notification**
Explain how the admin receives an email after deployment.

```md
## 📧 Admin Notification
After a successful deployment, **Jenkins sends an email to the admin**.

📌 **Jenkinsfile Email Notification**
```groovy
stage('Notify Admin') {
    steps {
        mail to: 'admin@example.com',
             subject: 'Deployment Successful',
             body: 'The ML application has been deployed successfully.'
    }
}

