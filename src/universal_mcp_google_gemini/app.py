from typing import Any
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class GeminiapiApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='geminiapiapp', integration=integration, **kwargs)
        self.base_url = "https://generativelanguage.googleapis.com"

    def fetch_model(self) -> dict[str, Any]:
        """
        Retrieves the configuration details for the Gemini 1.5 Flash-8B model via a GET request.

        Returns:
            dict[str, Any]: model

        Tags:
            Models
        """
        url = f"{self.base_url}/v1beta/models/gemini-1.5-flash-8b-exp-0827"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def fetch_models(self, pageSize=None, pageToken=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of available models, supporting page size and token parameters for result navigation.

        Args:
            pageSize (string): The `pageSize` parameter specifies the maximum number of items to include in each page of the response for the GET operation at the `/v1beta/models` path. Example: '5'.
            pageToken (string): Used in GET requests to specify the page token for fetching the next page of results. Example: 'Chxtb2RlbHMvZ2VtaW5pLTEuNS1wcm8tbGF0ZXN0'.

        Returns:
            dict[str, Any]: models

        Tags:
            Models
        """
        url = f"{self.base_url}/v1beta/models"
        query_params = {k: v for k, v in [('pageSize', pageSize), ('pageToken', pageToken)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def text_only_input(self, key=None, contents=None, generationConfig=None, safetySettings=None) -> dict[str, Any]:
        """
        Generates content using the Gemini 1.5 Flash model via POST request with optional query parameters.

        Args:
            key (string): API key for authentication, required to authorize requests to the Gemini API. Example: '{{vault:apiKey}}'.
            contents (array): contents Example: "[{'parts': [{'text': 'Write a story about a magic backpack.'}]}]".
            generationConfig (object): generationConfig
            safetySettings (array): safetySettings
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
        request_body = {
            'contents': contents,
            'generationConfig': generationConfig,
            'safetySettings': safetySettings,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/models/gemini-1.5-flash-8b-exp-0827:generateContent"
        query_params = {k: v for k, v in [('key', key)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def generate_atext_stream(self, alt=None, contents=None) -> Any:
        """
        Generates a streaming response from the Gemini 1.5 Flash model for multimodal input content.

        Args:
            alt (string): Specifies the alternative format for the response, commonly set to "sse" for server-sent events, allowing for streaming of the generated content. Example: 'sse'.
            contents (array): contents
                Example:
                ```json
                {
                  "contents": [
                    {
                      "parts": [
                        {
                          "text": "Tell me about this instrument"
                        },
                        {
                          "inline_data": {
                            "mime_type": "image/jpeg"
                          }
                        }
                      ]
                    }
                  ]
                }
                ```

        Returns:
            Any: generate a text stream

        Tags:
            Text Generation
        """
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
        """
        Uploads a file to storage using the POST method, with headers specifying upload protocol, command, content length, and content type.

        Args:
            file (object): file
                Example:
                ```json
                {
                  "file": {
                    "display_name": "state_of_the_union_address.mp3"
                  }
                }
                ```

        Returns:
            Any: resumable upload request / resumable upload request / resumable upload request / upload request

        Tags:
            Document Processing
        """
        request_body = {
            'file': file,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/upload/v1beta/files"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def prompt_document(self, contents=None) -> dict[str, Any]:
        """
        Generates content using the Gemini model, accepting input prompts and returning a streamed response across various media types, such as text, images, and audio.

        Args:
            contents (array): contents
                Example:
                ```json
                {
                  "contents": [
                    {
                      "parts": [
                        {
                          "text": "Summarize the uploaded document."
                        },
                        {
                          "file_data": {
                            "file_uri": "{{FILE_URI}}",
                            "mime_type": "application/pdf"
                          }
                        }
                      ]
                    }
                  ]
                }
                ```

        Returns:
            dict[str, Any]: prompt document

        Tags:
            Document Processing
        """
        request_body = {
            'contents': contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/models/gemini-1.5-pro-latest:generateContent"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def text_tokens(self, contents=None) -> dict[str, Any]:
        """
        Calculates the number of tokens and billable characters for input content when using the Gemini 1.5 Flash 8B model.

        Args:
            contents (array): contents
                Example:
                ```json
                {
                  "contents": [
                    {
                      "parts": [
                        {
                          "text": "Hi, my name is Bob."
                        }
                      ],
                      "role": "user"
                    },
                    {
                      "parts": [
                        {
                          "text": "Hi Bob"
                        }
                      ],
                      "role": "model"
                    }
                  ]
                }
                ```

        Returns:
            dict[str, Any]: text tokens / chat tokens / media tokens

        Tags:
            Count Tokens
        """
        request_body = {
            'contents': contents,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/models/gemini-1.5-flash-8b-exp-0827:countTokens"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def fetch_tuned_models(self, page_size=None) -> dict[str, Any]:
        """
        Retrieves a list of tuned models at the specified page size using the GET method.

        Args:
            page_size (string): Specifies the maximum number of items to return in a single response page. Example: '10'.

        Returns:
            dict[str, Any]: fetch models Copy

        Tags:
            Fine Tunning
        """
        url = f"{self.base_url}/v1beta/tunedModels"
        query_params = {k: v for k, v in [('page_size', page_size)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atuned_model(self, base_model=None, display_name=None, tuning_task=None) -> dict[str, Any]:
        """
        Creates a tuned model using the "POST" method at the "/v1beta/tunedModels" endpoint and returns a response upon successful creation.

        Args:
            base_model (string): base_model Example: 'models/gemini-1.5-flash-001-tuning'.
            display_name (string): display_name Example: 'number generator model'.
            tuning_task (object): tuning_task
                Example:
                ```json
                {
                  "base_model": "models/gemini-1.5-flash-001-tuning",
                  "display_name": "number generator model",
                  "tuning_task": {
                    "hyperparameters": {
                      "batch_size": 2,
                      "epoch_count": 5,
                      "learning_rate": 0.001
                    },
                    "training_data": {
                      "examples": {
                        "examples": [
                          {
                            "output": "2",
                            "text_input": "1"
                          },
                          {
                            "output": "4",
                            "text_input": "3"
                          },
                          {
                            "output": "-2",
                            "text_input": "-3"
                          },
                          {
                            "output": "twenty three",
                            "text_input": "twenty two"
                          },
                          {
                            "output": "two hundred one",
                            "text_input": "two hundred"
                          },
                          {
                            "output": "one hundred",
                            "text_input": "ninety nine"
                          },
                          {
                            "output": "9",
                            "text_input": "8"
                          },
                          {
                            "output": "-97",
                            "text_input": "-98"
                          },
                          {
                            "output": "1,001",
                            "text_input": "1,000"
                          },
                          {
                            "output": "10,100,001",
                            "text_input": "10,100,000"
                          },
                          {
                            "output": "fourteen",
                            "text_input": "thirteen"
                          },
                          {
                            "output": "eighty one",
                            "text_input": "eighty"
                          },
                          {
                            "output": "two",
                            "text_input": "one"
                          },
                          {
                            "output": "four",
                            "text_input": "three"
                          },
                          {
                            "output": "eight",
                            "text_input": "seven"
                          }
                        ]
                      }
                    }
                  }
                }
                ```

        Returns:
            dict[str, Any]: create a tuned model

        Tags:
            Fine Tunning
        """
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

    def prompt_the_tuned_model(self, tunedModel, contents=None) -> dict[str, Any]:
        """
        Generates content using a specified tuned model defined at path "/v1beta/{tunedModel}:generateContent" by sending a POST request.

        Args:
            tunedModel (string): tunedModel
            contents (array): contents
                Example:
                ```json
                {
                  "contents": [
                    {
                      "parts": [
                        {
                          "text": "LXIII"
                        }
                      ]
                    }
                  ]
                }
                ```

        Returns:
            dict[str, Any]: prompt the tuned model

        Tags:
            Fine Tunning
        """
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

    def delete_tuned_model(self, tunedModel) -> dict[str, Any]:
        """
        Deletes a specified tuned model and returns a success status upon removal.

        Args:
            tunedModel (string): tunedModel

        Returns:
            dict[str, Any]: delete tuned model

        Tags:
            Fine Tunning
        """
        if tunedModel is None:
            raise ValueError("Missing required parameter 'tunedModel'")
        url = f"{self.base_url}/v1beta/{tunedModel}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def generate_embeddings(self, content=None, model=None) -> dict[str, Any]:
        """
        Generates a text embedding vector from input text using the specified Gemini Embedding model, allowing for semantic analysis and comparison of textual content.

        Args:
            content (object): content
            model (string): model
                Example:
                ```json
                {
                  "content": {
                    "parts": [
                      {
                        "text": "Hello world"
                      }
                    ]
                  },
                  "model": "models/text-embedding-004"
                }
                ```

        Returns:
            dict[str, Any]: generate embeddings

        Tags:
            Embeddings
        """
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

    def batch_embeddings(self, requests=None) -> dict[str, Any]:
        """
        Generates batch embeddings for a list of text inputs using the "text-embedding-004" model via a POST request to the "/v1beta/models/text-embedding-004:batchEmbedContents" endpoint.

        Args:
            requests (array): requests
                Example:
                ```json
                {
                  "requests": [
                    {
                      "content": {
                        "parts": [
                          {
                            "text": "What is the meaning of life?"
                          }
                        ]
                      },
                      "model": "models/text-embedding-004"
                    },
                    {
                      "content": {
                        "parts": [
                          {
                            "text": "How much wood would a woodchuck chuck?"
                          }
                        ]
                      },
                      "model": "models/text-embedding-004"
                    },
                    {
                      "content": {
                        "parts": [
                          {
                            "text": "How does the brain work?"
                          }
                        ]
                      },
                      "model": "models/text-embedding-004"
                    }
                  ]
                }
                ```

        Returns:
            dict[str, Any]: batch embeddings

        Tags:
            Embeddings
        """
        request_body = {
            'requests': requests,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/v1beta/models/text-embedding-004:batchEmbedContents"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def discovery_document(self, version=None) -> dict[str, Any]:
        """
        Retrieves discovery metadata for REST APIs, including available endpoints and parameters, based on the specified version.

        Args:
            version (string): Specifies the API version to use for the request, allowing clients to target a specific release without modifying the URI structure. Example: 'v1beta'.

        Returns:
            dict[str, Any]: Get Discovery Document
        """
        url = f"{self.base_url}/$discovery/rest"
        query_params = {k: v for k, v in [('version', version)] if v is not None}
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
