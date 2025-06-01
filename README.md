# CI/CD Assignment – PROG8860

## 📌 Project Name
**ci-cd-assignment-denish-8901001**

## 👨‍💻 Author
Denish Akbari – Student ID: 8901001

---

## 🔧 Technologies Used
- Python 3.11
- Flask 2.3.2
- Docker
- GitHub Actions
- Werkzeug (Pinned to < 3.0.0 for compatibility)

---

## 📁 Folder Structure

```
ci-cd-assignment-denish-8901001/
├── app/
│   ├── app.py
│   ├── test_app.py
│   └── requirements.txt
├── .github/
│   └── workflows/
│       └── denish-ci-pipeline.yml
├── Dockerfile
├── README.md
```

---

## 🚀 How to Run the App

### ▶️ Run Locally Without Docker
```bash
pip install -r app/requirements.txt
python app/app.py
```

Visit: `http://localhost:5000`

---

### 🐳 Run with Docker

#### 1. Build the Image
```bash
docker build -t flask-app .
```

#### 2. Run the Container
```bash
docker run -d -p 5000:5000 --name flask-app flask-app
```

#### 3. Access in Browser
```
http://localhost:5000
```

#### 4. Stop the Container
```bash
docker stop flask-app
docker rm flask-app
```

---

## 🔄 GitHub Actions CI/CD Pipeline

### Trigger:
Runs automatically on:
- **Push** to `assignment1-denish-8901001`
- **Pull Request** to `assignment1-denish-8901001`

### Stages:
| Stage              | Description                            |
|--------------------|----------------------------------------|
| **Build**          | Installs dependencies via pip          |
| **Test**           | Runs 3 unit tests using `unittest`     |
| **Containerize**   | Builds Docker image with Flask app     |
| **Run Container**  | Starts Docker container                |
| **Show Status**    | Lists running containers (`docker ps`) |
| **Stop Container** | Stops the running container            |

---

## ✅ Test Cases Summary
Located in `app/test_app.py`, these tests include:
- ✅ Home route status code
- ✅ Home route response content
- ✅ Invalid route 404 response

---

## 📷 Screenshots (Required for Submission)
- ✅ Pipeline Success
- ✅ Test Logs
- ✅ Container Running
- ✅ Container Stopped
- ✅ Pull Request with Reviewer

---

## 📎 Author Notes
> This assignment demonstrates a full CI/CD setup using GitHub Actions, Docker, and a minimal Flask application. All tests, builds, and deployment steps are automated and verified inside the workflow logs.

---
