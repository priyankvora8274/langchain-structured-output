from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()
model = ChatOpenAI(model='gpt-5.2')

# Annotated: So, we can add the annotation for each field in TypedDict. So, if we fill model may be misinterpret the meaning from keys,
# description give with annotation will be also sent to the model. 

# Optional: To define the value of any key from the dict as an optional. So, let say if we are expecting that for  some keys in dict, 
# the value may not be present in LLM response we can define it as optional

#Literal: With help of this we can define the fixed options for the value of any dict keys, instead of getting any string.

class Review(TypedDict):
    key_themes: Annotated[list[str], 'write down all key theams discussed in the review']
    summary: Annotated[str, 'A brief description of the review']
    sentiment: Annotated[Literal["Pos", "Neg"],'sentiment of the review, which will be either positive, negative or neutral']
    pros: Optional[Annotated[list[str],'write down all pros in list from the given review if it is mentioned in the review']]
    cons: Optional[Annotated[list[str],'write down all cons in  the list from the given review if it is mentioned in the review']]
    reviewer_name: Optional[Annotated[str,'Write the name of reviewer if given']]
     
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

print(result)
# print(result["sentiment"])
# print(result["reviewer_name"])