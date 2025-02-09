import os
from dotenv import load_dotenv
load_dotenv()

from promptflow.core import Prompty, AzureOpenAIModelConfiguration
from promptflow.evals.evaluators import ChatEvaluator

model_config = AzureOpenAIModelConfiguration(
    azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

chat_history=[
    {"role": "user", "content": "which city has golden gate bridge?"},
    {"role": "assistant", "content": "The Golden Gate Bridge is located in San Francisco, California"}
]
chat_input="Where is Status of Liberty?"

prompty = Prompty.load("chat.prompty", model={'configuration': model_config})
response = prompty(chat_history=chat_history, chat_input=chat_input)

conversation = chat_history
conversation += [
    {"role": "user", "content": chat_input},
    {"role": "assistant", "content": response}
]

chat_eval = ChatEvaluator(model_config=model_config)
score = chat_eval(conversation=conversation)

print(score)