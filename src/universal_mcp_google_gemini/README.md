# Google-Gemini MCP Server

An MCP Server for the Google-Gemini API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Google-Gemini API.

| Tool                       | Description                                                                                                                                                                          |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `fetch_model`              | Retrieves the configuration details for the Gemini 1.5 Flash-8B model via a GET request.                                                                                             |
| `fetch_models`             | Retrieves a paginated list of available models, supporting page size and token parameters for result navigation.                                                                     |
| `text_only_input`          | Generates content using the Gemini 1.5 Flash model via POST request with optional query parameters.                                                                                  |
| `generate_atext_stream`    | Generates a streaming response from the Gemini 1.5 Flash model for multimodal input content.                                                                                         |
| `resumable_upload_request` | Uploads a file to storage using the POST method, with headers specifying upload protocol, command, content length, and content type.                                                 |
| `prompt_document`          | Generates content using the Gemini model, accepting input prompts and returning a streamed response across various media types, such as text, images, and audio.                     |
| `text_tokens`              | Calculates the number of tokens and billable characters for input content when using the Gemini 1.5 Flash 8B model.                                                                  |
| `fetch_tuned_models`       | Retrieves a list of tuned models at the specified page size using the GET method.                                                                                                    |
| `create_atuned_model`      | Creates a tuned model using the "POST" method at the "/v1beta/tunedModels" endpoint and returns a response upon successful creation.                                                 |
| `prompt_the_tuned_model`   | Generates content using a specified tuned model defined at path "/v1beta/{tunedModel}:generateContent" by sending a POST request.                                                    |
| `delete_tuned_model`       | Deletes a specified tuned model and returns a success status upon removal.                                                                                                           |
| `generate_embeddings`      | Generates a text embedding vector from input text using the specified Gemini Embedding model, allowing for semantic analysis and comparison of textual content.                      |
| `batch_embeddings`         | Generates batch embeddings for a list of text inputs using the "text-embedding-004" model via a POST request to the "/v1beta/models/text-embedding-004:batchEmbedContents" endpoint. |
| `discovery_document`       | Retrieves discovery metadata for REST APIs, including available endpoints and parameters, based on the specified version.                                                            |
