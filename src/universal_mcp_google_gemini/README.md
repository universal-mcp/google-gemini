**Universal MCP Google-gemini API**.

An MCP Server for the Universal Mcp Google-Gemini API.

---
## 📋 Prerequisites
Before you begin, ensure you have met the following requirements:
*   **Python 3.11+** (Recommended)
*   **[uv](https://github.com/astral-sh/uv)** installed globally (`pip install uv`)
---
## 🛠️ Setup Instructions
Follow these steps to get the development environment up and running:
### 1. Sync Project Dependencies
Navigate to the project root directory (where `pyproject.toml` is located).
```bash
uv sync
```
This command uses `uv` to install all dependencies listed in `pyproject.toml` into a virtual environment (`.venv`) located in the project root.
### 2. Activate the Virtual Environment
Activating the virtual environment ensures that you are using the project's specific dependencies and Python interpreter.
- On **Linux/macOS**:
```bash
source .venv/bin/activate
```
- On **Windows**:
```bash
.venv\\Scripts\\activate
```
### 3. Start the MCP Inspector
Use the MCP CLI to start the application in development mode.
```bash
mcp dev src/universal_mcp_google_gemini/mcp.py
```
The MCP inspector should now be running. Check the console output for the exact address and port.

## 🔌 Supported Integrations

- AgentR
- API Key (Coming Soon)
- OAuth (Coming Soon)

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Universal Mcp Google Gemini API.

| Tool | Description |
|------|-------------|
| `fetch_model` | Retrieves details of a specific model from an endpoint. |
| `fetch_models` | Fetches a paginated list of models from the API endpoint. |
| `text_only_input` | Generates text using the Gemini API with text-only input by constructing and sending a POST request. |
| `generate_atext_stream` | Generates a text stream using a rest API, supporting partial results for faster interactions. |
| `resumable_upload_request` | Initiates a resumable file upload process by sending a POST request with the file data. |
| `upload_image_file` | Uploads an image file using a POST request. |
| `futuristic_bear` | Submits a POST request with the provided request body to a predefined URL and returns the JSON response. |
| `prompt_document` | Sends a prompt request to Gemini for document analysis with provided contents. |
| `text_tokens` | Count and retrieve text tokens from given contents. |
| `fetch_tuned_models` | Fetches tuned models by querying a predefined endpoint. |
| `create_atuned_model` | Creates a tuned model by sending a request with the specified base model, display name, and tuning task. |
| `prompt_the_tuned_model` | Sends a prompt request to the tuned AI model and returns its response after verifying HTTP success status. |
| `delete_tuned_model` | Deletes a tuned model by sending a DELETE request to the specified endpoint. |
| `generate_embeddings` | Generates embeddings for input content using a specified model by sending a POST request to the API. |
| `batch_embeddings` | Generates and retrieves batch embeddings by sending a POST request with the provided requests. |
| `discovery_document` | Fetches the Geminis discovery document. |

## 📁 Project Structure
The generated project has a standard layout:
```
.
├── src/                  # Source code directory
│   └── universal_mcp_google_gemini/
│       ├── __init__.py
│       └──   mcp.py      # Server is launched here
│       └──   app.py      # Application tools are defined here
├── tests/                # Directory for project tests
├── .env                  # Environment variables (for local development)
├── pyproject.toml        # Project dependencies managed by uv
├── README.md             # This file
```
---
## ➡️ Next Steps
---
## 📄 License
---
_This project was generated using **MCP CLI** — Happy coding! 🚀_
