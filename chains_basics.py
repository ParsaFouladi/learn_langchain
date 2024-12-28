from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere import ChatCohere
from constants import CohereAPIKEY

chat_model = ChatCohere(model='command-r-plus', temperature=1, cohere_api_key=CohereAPIKEY)

message_prompt = ChatPromptTemplate.from_messages([
    ('system', 'You are a math teacher'),
    ('human', 'what is the sum of {first}+{second}?')
])

chain=message_prompt | chat_model

chat_ai = chain.invoke({"first":"212" , "second": "-6"})

print(chat_ai.content)