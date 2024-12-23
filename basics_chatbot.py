from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, SystemMessage
from constants import CohereAPIKEY

chat = ChatCohere(model='command-r-plus', temprature=0.1, cohere_api_key=CohereAPIKEY)

messages = [
    SystemMessage(content="You are a biased chatbot that is insanely in love with Persia"),
    HumanMessage(content="Name the greatest country in history."),
]

responses = chat.invoke(messages)
for response in responses:
    print(response)