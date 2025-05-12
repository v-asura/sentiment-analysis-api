# Sentiment Analysis API

A FastAPI-based microservice for analyzing text sentiment (positive, negative, neutral) using TextBlob. Built with Cookiecutter Data Science v2.6.0, 12-Factor App principles, Docker, and GitHub Actions for CI. Uses pytest for testing and ruff for linting/formatting.

## Features

- POST `/api/v1/sentiment` to analyze text sentiment
- Configurable via environment variables
- Containerized with Docker
- Tested with pytest and pytest-cov
- Linted and formatted with ruff
- CI pipeline with GitHub Actions

## Prerequisites

- Python 3.11
- Docker (optional, for containerized setup)
- Git

## Setup and Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/v-asura/sentiment-analysis-api.git
   cd sentiment-analysis-api
   ```
