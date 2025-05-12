# Sentiment Analysis API

## Overview

The Sentiment Analysis API is a FastAPI-based microservice that analyzes the sentiment of text input, classifying it as **positive**, **negative**, or **neutral**. It uses the `TextBlob` library for sentiment analysis and is structured using the **Cookiecutter Data Science (CCDS) v2.6.0** template, with **pytest** for testing, **ruff** for linting, and **Docker** for containerization.

## Features

- **Endpoint**: `POST /api/v1/sentiment` accepts JSON input (e.g., `{"text": "I love this product!"}`) and returns the text and its sentiment (e.g., `{"text": "I love this product!", "sentiment": "positive"}`).
- **Testing**: Includes pytest tests with 90%+ code coverage.
- **CI/CD**: GitHub Actions workflow for linting, testing, and Docker build.
- **Containerization**: Docker support for easy deployment.
