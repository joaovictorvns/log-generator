"""Blueprint for the home page of the application.

This module defines a Flask Blueprint (`home_blueprint`) that handles the
root endpoint (`/`). It renders the home page using the `home.html` template.

Attributes:
    home_blueprint (flask.Blueprint): A Flask Blueprint for routing to the home
    page.

Functions:
    home: Renders the home page template.
"""

from flask import Blueprint, render_template

home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    """Renders the home page template.

    This function handles GET requests to the root URL (`/`) of the
    application. It renders the `home.html` template, which is expected to
    provide the content displayed to the user when they access the home page.

    Returns:
        flask.Response: The rendered `home.html` template response.
    """
    return render_template('home.html')
