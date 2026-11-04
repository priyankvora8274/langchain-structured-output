from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()
model = ChatOpenAI(model='gpt-5.2')

# this is similar version TypedDict, but with help of Pydentic library

# main advantage of using Pydentic is, we can also add data validation. It ensures data we work with is correct and has correct datatype. On other side,
# Typed dict does not check that, it just give us hint of the datatype of value. 
class Review(BaseModel):
    key_themes: list[str] = Field(description='write down all key theams discussed in the review')
    summary: str = Field(description='A brief description of the review')
    sentiment: Literal['pos','neg'] = Field(description='sentiment of the review, which will be either positive, negative or neutral')
    pros: Optional[list[str]] = Field(description='write down all pros in list from the given review if it is mentioned in the review')
    cons: Optional[list[str]] = Field(description='write down all cons in  the list from the given review if it is mentioned in the review')
    reviewer_name: Optional[str] = Field(description='Write the name of reviewer if given')
     
structured_model = model.with_structured_output(Review)
 
review = """**Product Name:** Samsung Galaxy S24 Ultra

I have been using the Samsung Galaxy S24 Ultra for about three months, and my experience has been mixed. While the phone offers some impressive features, there are several issues that make me question whether it is worth its expensive price tag.
**Pros:**
1. **Camera:** Excellent photo quality with impressive zoom capabilities.
2. **Display:** Bright, colorful AMOLED screen with smooth performance.
3. **Performance:** Fast processor that handles multitasking and gaming well.
4. **Design:** Premium build quality with a useful S Pen.

**Cons:**
1. **Battery Life:** Battery drains quickly, especially during gaming and video calls.
2. **Overheating:** The phone gets noticeably hot during heavy usage.
3. **Price:** Extremely expensive compared to other smartphones.
4. **Charging:** Charging speed is slower than expected.
"""

result = structured_model.invoke(review)

print(result.summary)
# print(result["sentiment"])
# print(result["reviewer_name"])