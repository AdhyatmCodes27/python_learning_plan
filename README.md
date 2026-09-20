# Python API Utility

A reusable Python API client built using Python. This project demonstrates API communication, JSON processing, exception handling, logging, modular code, virtual environments, dependency management, and Git.

## Features

- GET, POST, PUT, PATCH, and DELETE HTTP requests
- Query parameter support
- Custom HTTP headers
- Configurable request timeout
- Centralized API request handling
- HTTP error handling
- Connection error handling
- Timeout handling
- JSON decoding error handling
- Logging
- JSON file reading and writing
- Reusable Python package structure

## Project Structure

```text
api_utility/
├── api_utility/
│   ├── __init__.py
│   ├── client.py
│   └── logger.py
│
├── data/
│   ├── users.json
│   └── summary.json
│
├── api_demo.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3
- Requests

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/AdhyatmCodes27/python_learning_plan
cd api_utility
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

#### macOS/Linux

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### JSON Processing

Run:

```bash
python main.py
```

This loads user data from `data/users.json`, processes the data, and creates `data/summary.json`.

### API Client Demonstration

Run:

```bash
python api_demo.py
```

The API demonstration covers:

- GET requests
- GET requests with query parameters
- GET requests with custom headers
- POST requests
- PUT requests
- PATCH requests
- DELETE requests

The API examples use JSONPlaceholder and httpbin as public testing APIs.

## APIClient

The reusable `APIClient` class provides a simple interface for making HTTP requests.

Example:

```python
from api_utility.client import APIClient

client = APIClient(timeout=10)

users = client.get(
    "https://jsonplaceholder.typicode.com/users"
)
```

The client centralizes common request handling such as:

- Logging
- Request timeouts
- HTTP error handling
- Connection error handling
- JSON response handling

## Supported HTTP Methods

| Method | Purpose |
|---|---|
| GET | Retrieve resources |
| POST | Create a resource |
| PUT | Replace or update a resource |
| PATCH | Partially update a resource |
| DELETE | Delete a resource |

## JSON Processing

The project also demonstrates reading and writing JSON data using Python's built-in `json` module.

Example:

```python
with open("data/users.json", "r") as f:
    users = json.load(f)
```

The project creates a summary from the user data and writes it to:

```text
data/summary.json
```

## Exception Handling

The API client handles common request-related exceptions including:

- HTTP errors
- Connection errors
- Request timeouts
- Invalid JSON responses

File processing also handles:

- Missing files
- Invalid JSON files

Exceptions are logged and re-raised so that errors are not silently ignored.

## Logging

The project uses Python's built-in `logging` module through a reusable logger configuration in `api_utility/logger.py`.

Example log output:

```text
2026-09-20 20:18:30,948 - api_utility.client - INFO -
Sending POST request to https://jsonplaceholder.typicode.com/users
```

## Virtual Environment

The project uses a Python virtual environment to isolate project dependencies.

The `.venv` directory is excluded from Git using `.gitignore`.

## Git

The project is maintained using Git with incremental commits to demonstrate good version-control practices.

## Technologies

- Python
- Requests
- JSON
- Logging
- Git
- Virtual environments

## Learning Objectives

This project was built to practice:

- Python modules and packages
- Object-oriented programming
- Clean code principles
- Exception handling
- Logging
- JSON and file handling
- REST API communication
- Reusable utility design
- Virtual environments
- Dependency management
- Git and GitHub workflow