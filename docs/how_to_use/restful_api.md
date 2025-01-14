# RESTful API

The Log Generator RESTful API allows you to register logs with custom levels and view the current log level. This guide covers the details of how to interact with the API endpoints.

The RESTful API endpoint is (`/api`).

## HTTP Methods

### 1. `GET /api` - Get information about the current log level

Returns the name and the corresponding number of the configured log level.

**Request Example:**

```bash
curl -X GET http://127.0.0.1:5000/api
```

**Response Example:**

```json
{
  "log_level_name": "debug",
  "log_level_number": 1
}
```

### 2. `POST /api` - Register a log message

Allows you to register a message at the specified log level. The request must be made with a JSON body containing the following fields:

**Parameters:**

- **`level` (required):** The log level. Accepted values: `debug`, `info`, `warning`, `error`, and `critical`.
- **`message` (required):** The log message (string).
- **`extra` (optional):** A JSON object containing custom fields.

#### 2.1 - Success

**Request Example:**

```bash
curl -X POST http://127.0.0.1:5000/api \
-H "Content-Type: application/json" \
-d '{
  "level": "info",
  "message": "User logged in to the system",
  "extra": {
    "user_id": 42,
    "role": "admin"
  }
}'
```

**Response Example:**

```json
{
  "message": "success",
  "success": "Log registered successfully"
}
```

#### 2.2 - Error

**Request Example:**

```bash
curl -X POST http://127.0.0.1:5000/api \
-H "Content-Type: application/json" \
-d '{
  "message": "User logged in to the system",
  "extra": {
    "user_id": 42,
    "role": "admin"
  }
}'
```

**Response Example:**

```json
{
  "error": "The \"level\" field is required",
  "message": "error"
}
```
