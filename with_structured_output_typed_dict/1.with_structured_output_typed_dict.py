from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()
model = ChatOpenAI(model='gpt-5.2')

class Review(TypedDict):
    summary: str
    sentiment: str
     
structured_model = model.with_structured_output(Review)
 
review = """I am really disappointed with this MacBook Air. The battery drains much faster than advertised, 
and the laptop gets hot even when running basic applications. It frequently lags when I open multiple tabs, 
making multitasking frustrating. Considering the high price, the performance is not worth the money.
I would not recommend this product to anyone looking for a reliable laptop."""

result = structured_model.invoke(review)

print(result)