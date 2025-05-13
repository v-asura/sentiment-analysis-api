# Setup Guide

## Local Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/v-asura/sentiment-analysis-api.git
   cd sentiment-analysis-api
   ```
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the API:
   ```bash
   uvicorn sentiment_analysis_api.main:app --host 0.0.0.0 --port 8000 --reload
   ```

## Docker Installation

1. Build the Docker image:
   ```bash
   docker build -t sentiment-api .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 sentiment-api
   ```
3. Stop the container:
   ```bash
   docker ps -q | xargs docker stop
   ```

!!! tip "Tip"
Access the API at [http://localhost:8000/docs](http://localhost:8000/docs) for testing.
