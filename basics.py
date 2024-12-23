from constants import CohereAPIKEY
from langchain_cohere.llms import Cohere

model = Cohere(temperature=0.1,cohere_api_key=CohereAPIKEY, max_tokens=100)

message = "Name the greatest country in history."
response = model.invoke(message)
print(response)