from typing import Any, Dict,List
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration
import httpx
import logging

logger = logging.getLogger(__name__)

class GeminiapiApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='geminiapiapp', integration=integration, **kwargs)
        self.base_url = "https://generativelanguage.googleapis.com"

    def _get_headers(self) -> Dict[str, str]:
      """
      Override the base method to return empty headers.
      The Gemini API key is passed as a query parameter ('key'),
      not in an Authorization header for these endpoints.
      """
      logger.debug(f"Overriding _get_headers for {self.name}. Returning empty dict to prevent default auth header.")
      return {}

    def _add_api_key_param(self, params: Dict[str, Any] | None) -> Dict[str, Any]:
        """Helper to add the API key as a 'key' query parameter."""
        actual_params = params.copy() if params else {}
        if 'key' not in actual_params and self.integration:
            try:
                credentials = self.integration.get_credentials()
                api_key = credentials.get("api_key")
                if api_key:
                    actual_params['key'] = api_key
                    logger.debug("Added API key as query parameter.")
                else:
                      # This might happen if the store returned credentials without an api_key field
                    logger.warning("API key retrieved from integration credentials is None or empty.")
            except Exception as e:
                logger.error(f"Error retrieving API key from integration: {e}")
        return actual_params

    def _get(self, url: str, params: Dict[str, Any] | None = None) -> httpx.Response:
        """
        Make a GET request, ensuring the API key is added as a query parameter.
        """
        actual_params = self._add_api_key_param(params)
        logger.debug(f"Making GET request to {url} with params: {actual_params}")
        return super()._get(url, params=actual_params)

    def _post(
        self, url: str, data: Dict[str, Any], params: Dict[str, Any] | None = None
    ) -> httpx.Response:
        """
        Make a POST request, ensuring the API key is added as a query parameter.
        """
        actual_params = self._add_api_key_param(params)
        logger.debug(
            f"Making POST request to {url} with params: {actual_params} and data: {data}"
        )
        # Note: The parent _post in application.py still uses httpx.post directly
        # and calls self._get_headers() again, which is fine because our override returns {}.
        return super()._post(url, data=data, params=actual_params)

    def _delete(self, url: str, params: Dict[str, Any] | None = None) -> httpx.Response:
        """
        Make a DELETE request, ensuring the API key is added as a query parameter.
        """
        actual_params = self._add_api_key_param(params)
        logger.debug(f"Making DELETE request to {url} with params: {actual_params}")
        return super()._delete(url, params=actual_params)

    # --- Corrected Tool Method ---

    def text_only_input(
        self,
        contents: List[Dict[str, Any]], # Removed key=None
        generationConfig: Dict[str, Any] | None = None,
        safetySettings: List[Dict[str, Any]] | None = None
    ) -> Dict[str, Any]:
        """
        Generates content using the Gemini 1.5 Flash model via POST request.

        The API key is automatically added as a query parameter by the overridden _post method.

        Args:
            contents (list[dict[str, Any]]): contents Example: "[{'parts': [{'text': 'Write a story about a magic backpack.'}]}]".
            generationConfig (dict[str, Any], optional): generationConfig
            safetySettings (list[dict[str, Any]], optional): safetySettings
                Example:
                ```json
                {
                  "contents": [
                    {
                      "parts": [
                        {
                          "text": "List 5 popular cookie recipes"
                        }
                      ]
                    }
                  ],
                  "generationConfig": {
                    "response_mime_type": "application/json",
                    "response_schema": {
                      "items": {
                        "properties": {
                          "recipe_name": {
                            "type": "STRING"
                          }
                        },
                        "type": "OBJECT"
                      },
                      "type": "ARRAY"
                    }
                  }
                }
                ```

        Returns:
            dict[str, Any]: text-only input / text-and-image input / interractive chat / generate content from uploaded file / generate content from uploaded file / video[2]: generate content from uploaded file / video[3]: generate content from uploaded file / generate content from uploaded file / single-turn function calling / multi turn function call / JSON mode / random / generation config example

        Tags:
            Function Calling
        """
        # Ensure contents is not None, as it's a required parameter based on the OpenAPI spec
        if contents is None:
            raise ValueError("Missing required parameter 'contents'")
        if not isinstance(contents, list):
            # Add type checking for robustness based on expected input
            raise TypeError("'contents' must be a list")

        request_body = {
            'contents': contents,
        }
        if generationConfig is not None:
            request_body['generationConfig'] = generationConfig
        if safetySettings is not None:
            request_body['safetySettings'] = safetySettings

        url = f"{self.base_url}/v1beta/models/gemini-1.5-flash-8b-exp-0827:generateContent"
        # No explicit 'key' parameter needed here; _post handles it from integration
        query_params = {}

        logger.debug(f"Calling _post for generateContent with body: {request_body} and params: {query_params}")

        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status() # This will raise HTTPError for 400 status
        return response.json()

    # --- Rest of the tool methods (same as previous correction) ---
    def fetch_model(self) -> Dict[str, Any]:
        # ... (keep the implementation as before) ...
        url = f"{self.base_url}/v1beta/models/gemini-1.5-flash-8b-exp-0827"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def fetch_models(self, pageSize=None, pageToken=None) -> Dict[str, Any]:
        # ... (keep the implementation as before) ...
        url = f"{self.base_url}/v1beta/models"
        query_params = {k: v for k, v in [('pageSize', pageSize), ('pageToken', pageToken)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def generate_atext_stream(self, alt=None, contents=None) -> Any:
        # ... (keep the implementation as before) ...
        request_body = {
            'contents': contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/models/gemini-1.5-flash-8b-exp-0827:streamGenerateContent"
        query_params = {k: v for k, v in [('alt', alt)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    # ... (include all other tool methods like generate_atext_stream, resumable_upload_request,
    # prompt_document, text_tokens, fetch_tuned_models, create_atuned_model,
    # prompt_the_tuned_model, delete_tuned_model, generate_embeddings, batch_embeddings,
    # discovery_document - they can remain as they were in the previous corrected version,
    # as they now correctly rely on the overridden _get/_post/_delete which handle the key param
    # and the overridden _get_headers which prevents the incorrect header.)

    def generate_atext_stream(self, alt=None, contents=None) -> Any:
        # ... (keep the implementation as before) ...
        request_body = {
            'contents': contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/models/gemini-1.5-flash-8b-exp-0827:streamGenerateContent"
        query_params = {k: v for k, v in [('alt', alt)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def resumable_upload_request(self, file=None) -> Any:
        # ... (keep the implementation as before) ...
        request_body = {
            'file': file,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/upload/v1beta/files"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def prompt_document(self, contents=None) -> Dict[str, Any]:
        # ... (keep the implementation as before) ...
        request_body = {
            'contents': contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/models/gemini-1.5-pro-latest:generateContent"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def text_tokens(self, contents=None) -> Dict[str, Any]:
        # ... (keep the implementation as before) ...
        request_body = {
            'contents': contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/models/gemini-1.5-flash-8b-exp-0827:countTokens"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def fetch_tuned_models(self, page_size=None) -> Dict[str, Any]:
        # ... (keep the implementation as before) ...
        url = f"{self.base_url}/v1beta/tunedModels"
        query_params = {k: v for k, v in [('page_size', page_size)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atuned_model(self, base_model=None, display_name=None, tuning_task=None) -> Dict[str, Any]:
        # ... (keep the implementation as before) ...
        request_body = {
            'base_model': base_model,
            'display_name': display_name,
            'tuning_task': tuning_task,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/tunedModels"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def prompt_the_tuned_model(self, tunedModel, contents=None) -> Dict[str, Any]:
        # ... (keep the implementation as before) ...
        if tunedModel is None:
            raise ValueError("Missing required parameter 'tunedModel'")
        request_body = {
            'contents': contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/{tunedModel}:generateContent"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tuned_model(self, tunedModel) -> Dict[str, Any]:
        # ... (keep the implementation as before) ...
        if tunedModel is None:
            raise ValueError("Missing required parameter 'tunedModel'")
        url = f"{self.base_url}/v1beta/{tunedModel}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def generate_embeddings(self, content=None, model=None) -> Dict[str, Any]:
        # ... (keep the implementation as before) ...
        request_body = {
            'content': content,
            'model': model,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/models/text-embedding-004:embedContent"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def batch_embeddings(self, requests=None) -> Dict[str, Any]:
        # ... (keep the implementation as before) ...
        request_body = {
            'requests': requests,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/models/text-embedding-004:batchEmbedContents"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def discovery_document(self, version=None) -> Dict[str, Any]:
        # ... (keep the implementation as before) ...
        url = f"{self.base_url}/$discovery/rest"
        query_params = {k: v for k, v in [('version', version)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        # ... (keep the implementation as before) ...
        return [
            self.fetch_model,
            self.fetch_models,
            self.text_only_input,
            self.generate_atext_stream,
            self.resumable_upload_request,
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