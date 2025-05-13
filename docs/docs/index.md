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
