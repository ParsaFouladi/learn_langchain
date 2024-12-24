from langchain_core.prompts import PromptTemplate
from constants import CohereAPIKEY
from langchain_cohere.llms import Cohere
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate

### For using templates with llms
# model=Cohere(temperature=5,cohere_api_key=CohereAPIKEY)


# prompt_templates = PromptTemplate.from_template('Generate a very short conversation between two mancs regarding {topic}.')

# response=model.invoke(prompt_templates.format(topic='weather'))

# print(response)
###

### for using templates with chatbot
chat_model = ChatCohere(model='command-r-plus', temprature=5, cohere_api_key=CohereAPIKEY)

message_templates=ChatPromptTemplate.from_messages([
    ('system', 'You are mistakful math teacher'),
    ('human', 'what is the summation of {first}+{second}?')
]

)

chat_ai = chat_model.invoke(message_templates.invoke({"first":"5" , "second": "6"}))

print(chat_ai.content)