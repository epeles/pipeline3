# Selenium Python Example with GitHub Actions CI Pipeline

This repository contains a basic example of using Selenium with Python to perform automated web testing. It also includes a Continuous Integration (CI) pipeline configured with GitHub Actions to automatically run the tests.

## Project Structure

- `tests/`: Directory containing the test scripts.
  - `test_example.py`: Example test script using Selenium and pytest.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `.github/workflows/ci.yml`: GitHub Actions workflow file that defines the CI pipeline.

## Setting Up the Project

### Prerequisites

- Python 3.x
- Chrome browser installed
- ChromeDriver installed (managed by `webdriver_manager`)

### Installing Dependencies

To install the necessary dependencies, run:

```sh
pip install -r requirements.txt