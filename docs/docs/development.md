# Development Notes

- **Project Structure**: Follows CCDS v2.6.0 with `sentiment_analysis_api/` for code, `tests/` for pytest, and `data/` for datasets.
- **Testing**: Tests in `sentiment_analysis_api/tests/test_routes.py` cover positive, negative, and neutral sentiments.
- **Troubleshooting**:
  - Ensure Python 3.11 is installed (`python --version`).
  - If tests fail, verify `httpx==0.27.2` is installed (`pip show httpx`).
  - For Docker issues, test with `docker run hello-world`.

## Screen Recording

A short video demonstrating the app, tests, and CI workflow is available at:

- [Watch Demo](#) \_(https://drive.google.com/drive/folders/1lYoIS0iB0HmYy4RHW9QI288zdy0CJ7lu?usp=share_link)

## License

MIT License. See `LICENSE` for details.
