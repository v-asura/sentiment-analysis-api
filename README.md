Sentiment Analysis API 🎉

📖 Overview
The Sentiment Analysis API is a modern, lightweight microservice built with FastAPI that analyzes text sentiment, classifying it as positive 😊, negative 😔, or neutral 😐. Powered by the TextBlob library, it’s structured using the Cookiecutter Data Science (CCDS) v2.6.0 template, with pytest for robust testing, ruff for code quality, and Docker for seamless deployment.

✨ Features

🚀 API Endpoint: POST /api/v1/sentiment processes JSON input (e.g., {"text": "I love this product!"}) and returns sentiment (e.g., {"text": "I love this product!", "sentiment": "positive"}).
🧪 Testing: Comprehensive pytest suite with 90%+ code coverage.
🔄 CI/CD: Automated GitHub Actions workflow for linting, testing, and Docker builds.
🐳 Containerization: Docker support for easy, portable deployment.
📝 Documentation: Elegant MkDocs-based docs, previewable locally.

🛠 Prerequisites
Before you begin, ensure you have:

Python 3.11 🐍
Git 📂 (to clone the repository)
Virtualenv 🧑‍💻 (for dependency management)
Docker 🐳 (optional, for containerized deployment)

🚀 Quick Start

1. Clone the Repository
   git clone https://github.com/v-asura/sentiment-analysis-api.git
   cd sentiment-analysis-api

2. Run Locally 🖥️

Set Up a Virtual Environment:
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt

Launch the API:
uvicorn sentiment_analysis_api.main:app --host 0.0.0.0 --port 8000 --reload

Access the API:

Visit http://localhost:8000/docs for the interactive Swagger UI.
Test the POST /api/v1/sentiment endpoint:{"text": "This is a fact."}

Expected Response:{"text": "This is a fact.", "sentiment": "neutral"}

Run Tests:
python -m pytest sentiment_analysis_api/tests/ --cov=sentiment_analysis_api

3. Run with Docker 🐳

Build the Docker Image:
docker build -t sentiment-api .

Run the Container:
docker run -p 8000:8000 sentiment-api

Access the API:

Open http://localhost:8000/docs and test as above.

Stop the Container:
docker ps -q | xargs docker stop

4. Preview Documentation with MkDocs 📚

Install MkDocs (if not already in requirements.txt):
pip install mkdocs==1.6.1 mkdocs-material==10.0.0

Run MkDocs Server:
mkdocs serve

Open http://127.0.0.1:8000 to preview the docs.
If port 8000 is in use, try:mkdocs serve --dev-addr=127.0.0.1:8001

Stop the Server:

Press Ctrl+C in the terminal.

⚙️ Configuration

Environment Variables 🌍:

The API uses a .env file for settings. Defaults are in sentiment_analysis_api/core/config.py:APP_NAME = "Sentiment Analysis API"
DEBUG = False
PORT = 8000
LOG_LEVEL = "INFO"

Override defaults by creating a .env file:echo "PORT=8080" > .env

Key Dependencies 📦:

fastapi==0.115.0
textblob==0.18.0.post0
pytest==8.3.3
ruff==0.6.8
mkdocs==1.6.1
mkdocs-material==10.0.0

Linting 🧹:
ruff check sentiment_analysis_api/

CI/CD 🔄:

GitHub Actions (.github/workflows/ci.yml) automates linting, testing, and Docker builds.

📽️ Screen Recording
Watch a short demo of the API, tests, CI workflow, and MkDocs documentation:

Insert Link Here (Replace with the actual link after uploading)

🛠️ Development Notes

Project Structure 🗂️:

Follows CCDS v2.6.0:
sentiment_analysis_api/: Core code
tests/: Pytest suite
docs/: MkDocs documentation
data/: Datasets (if any)

Testing 🧪:

Tests in sentiment_analysis_api/tests/test_routes.py cover positive, negative, and neutral sentiments.

Troubleshooting 🔍:

Verify Python 3.11: python --version
Check httpx==0.27.2: pip show httpx
Test Docker: docker run hello-world
MkDocs port conflict: Use mkdocs serve --dev-addr=127.0.0.1:8001

📜 License
MIT License. See LICENSE for details.

Built with ❤️ by v-asura
