"""Factory function of Log Generator (Flask Application).

This module implements a function that generates an instance of
Log Generator (Flask Application). This function registers the application's
blueprints, configures the `ProxyFix` middleware and loads the settings from
the configuration system (Dynaconf).

Functions:
    create_app: Create and configure the Flask application.
"""

from dynaconf import FlaskDynaconf, Validator  # type: ignore[import-untyped]
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from log_generator.controller.api import api_blueprint
from log_generator.controller.ui import ui_blueprint
from log_generator.logging.config import setup_logging


def create_app() -> Flask:
    """Create and configure the Flask application.

    This function initializes a new Flask application, registers the necessary
    blueprints (`ui_blueprint` and `api_blueprint`), applies the `ProxyFix`
    middleware for proper handling of proxy headers, and loads settings from
    Dynaconf. It also validates the log level configuration and sets up
    logging.

    Steps:
    1. Registers the UI and API blueprints.
    2. Configures the app with `ProxyFix` middleware for handling proxied
        requests.
    3. Loads settings from Dynaconf, validating the log level setting.
    4. Sets up logging based on the loaded configuration.

    Returns:
        flask.Flask: The configured Flask application instance.
    """
    app = Flask(__name__)

    # Register blueprints for routing
    app.register_blueprint(ui_blueprint)
    app.register_blueprint(api_blueprint)

    # Apply ProxyFix middleware to handle proxy headers
    app.wsgi_app = ProxyFix(  # type: ignore[method-assign]
        app.wsgi_app, x_for=1, x_proto=1, x_host=1
    )

    # Load settings from Dynaconf and validate configuration
    FlaskDynaconf(
        load_dotenv=True,
        app=app,
        validators=[
            Validator(
                'FLASK_LOG_LEVEL',
                default='DEBUG',
                is_in={'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'},
            ),
            Validator(
                'FLASK_LOG_HEADERS',
                default=True,
                is_type_of=bool,
            ),
            Validator(
                'FLASK_SELENIUM_BROWSERS',
                default='chrome,firefox,edge',
            ),
            Validator(
                'FLASK_SELENIUM_HEADLESS',
                default=True,
                is_type_of=bool,
            ),
        ],
    )

    setup_logging()
    return app
