# Scenic Server Python Project Setup

## Overview

The project is based on FastAPI and is deployed on a server.


## Activate Virtual Environment

```
source .venv/bin/activate
which python
```

## Run the Project

To run the application in development mode, you can use:

```
fastapi dev main.py
```
The fastapi dev main.py command is a feature introduced in recent FastAPI, providing a convenient way to run your FastAPI application in development mode. This command is part of the FastAPI CLI, which simplifies the process of starting a development server.

Or

```
uvicorn main:app --reload
```

uvicorn main:app --reload
Start a FastAPI application using the Uvicorn server.
Components:
uvicorn: This is the command to start the Uvicorn server.
main:app: This specifies the module (main.py) and the FastAPI application instance (app) to run.
--reload: This flag enables auto-reloading, which means the server will automatically restart when you make changes to your code. This is particularly useful during development for testing changes quickly.

Or plainly:
```
python main.py
```

## Run Tests

```
pytest
```

## Lint the code

```
black src tests
```


To set up a pre-commit hook that runs black, create a file named .git/hooks/pre-commit with the following content:

```
#!/bin/sh
black src tests
if [ $? -ne 0 ]; then
    echo "Code formatting failed. Please fix the issues before committing."
    exit 1
fi 
```

Make the script executable:

```
chmod +x .git/hooks/pre-commit
```

## Type Checking with mypy:
mypy is a static type checker for Python. It helps catch type-related errors before runtime by checking code against type annotations.

```
mypy src
```

## Security Checks with bandit:
bandit is a tool designed to find common security issues in Python code.

```
bandit -r src
```

## Code Coverage with coverage.py:

Measure how much of the code is covered by tests. This helps identify untested parts of the codebase.

```
coverage report
```

## Generate Documentation with Sphinx:
```
pip install sphinx
sphinx-quickstart docs
```

## Generate Requirements.txt


```pip install pipreqs```
```pip freeze > requirements.txt```



### pip freeze vs pipreqs

- **pip freeze**: Includes all packages in your environment, even those not used by your project. It's useful for replicating your exact environment but may include unnecessary dependencies.
- **pipreqs**: Generates a more focused `requirements.txt` file based on your project's actual imports. It's ideal for sharing your project with others, ensuring they only install what is needed.

## Docker Instructions

### Build Docker Image

```bash
docker build -t scenic-road-app .
```

### Run Docker Container

```bash
docker run --env-file .env -p 80:80 scenic-road-app
```

### Using Docker Compose

To run the application using Docker Compose, ensure your `docker-compose.yml` is set up correctly and then use:

```bash
docker-compose up
```