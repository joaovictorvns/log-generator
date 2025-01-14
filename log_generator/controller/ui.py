"""Blueprint for the UI page of the application.

This module defines a Flask Blueprint (`ui_blueprint`) that handles the
root endpoint (`/`). It renders the UI page using the `ui.html` template.

Attributes:
    ui_blueprint (flask.Blueprint): A Flask Blueprint for routing to the UI
        page.

Functions:
    ui_route: Renders the UI page template.
"""

from flask import Blueprint, render_template

ui_blueprint = Blueprint('ui', __name__)


@ui_blueprint.route('/', methods=['GET'])
def ui_route():
    """Renders the UI page template.

    This function handles GET requests to the root URL (`/`) of the
    application. It renders the `ui.html` template, which is expected to
    provide the content displayed to the user when they access the UI page.
    """
    return render_template('ui.html')
