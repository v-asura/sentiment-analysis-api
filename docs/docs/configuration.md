# Configuration

## Environment Variables

- Default settings are in `sentiment_analysis_api/core/config.py`:
  ```python
  APP_NAME = "Sentiment Analysis API"
  DEBUG = False
  PORT = 8000
  LOG_LEVEL = "INFO"
  ```
- Create a `.env` file to override:
  ```bash
  echo "PORT=8080" > .env
  ```

## Dependencies

- Managed in `requirements.txt`:
  - `fastapi==0.115.0`
  - `textblob==0.18.0.post0`
  - `pytest==8.3.3`
  - `ruff==0.6.8`

## Linting

Run linting with:

```bash
ruff check sentiment_analysis_api/
```

!!! warning "Warning"
Ensure all dependencies are installed before linting.
