# Environment Variables

## Flask Variables

- **`FLASK_APP`:** Defines the main module of the Flask application. Expected value: the name of the module or Python file that contains the Flask application. The default value is `app`.
- **`FLASK_DEBUG`:** Enables (`True`) or disables (`False`) debug mode. When `True`, it enables automatic server reloading and detailed error information. The default value is `False`.

## Log Generator Specific Variables

- **`FLASK_LOG_PATH`:** Directory to store log files. The default value is `./log`.
- **`FLASK_LOG_LEVEL`:** Defines the log detail level. Supported values:
    - **`DEBUG`:** Maximum details (default value).
    - **`INFO`:** Informative messages.
    - **`WARNING`, `ERROR`, `CRITICAL`:** Alerts and errors in order of severity.
- **`FLASK_LOG_HEADERS`:** Enables (`True`) or disables (`False`) logging of HTTP headers. The default value is `True`.

## Selenium Variables

The variables below control the behavior of Selenium in the project, but are not native to the Selenium framework.

- **`FLASK_SELENIUM_BROWSERS`:** Defines the list of browsers for running automated tests. The variable should receive a comma-separated list. The default value is `chrome,firefox,edge`.
    - **Supported browsers:** `chrome`, `firefox`, and `edge`.

    !!! info "Note"
        It is necessary to have the corresponding browsers installed to run the tests.

- **`FLASK_SELENIUM_HEADLESS`:** Enables (`True`) or disables (`False`) the "headless" mode (without graphical interface) of Selenium in tests. The default value is `True`. Variáveis de Ambiente
