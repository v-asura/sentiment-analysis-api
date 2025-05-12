# Configuration Notes

- **Environment Variables**: The app uses a `.env` file for configuration (e.g., `PORT`, `DEBUG`). Default settings are in `sentiment_analysis_api/core/config.py`:
  ```python
  APP_NAME = "Sentiment Analysis API"
  DEBUG = False
  PORT = 8000
  LOG_LEVEL = "INFO"
  ```
