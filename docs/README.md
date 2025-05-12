## Generating the docs

Use [mkdocs](http://www.mkdocs.org/) structure to update the documentation.

Build locally with:

mkdocs build

Serve locally with:
cd docs
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

Built by v-asura
