FROM python:3.13.0-slim-bookworm

WORKDIR /log-generator

COPY pyproject.toml poetry.lock ./
COPY log_generator ./log_generator

RUN pip install poetry==1.8.3
RUN poetry install --only main

CMD ["poetry", "run", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "log_generator:create_app()"]
