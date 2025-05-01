from typing import Any, Annotated, Optional
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration
import requests

class GeminiApiApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='geminiapiapp', integration=integration, **kwargs)
        self.base_url = "https://generativelanguage.googleapis.com"

    def fetch_model(self, ) -> dict[str, Any]:
        """
        Fetches information about a specific generative model (gemini-1.5-flash-8b-exp-0827) by sending a GET request to the API.
        
        Returns:
            Dictionary containing information about the fetched model, derived from the API's JSON response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (4xx/5xx status codes).
        
        Tags:
            fetch, model, get-request, important
        """
        path = "/v1beta/models/gemini-1.5-flash-8b-exp-0827"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def fetch_models(self, pageSize: Annotated[Optional[int], ''] = None, pageToken: Annotated[Optional[str], ''] = None) -> dict[str, Any]:
        """
        Fetches a list of available generative models by sending a GET request to the API.
        
        Args:
            pageSize: The maximum number of models to return in a single page. Optional, defaults to None.
            pageToken: A token received from a previous `fetch_models` call to retrieve the next page. Optional, defaults to None.
        
        Returns:
            Dictionary containing a list of models and pagination information, derived from the API's JSON response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (4xx/5xx status codes).
        
        Tags:
            fetch, models, list, get-request, important, management
        """
        path = "/v1beta/models"
        url = f"{self.base_url}{path}"
        query_params = {
                "pageSize": pageSize,
                "pageToken": pageToken,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def text_only_input(self, contents: Annotated[list[Any], ''] = None, generationConfig: Annotated[Optional[dict[str, Any]], ''] = None, key: Annotated[Optional[str], ''] = None, safetySettings: Annotated[Optional[list[Any]], ''] = None) -> dict[str, Any]:
        """
        Generates text content from input using a specific model (gemini-1.5-flash-8b-exp-0827) via a POST request.
        
        Args:
            contents: A list of content parts (e.g., text, inline_data) to send as input to the model. Optional, defaults to None.
            generationConfig: Configuration for text generation parameters (e.g., temperature, max output tokens). Optional, defaults to None.
            key: API key for authentication. Optional, defaults to None.
            safetySettings: Settings for safety filtering of the generated content. Optional, defaults to None.
        
        Returns:
            Dictionary containing the generated content and potentially other response details, derived from the API's JSON response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (4xx/5xx status codes).
        
        Tags:
            generate, text, model, post-request, important
        """
        request_body = {
            "contents": contents,
            "generationConfig": generationConfig,
            "safetySettings": safetySettings,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = "/v1beta/models/gemini-1.5-flash-8b-exp-0827:generateContent"
        url = f"{self.base_url}{path}"
        query_params = {
                "key": key,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def generate_atext_stream(self, contents: Annotated[list[Any], ''] = None, generationConfig: Annotated[Optional[dict[str, Any]], ''] = None, safetySettings: Annotated[Optional[list[Any]], ''] = None, alt: Annotated[str, ''] = "sse") -> requests.Response:
        """
        Streams text content generation from input using a specific model (gemini-1.5-flash-8b-exp-0827) via a POST request.
        
        Args:
            contents: A list of content parts (e.g., text, inline_data) to send as input to the model. Optional, defaults to None.
            generationConfig: Configuration for text generation parameters (e.g., temperature, max output tokens). Optional, defaults to None.
            safetySettings: Settings for safety filtering of the generated content. Optional, defaults to None.
            alt: Specifies the response format, typically "sse" for Server-Sent Events. Defaults to "sse".
        
        Returns:
            A `requests.Response` object with `stream=True`, allowing the caller to iterate over chunks of the streamed response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (4xx/5xx status codes).
        
        Tags:
            generate, text, stream, model, post-request, important
        """
        request_body = {
            "contents": contents,
            "generationConfig": generationConfig,
            "safetySettings": safetySettings,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = "/v1beta/models/gemini-1.5-flash-8b-exp-0827:streamGenerateContent"
        url = f"{self.base_url}{path}"
        query_params = {
                "alt": alt,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, json=request_body, params=query_params, stream=True)
        response.raise_for_status()
        return response

    def resumable_upload_request(self, display_name: Annotated[str, ''], content_length: Annotated[int, ''], content_type: Annotated[str, '']) -> dict[str, Any]:
        """
        Initiates a resumable file upload request by sending a POST request with upload metadata.
        
        Args:
            display_name: The desired display name for the file being uploaded.
            content_length: The total size (in bytes) of the file content to be uploaded.
            content_type: The MIME type of the file content.
        
        Returns:
            Dictionary containing information needed for the subsequent upload steps, including the upload URL, derived from the API's JSON response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (4xx/5xx status codes).
        
        Tags:
            upload, file, resumable, post-request, important
        """
        path = "/upload/v1beta/files"
        url = f"{self.base_url}{path}"
        request_body = {
            "file": {
                "display_name": display_name
            }
        }
        headers = {
            "x-goog-upload-protocol": "resumable",
            "x-goog-upload-command": "start",
            "x-goog-upload-header-content-length": str(content_length),
            "x-goog-upload-header-content-type": content_type
        }
        query_params = {}
        response = self._post(url, json=request_body, params=query_params, headers=headers)
        response.raise_for_status()
        return response.json()

    def upload_image_file(self, upload_url: Annotated[str, ''], file_data: Annotated[bytes, ''], content_type: Annotated[str, ''], offset: Annotated[int, ''] = 0) -> dict[str, Any]:
        """
        Uploads a chunk of file data as part of a resumable upload process using a POST request.
        
        Args:
            upload_url: The URL provided in the response from `resumable_upload_request`.
            file_data: The bytes representing the chunk of the file content to upload.
            content_type: The MIME type of the file content being uploaded.
            offset: The starting byte offset within the total file content for the current chunk. Defaults to 0.
        
        Returns:
            Dictionary containing the status of the upload chunk, derived from the API's JSON response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (4xx/5xx status codes).
        
        Tags:
            upload, file, chunk, resumable, post-request, important
        """
        url = upload_url
        content_length = len(file_data)
        headers = {
            "Content-Length": str(content_length),
            "X-Goog-Upload-Offset": str(offset),
            "X-Goog-Upload-Command": "upload, finalize",
            "Content-Type": content_type
        }
        request_body = file_data
        query_params = {}
        response = self._post(url, data=request_body, params=query_params, headers=headers)
        response.raise_for_status()
        return response.json()

    def futuristic_bear(self, instances: Annotated[list[Any], ''] = None, parameters: Annotated[Optional[dict[str, Any]], ''] = None) -> dict[str, Any]:
        """
        Sends a prediction request to the 'imagen-3.0-generate-002' model via a POST request.
        Note: The method name 'futuristic_bear' is arbitrary and corresponds to the API endpoint's function.
        
        Args:
            instances: A list of instances to process for prediction. Optional, defaults to None.
            parameters: Dictionary containing prediction parameters. Optional, defaults to None.
        
        Returns:
            Dictionary containing the prediction results, derived from the API's JSON response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (4xx/5xx status codes).
        
        Tags:
            predict, image, model, post-request, important
        """
        request_body = {
            "instances": instances,
            "parameters": parameters,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = "/v1beta/models/imagen-3.0-generate-002:predict"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def prompt_document(self, contents: Annotated[list[Any], ''] = None) -> dict[str, Any]:
        """
        Generates content from input using the 'gemini-1.5-pro-latest' model via a POST request.
        
        Args:
            contents: A list of content parts (e.g., text, inline_data) to send as input to the model. Optional, defaults to None.
        
        Returns:
            Dictionary containing the generated content, derived from the API's JSON response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (4xx/5xx status codes).
        
        Tags:
            generate, text, document, model, post-request, important
        """
        request_body = {
            "contents": contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = "/v1beta/models/gemini-1.5-pro-latest:generateContent"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def text_tokens(self, contents: Annotated[list[Any], ''] = None) -> dict[str, Any]:
        """
        Counts tokens in the provided content using a specific model (gemini-1.5-flash-8b-exp-0827) via a POST request.
        
        Args:
            contents: A list of content parts (e.g., text) for which to count tokens. Optional, defaults to None.
        
        Returns:
            Dictionary containing the token count, derived from the API's JSON response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (4xx/5xx status codes).
        
        Tags:
            count, tokens, text, model, post-request, important
        """
        request_body = {
            "contents": contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = "/v1beta/models/gemini-1.5-flash-8b-exp-0827:countTokens"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def fetch_tuned_models(self, page_size: Annotated[Optional[int], ''] = None, page_token: Annotated[Optional[str], ''] = None) -> dict[str, Any]:
        """
        Fetches a list of available tuned models by sending a GET request to the API.
        
        Args:
            page_size: The maximum number of tuned models to return in a single page. Optional, defaults to None.
            page_token: A token received from a previous `fetch_tuned_models` call to retrieve the next page. Optional, defaults to None.
        
        Returns:
            Dictionary containing a list of tuned models and pagination information, derived from the API's JSON response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (4xx/5xx status codes).
        
        Tags:
            fetch, tuned-models, list, get-request, important, management
        """
        path = "/v1beta/tunedModels"
        url = f"{self.base_url}{path}"
        query_params = {
                "page_size": page_size,
                "page_token": page_token,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atuned_model(self, base_model: Annotated[str, ''], display_name: Annotated[str, ''], tuning_task: Annotated[dict[str, Any], '']) -> dict[str, Any]:
        """
        Creates a new tuned model based on a base model and tuning task configuration via a POST request.
        
        Args:
            base_model: The identifier of the base model to tune (e.g., "models/gemini-1.0-pro-001").
            display_name: A human-readable name for the new tuned model.
            tuning_task: Dictionary containing the configuration for the tuning process.
        
        Returns:
            Dictionary containing information about the newly created tuned model, derived from the API's JSON response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (4xx/5xx status codes).
        
        Tags:
            create, tuned-model, post-request, important, management
        """
        request_body = {
            "base_model": base_model,
            "display_name": display_name,
            "tuning_task": tuning_task,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = "/v1beta/tunedModels"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def prompt_the_tuned_model(self, tunedModel: Annotated[str, ''], contents: Annotated[list[Any], '']) -> dict[str, Any]:
        """
        Generates content from input using a specific tuned model via a POST request.
        
        Args:
            tunedModel: The resource name of the tuned model to use (e.g., "tunedModels/your-tuned-model-id").
            contents: A list of content parts (e.g., text) to send as input to the tuned model.
        
        Returns:
            Dictionary containing the generated content, derived from the API's JSON response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (4xx/5xx status codes).
        
        Tags:
            generate, text, tuned-model, post-request, important
        """
        request_body = {
            "contents": contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = f"/v1beta/{tunedModel}:generateContent"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tuned_model(self, tunedModel: Annotated[str, '']) -> dict[str, Any]:
        """
        Deletes a specific tuned model by sending a DELETE request.
        
        Args:
            tunedModel: The resource name of the tuned model to delete (e.g., "tunedModels/your-tuned-model-id").
        
        Returns:
            Dictionary containing the result of the delete operation (usually an empty object on success), derived from the API's JSON response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (4xx/5xx status codes).
        
        Tags:
            delete, tuned-model, delete-request, important, management
        """
        path = f"/v1beta/{tunedModel}"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def generate_embeddings(self, content: Annotated[dict[str, Any], ''] = None, model: Annotated[Optional[str], ''] = None) -> dict[str, Any]:
        """
        Generates embeddings for input content using a specified model by sending a POST request to the API.
        
        Args:
            content: Dictionary containing content to generate embeddings for. Must be a non-null dictionary with string keys.
            model: Model identifier or configuration used for embedding generation. Optional, defaults to None.
        
        Returns:
            Dictionary containing generated embeddings, derived from the API's JSON response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (4xx/5xx status codes).
        
        Tags:
            generate, embeddings, ai, post-request, important
        """
        request_body = {
            "content": content,
            "model": model,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = "/v1beta/models/text-embedding-004:embedContent"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def batch_embeddings(self, requests: Annotated[list[Any], ''] = None) -> dict[str, Any]:
        """
        Generates and retrieves batch embeddings by sending a POST request with the provided requests.
        
        Args:
            requests: A list of requests for generating embeddings. If None, the default value will be used.
        
        Returns:
            A dictionary containing the response from the server, which includes the generated embeddings.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request, such as network errors or invalid responses.
            HTTPError: Raised if the HTTP request returned an unsuccessful status code.
        
        Tags:
            embeddings, batch, important, management
        """
        request_body = {
            "requests": requests,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = "/v1beta/models/text-embedding-004:batchEmbedContents"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def discovery_document(self, version: Annotated[Any, ''] = None) -> dict[str, Any]:
        """
        Fetches the Geminis discovery document.
        
        Args:
            version: Optional version parameter for the discovery document. Defaults to None.
        
        Returns:
            A dictionary containing the discovery document data.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request to fetch the discovery document fails.
        
        Tags:
            fetch, discovery, document, important, management
        """
        path = "/$discovery/rest"
        url = f"{self.base_url}{path}"
        query_params = {
                "version": version,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            
            self.fetch_model,
            self.fetch_models,
            self.text_only_input,
            self.generate_atext_stream,
            self.resumable_upload_request,
            self.upload_image_file,
            self.futuristic_bear,
            self.prompt_document,
            self.text_tokens,
            self.fetch_tuned_models,
            self.create_atuned_model,
            self.prompt_the_tuned_model,
            self.delete_tuned_model,
            self.generate_embeddings,
            self.batch_embeddings,
            self.discovery_document
        ]