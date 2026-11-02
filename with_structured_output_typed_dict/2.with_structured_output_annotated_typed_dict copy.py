from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()
model = ChatOpenAI(model='gpt-5.2')

# Annotated: So, we can add the annotation for each field in TypedDict. So, if we fill model may be misinterpret the meaning from keys,
# description give with annotation will be also sent to the model. 


class Review(TypedDict):
    summary: Annotated[str, 'A brief description of the review']
    sentiment: Annotated[str,'sentiment of the review, which will be either positive, negative or neutral']
     
structured_model = model.with_structured_output(Review)
 
review = """I am really disappointed with this MacBook Air. The battery drains much faster than advertised, 
and the laptop gets hot even when running basic applications. It frequently lags when I open multiple tabs, 
making multitasking frustrating. Considering the high price, the performance is not worth the money.
I would not recommend this product to anyone looking for a reliable laptop."""

result = structured_model.invoke(review)

print(result)