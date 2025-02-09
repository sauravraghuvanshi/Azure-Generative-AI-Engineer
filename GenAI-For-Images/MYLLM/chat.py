import os
from dotenv import load_dotenv
load_dotenv()

from promptflow.core import Prompty, AzureOpenAIModelConfiguration

model_config = AzureOpenAIModelConfiguration(
    azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

prompty = Prompty.load("chat.prompty", model={'configuration': model_config})
result = prompty(
    chat_history=[
        {"role": "user", "content": "which city has golden gate bridge?"},
        {"role": "assistant", "content": "The Golden Gate Bridge is located in San Francisco, California"}
    ],
    chat_input="Where is Status of Liberty?")

print(result)