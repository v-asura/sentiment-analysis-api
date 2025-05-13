# Sentiment Analysis API 🎉

_Elegant documentation powered by MkDocs and Material for MkDocs 🌟_

## 📖 Overview

The **Sentiment Analysis API** is a modern FastAPI microservice that analyzes text sentiment, classifying it as **positive 😊**, **negative 😔**, or **neutral 😐**. Built with `TextBlob` and structured using the **Cookiecutter Data Science (CCDS) v2.6.0** template, it features **pytest** for testing, **ruff** for linting, and **Docker** for deployment.

!!! note "Project Goal"
This project applies the 12-Factor Principles to create a functional, scalable sentiment analysis tool.

## ✨ Features

- 🚀 **API Endpoint**: `POST /api/v1/sentiment` (e.g., `{"text": "I love this product!"}` → `{"text": "I love this product!", "sentiment": "positive"}`).
- 🧪 **Testing**: Pytest with **90%+ code coverage**.
- 🔄 **CI/CD**: GitHub Actions for automated workflows.
- 🐳 **Containerization**: Docker support.
- 📝 **Documentation**: Interactive MkDocs site.

## 🛠 Prerequisites

- **Python 3.11** 🐍
- **Git** 📂
- **Virtualenv** 🧑‍💻
- **Docker** 🐳 (optional)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/v-asura/sentiment-analysis-api.git
cd sentiment-analysis-api
```

### 2. Run Locally 🖥️

=== "Local Setup" 1. **Create and Activate Virtual Environment**:
`bash
       python -m venv .venv
       source .venv/bin/activate  # On Windows: .venv\Scripts\activate
       ` 2. **Install Dependencies**:
`bash
       pip install -r requirements.txt
       ` 3. **Launch the API**:
`bash
       uvicorn sentiment_analysis_api.main:app --host 0.0.0.0 --port 8000 --reload
       ` 4. **Access the API**: - Open [http://localhost:8000/docs](http://localhost:8000/docs). - Test: `{"text": "This is a fact."}` → `{"text": "This is a fact.", "sentiment": "neutral"}`.

=== "Run Tests"
`bash
    python -m pytest sentiment_analysis_api/tests/ --cov=sentiment_analysis_api
    `

### 3. Run with Docker 🐳

1. **Build the Docker Image**:
   ```bash
   docker build -t sentiment-api .
   ```
2. **Run the Container**:
   ```bash
   docker run -p 8000:8000 sentiment-api
   ```
3. **Access the API**:
   - Open [http://localhost:8000/docs](http://localhost:8000/docs) and test as above.
4. **Stop the Container**:
   ```bash
   docker ps -q | xargs docker stop
   ```

### 4. Preview Documentation 📚

1. **Install MkDocs**:
   ```bash
   pip install mkdocs==1.6.1 mkdocs-material==10.0.0
   ```
2. **Run MkDocs Server**:
   ```bash
   mkdocs serve
   ```
   - Open [http://127.0.0.1:8000](http://127.0.0.1:8000) (use `127.0.0.1:8001` if port 8000 is in use).
   - Stop with `Ctrl+C`.

## ⚙️ Configuration

- **Environment Variables** 🌍:
  - Defaults in `sentiment_analysis_api/core/config.py`:
    ```python
    APP_NAME = "Sentiment Analysis API"
    DEBUG = False
    PORT = 8000
    LOG_LEVEL = "INFO"
    ```
  - Override in `.env`:
    ```bash
    echo "PORT=8080" > .env
    ```
- **Dependencies**: `requirements.txt` includes `fastapi==0.115.0`, `textblob==0.18.0.post0`, etc.
- **Linting** 🧹:
  ```bash
  ruff check sentiment_analysis_api/
  ```

## 📽️ Screen Recording

Watch a short demo of the API, tests, CI workflow, and MkDocs documentation:

- [Watch Demo and Screenshots](https://drive.google.com/drive/folders/1lYoIS0iB0HmYy4RHW9QI288zdy0CJ7lu?usp=share_link)

## 📸 Screenshots

Explore key components:

- [Project Structure](screenshots/project_structure.png)
- [Main API Code](screenshots/main_py.png)
- [API Routes](screenshots/routes_py.png)
- [Tests](screenshots/test_routes_py.png)
- [MkDocs Documentation](screenshots/mkdocs_home.png)
- [CI Workflow](screenshots/ci_workflow.png)

## 🛠️ Development Notes

- **Structure**: Follows CCDS v2.6.0 with `sentiment_analysis_api/`, `tests/`, and `docs/`.
- **Troubleshooting** 🔍:
  - Verify Python 3.11: `python --version`
  - Check `httpx==0.27.2`: `pip show httpx`
  - Test Docker: `docker run hello-world`

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.

---

_Built by v-asura_  
_Last Updated: May 13, 2025_
