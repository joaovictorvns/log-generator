# Log Generator Configuration

## Configuring the `.env` file

The `.env` file at the root of the project is used to define the necessary environment variables. It should follow the format below:

```env
FLASK_APP=log_generator
FLASK_DEBUG=True

FLASK_LOG_PATH=./log
FLASK_LOG_LEVEL=DEBUG
FLASK_LOG_HEADERS=True

FLASK_SELENIUM_BROWSERS=chrome,firefox,edge
FLASK_SELENIUM_HEADLESS=True
```

### Basic Explanation of Variables

- **`FLASK_APP` and `FLASK_DEBUG`:** Standard Flask settings.
- **`FLASK_LOG_*`:** Settings related to the logging system, such as directory, detail level, and HTTP headers.
- **`FLASK_SELENIUM_*`:** Controls automated tests with Selenium.

> For a detailed explanation of each variable and the accepted values, see [Environment Variables](references/env_vars.md) in the References section.

## Running the project

### With Poetry:

Use the command below to run the development server:

```bash
poetry run flask run --no-reload
```

The server will be available at: [http://127.0.0.1:5000](http://127.0.0.1:5000).

!!! warning "Note"
    Due to an incompatibility between log file rotation and Flask's auto-reload, it is **recommended to use the** `--no-reload` **flag** to avoid issues.

### With Docker:

Use the command below to run the production server in Docker:

```bash
docker compose up -d
```

The server will be available at: [http://localhost](http://localhost). Configuração do Log Generator
