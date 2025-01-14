![project_logo](assets/logo.svg){ width="300" class="center" }

# Log Generator

Welcome to the **Log Generator** documentation!

This project aims to provide a simple web application to generate custom logs. Developed in Python with the Flask framework, the **Log Generator** allows you to explore the generation of structured logs efficiently and flexibly.

## Objective

The main objective of this project is to demonstrate how a Flask application can generate detailed and custom logs, facilitating the analysis, visualization, and monitoring of data in modern observability tools.

## Features

- Log registration through RESTful API and Web Page
- Support for multiple log levels
- Addition of extra fields in JSON format
- Compatibility with observability tools like Elastic Stack (ELK) and Grafana (with Loki)
- Detailed log structure including log level, timestamp, message, context, and custom extra fields
- Daily log file rotation, keeping up to 7 log files in backup

## Technologies Used

This project was developed using the following technologies:

- **[Python](https://www.python.org/):** The main language used for project development.
- **[Flask](https://flask.palletsprojects.com/en/stable/):** Python web framework.
- **[PyTest](https://docs.pytest.org/en/stable/):** Python testing framework.
- **[Gunicorn](https://gunicorn.org/):** WSGI server for Python applications.
- **[Nginx](https://nginx.org/):** Web server used as a reverse proxy for Flask.
- **[Selenium](https://www.selenium.dev/):** Library for web interface test automation.
- **[Dynaconf](https://www.dynaconf.com/):** Configuration management library.
- **[Poetry](https://python-poetry.org/):** Tool for dependency management and packaging of Python projects.
- **[Docker](https://www.docker.com/):** Containerization platform.
- **[Mypy](https://mypy-lang.org/):** Python static type checker.
- **Linters:** [Flake8](https://flake8.pycqa.org/en/latest/), [Pylint](https://www.pylint.org/) and [Ruff](https://docs.astral.sh/ruff/).
- **Code Formatters:** [isort](https://pycqa.github.io/isort/) and [Ruff](https://docs.astral.sh/ruff/).
- **[Taskipy](https://github.com/taskipy/taskipy):** Used to manage custom tasks directly from `pyproject.toml`.
- **Other technologies:** [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) and [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), in addition to [CodeMirror](https://codemirror.net/) (a JavaScript library that provides a web component to create code editors in the browser).

## Ways to Generate Logs

#### RESTful API:

<video width="500" height="360" class="center" autoplay loop muted playsinline>
  <source src="assets/restful_api.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

#### Web Page:

<video width="800" height="360" class="center" autoplay loop muted playsinline>
  <source src="assets/web_page.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Getting Started

To start using **Log Generator**, follow the [installation](installation.md) and [configuration](configuration.md) instructions available in the documentation.

Explore the **Log Generator** documentation to learn how to register logs through the [RESTful API](how_to_use/restful_api.md) and [Web Page](how_to_use/web_page.md).
