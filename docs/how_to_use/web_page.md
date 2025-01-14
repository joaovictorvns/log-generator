# Web Page

The Log Generator web interface provides an interactive way to view and log directly in the browser without the need to interact with the RESTful API.

The Web Page endpoint is (`/`).

## Web Interface Structure

The page has a clean and functional interface, divided into several sections:

### 1. Log Level Selection

- Located in the upper left corner.
- A dropdown menu allows you to select the desired log level. Available options: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`. The available options depend on the server configuration.

### 2. Log Message

- Located to the right of the log level selection.
- A text field where you can enter the message you want to log. Example: "User logged in to the system"

### 3. Extra Fields

- Below the main fields, there is a checkbox that enables a JSON editor.
- This editor allows you to add extra information to the log, such as contextual data or metadata.

**Example of input in the JSON editor:**

```json
{
  "level": "info",
  "message": "User logged in to the system",
  "extra": {
    "user_id": 42,
    "role": "admin"
  }
}
```

### 4. Action Buttons

- **RESET:** Clears all filled fields, allowing you to reset the form.
- **SUBMIT:** Sends the configured log to the server. After submission, the interface will display a message indicating the success or failure of the operation.

### 5. Status Messages

- Located at the bottom of the page.
- Displays feedback messages, such as:
    - *'Success: Log registered successfully'*
    - *'Error: The "extra" field must be a dict'*Web Page
