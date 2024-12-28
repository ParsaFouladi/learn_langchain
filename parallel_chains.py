from constants import CohereAPIKEY
from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere import ChatCohere

chat_model = ChatCohere(model='command-r-plus', temperature=1, cohere_api_key=CohereAPIKEY)

message_prompt_poem = ChatPromptTemplate.from_messages([
    ("system", " تو یک شاعر ایرانی هستی "),
    ("human", "یک شعر دو بیتی درباره‌ی {topic} بگو")
    ])

chain_poem = message_prompt_poem | chat_model

message_prompt_story = ChatPromptTemplate.from_messages([
    ("system", " تو یک نویسنده‌ی ایرانی هستی "),
    ("human", "یک داستان خیلی خیلی خیلی کوتاه درباره‌ی {topic}")
])

chain_story = message_prompt_story | chat_model

from langchain_core.runnables import RunnableParallel

combined = RunnableParallel(poem=chain_poem, story=chain_story)

content_ai=combined.invoke({"topic": "پاییز"})

print(content_ai)

