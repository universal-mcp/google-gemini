# Universal Mcp Google Gemini MCP Server

An MCP Server for the Universal Mcp Google Gemini API.

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.11+ (Recommended)
* [uv](https://github.com/astral-sh/uv) installed globally (`pip install uv`)

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
mcp dev src/universal mcp google gemini/mcp.py
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
| `fetch_model` | fetch model. This endpoint retrieves details of a specific model. |
| `fetch_models` | fetch models. The endpoint retrieves a list of models with the option to paginate the results. The response is a JSON object with a "models" array containing information about each model. The "nextPageToken" field may be included to facilitate pagination. |
| `text_only_input` | text-only input. The simplest way to generate text using the Gemini API is to provide the model with a single text-only input, as shown in this example. |
| `generate_atext_stream` | generate a text stream. By default, the model returns a response after completing the entire text generation process. You can achieve faster interactions by not waiting for the entire result, and instead use streaming to handle partial results. |
| `resumable_upload_request` | resumable upload request. resumable upload request |
| `upload_image_file` | upload image file. upload image file |
| `futuristic_bear` | Futuristic Bear. Futuristic Bear |
| `prompt_document` | prompt document. Prompt Gemini about the document |
| `text_tokens` | text tokens. Count text tokens |
| `fetch_tuned_models` | fetch tuned models. Get all tuned models |
| `create_atuned_model` | create a tuned model. To create a tuned model, you need to pass your [dataset](https://ai.google.dev/api/tuning#Dataset) to the model. For this example, you will tune a model to generate the next number in the sequence. For example, if the input is `1`, the model should output `2`. If the input is `one hundred`, the output should be `one hundred one`. |
| `prompt_the_tuned_model` | prompt the tuned model. Try the tuned model |
| `delete_tuned_model` | delete tuned model. Delete a tuned model |
| `generate_embeddings` | generate embeddings. generate embeddings |
| `batch_embeddings` | batch embeddings. batch embeddings |
| `discovery_document` | Discovery Document. Fetch Geminis discovery document |


## 📁 Project Structure

The generated project has a standard layout:
```
.
├── src/                  # Source code directory
│   └── universal mcp google gemini/
│       ├── __init__.py
│       └── mcp.py        # Server is launched here
│       └── app.py        # Application tools are defined here
├── tests/                # Directory for project tests
├── .env                  # Environment variables (for local development)
├── pyproject.toml        # Project dependencies managed by uv
├── README.md             # This file
```

## 📝 License

This project is licensed under the MIT License.

---

_This project was generated using **MCP CLI** — Happy coding! 🚀_

## Usage

- Login to AgentR
- Follow the quickstart guide to setup MCP Server for your client
- Visit Apps Store and enable the Universal Mcp Google Gemini app
- Restart the MCP Server

### Local Development

- Follow the README to test with the local MCP Server 