from typing import Any, Annotated
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class GeminiApiApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='geminiapiapp', integration=integration, **kwargs)
        self.base_url = "https://generativelanguage.googleapis.com"


    def fetch_model(self, ) -> dict[str, Any]:
        """
        Retrieves details of a specific model from an endpoint.
        
        Args:
            None: This function does not accept any parameters.
        
        Returns:
            A dictionary containing model details.
        
        Raises:
            requests.HTTPError: Raised when an HTTP request returns an unsuccessful status code.
        
        Tags:
            fetch, models, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def fetch_models(self, pageSize: Annotated[Any, ''] = None, pageToken: Annotated[Any, ''] = None) -> dict[str, Any]:
        """
        Fetches a paginated list of models from the API endpoint.
        
        Args:
            pageSize: Maximum number of models to return in the response. A `None` value uses the API's default page size.
            pageToken: Token for pagination, retrieved from a prior response's 'nextPageToken' field. A `None` value starts from the first page.
        
        Returns:
            A dictionary containing the API response, including a 'models' array with model details and an optional 'nextPageToken' for pagination.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the API request fails (non-2xx status code).
        
        Tags:
            fetch, list, models, pagination, api, async_job, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "pageSize": pageSize,
                "pageToken": pageToken,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def text_only_input(self, contents: Annotated[list[Any], ''] = None, generationConfig: Annotated[dict[str, Any], ''] = None, key: Annotated[Any, ''] = None, safetySettings: Annotated[list[Any], ''] = None) -> dict[str, Any]:
        """
        Generates text using the Gemini API with text-only input by constructing and sending a POST request.
        
        Args:
            contents: List of input content elements for text generation (default: None)
            generationConfig: Dictionary containing configuration parameters for text generation (default: None)
            key: API key for authentication (default: None)
            safetySettings: List of safety configuration parameters to filter inappropriate content (default: None)
        
        Returns:
            Dictionary containing the JSON response from the Gemini API with generated text results
        
        Raises:
            HTTPError: If the POST request fails or returns a non-200 status code
        
        Tags:
            text-generation, api-call, async_job, ai, important
        """
        request_body = {
            "contents": contents,
            "generationConfig": generationConfig,
            "safetySettings": safetySettings,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "key": key,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def generate_atext_stream(self, alt: Annotated[Any, ''] = None, contents: Annotated[list[Any], ''] = None) -> Any:
        """
        Generates a text stream using a rest API, supporting partial results for faster interactions.
        
        Args:
            alt: Alternative representation for the response.
            contents: List of contents to be passed in the request body.
        
        Returns:
            JSON response from the API.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            generate, text-generation, stream, api-call, important
        """
        request_body = {
            "contents": contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "alt": alt,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def resumable_upload_request(self, file: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Initiates a resumable file upload process by sending a POST request with the file data.
        
        Args:
            file: A dictionary containing file data, typically including file content and metadata. Can be None for subsequent upload chunks in a resumable workflow.
        
        Returns:
            Parsed JSON response containing upload session details such as session ID, upload URL, or status information.
        
        Raises:
            HTTPError: Raised for HTTP request failures (non-2xx status codes), typically indicating network issues, authentication errors, or invalid request parameters.
        
        Tags:
            upload, resumable, async-job, file-upload, http-request, document-processing, important
        """
        request_body = {
            "file": file,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def upload_image_file(self, request_body: Annotated[Any, ''] = None) -> dict[str, Any]:
        """
        Uploads an image file using a POST request.
        
        Args:
            request_body: Optional request body, defaults to None if not provided.
        
        Returns:
            A dictionary containing the server's response.
        
        Raises:
            requests.RequestException: Raised if there's an issue with the request, such as network problems or invalid responses.
        
        Tags:
            upload, image, http-post, api-call, important
        """
        request_body = request_body
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def futuristic_bear(self, request_body: Annotated[Any, ''] = None) -> dict[str, Any]:
        """
        Submits a POST request with the provided request body to a predefined URL and returns the JSON response.
        
        Args:
            request_body: The body of the POST request; defaults to None if not provided.
        
        Returns:
            A dictionary containing the JSON response from the server.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returned an unsuccessful status code.
        
        Tags:
            post, request, json-response, important
        """
        request_body = request_body
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def prompt_document(self, contents: Annotated[list[Any], ''] = None) -> dict[str, Any]:
        """
        Sends a prompt request to Gemini for document analysis with provided contents.
        
        Args:
            contents: A list of elements constituting the document to be processed. Defaults to None, which excludes it from the request body.
        
        Returns:
            A dictionary containing the parsed JSON response from the Gemini API after processing the document.
        
        Raises:
            requests.HTTPError: Raised when the API request fails, typically due to invalid inputs or server-side errors.
        
        Tags:
            prompt, document-processing, api-request, important
        """
        request_body = {
            "contents": contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def text_tokens(self, contents: Annotated[list[Any], ''] = None) -> dict[str, Any]:
        """
        Count and retrieve text tokens from given contents.
        
        Args:
            contents: A list of any type of contents to analyze (default is None).
        
        Returns:
            A dictionary containing the text token count.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            count, text-analysis, important
        """
        request_body = {
            "contents": contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def fetch_tuned_models(self, page_size: Annotated[Any, ''] = None) -> dict[str, Any]:
        """
        Fetches tuned models by querying a predefined endpoint.
        
        Args:
            page_size: Optional page size parameter to control the number of models returned.
        
        Returns:
            A dictionary containing tuned models.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            fetch, machine-learning, model-management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "page_size": page_size,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atuned_model(self, base_model: Annotated[Any, ''] = None, display_name: Annotated[Any, ''] = None, tuning_task: Annotated[dict[str, Any], ''] = None) -> dict[str, Any]:
        """
        Creates a tuned model by sending a request with the specified base model, display name, and tuning task.
        
        Args:
            base_model: The base model used for tuning.
            display_name: The display name for the tuned model.
            tuning_task: A dictionary containing the tuning task details.
        
        Returns:
            A dictionary containing details of the created tuned model.
        
        Raises:
            requests.exceptions.HTTPError: This exception is raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            tuning, ai, important, fine-tuning
        """
        request_body = {
            "base_model": base_model,
            "display_name": display_name,
            "tuning_task": tuning_task,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def prompt_the_tuned_model(self, contents: Annotated[list[Any], ''] = None) -> dict[str, Any]:
        """
        Sends a prompt request to the tuned AI model and returns its response after verifying HTTP success status.
        
        Args:
            contents: List of content elements to send as input to the tuned model. Defaults to None (omitted if None).
        
        Returns:
            Dictionary containing the parsed JSON response from the tuned model's API endpoint.
        
        Raises:
            requests.HTTPError: Raised when the API request fails, typically due to authorization errors (4XX) or server issues (5XX).
        
        Tags:
            prompt, ai, tuned-model, async-job, important
        """
        request_body = {
            "contents": contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tuned_model(self, ) -> dict[str, Any]:
        """
        Deletes a tuned model by sending a DELETE request to the specified endpoint.
        
        Args:
            None: This function does not accept any arguments.
        
        Returns:
            A dictionary containing the response data.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the server returns a status code indicating a problem.
        
        Tags:
            delete, model, fine-tuning, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def generate_embeddings(self, content: Annotated[dict[str, Any], ''] = None, model: Annotated[Any, ''] = None) -> dict[str, Any]:
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
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
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
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
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
        path = ""
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