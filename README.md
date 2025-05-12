Sentiment Analysis API
Overview
The Sentiment Analysis API is a FastAPI-based microservice that analyzes the sentiment of text input, classifying it as positive, negative, or neutral. It uses the TextBlob library for sentiment analysis and is structured using the Cookiecutter Data Science (CCDS) v2.6.0 template, with pytest for testing, ruff for linting, and Docker for containerization.
Features

Endpoint: POST /api/v1/sentiment accepts JSON input (e.g., {"text": "I love this product!"}) and returns the text and its sentiment (e.g., {"text": "I love this product!", "sentiment": "positive"}).
Testing: Includes pytest tests with 90%+ code coverage.
CI/CD: GitHub Actions workflow for linting, testing, and Docker build.
Containerization: Docker support for easy deployment.

Prerequisites

Python: 3.11
Docker: (Optional) For running the app in a container
Git: For cloning the repository
Virtualenv: For managing Python dependencies

Setup Instructions
Clone the Repository
git clone https://github.com/v-asura/sentiment-analysis-api.git
cd sentiment-analysis-api

Option 1: Run Locally

Create and Activate a Virtual Environment:
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt

Run the Application:
uvicorn sentiment_analysis_api.main:app --host 0.0.0.0 --port 8000 --reload

Access the API:

Open http://localhost:8000/docs in a browser to use the Swagger UI.
Test the POST /api/v1/sentiment endpoint with:{"text": "This is a fact."}

Expected response:{"text": "This is a fact.", "sentiment": "neutral"}

Run Tests:
python -m pytest sentiment_analysis_api/tests/ --cov=sentiment_analysis_api

Option 2: Run with Docker

Build the Docker Image:
docker build -t sentiment-api .

Run the Container:
docker run -p 8000:8000 sentiment-api

Access the API:

Open http://localhost:8000/docs and test the endpoint as above.

Stop the Container:
docker ps -q | xargs docker stop

Configuration Notes

Environment Variables: The app uses a .env file for configuration (e.g., PORT, DEBUG). Default settings are in sentiment_analysis_api/core/config.py:
APP_NAME = "Sentiment Analysis API"
DEBUG = False
PORT = 8000
LOG_LEVEL = "INFO"

Create a .env file to override defaults if needed:
echo "PORT=8080" > .env

Dependencies: Managed via requirements.txt. Key libraries:

fastapi==0.115.0
textblob==0.18.0.post0
pytest==8.3.3
ruff==0.6.8

Linting: Run ruff check sentiment_analysis_api/ to ensure code quality.

CI: The GitHub Actions workflow (.github/workflows/ci.yml) runs linting, tests, and Docker build on push/pull requests.

Screen Recording
A short video demonstrating the app, tests, and CI workflow is available at:

Insert Link Here (Replace with the actual link after uploading)

Development Notes

Project Structure: Follows CCDS v2.6.0 with sentiment_analysis_api/ for code, tests/ for pytest, and data/ for datasets.
Testing: Tests in sentiment_analysis_api/tests/test_routes.py cover positive, negative, and neutral sentiments.
Troubleshooting:
Ensure Python 3.11 is installed (python --version).
If tests fail, verify httpx==0.27.2 is installed (pip show httpx).
For Docker issues, test with docker run hello-world.

License
MIT License. See LICENSE for details.
