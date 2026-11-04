from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model='gpt-5.2')

# this is same thing we described as in other TypedDict, and Pydentic, but with help of Json Schema Syntex.
# Advantage: JSON schema is widely used and accepted structured format as compared to other. So, let say we are working on Frontend App &
#           Backed app, so Json structured can be used for all. Because we will use different languages not just python
#           Also we do not need extra library, and it provides data validation as well.
# The return type of model output when we use Json schema is dict type.
review_schema = {
    "title": "Review",
    "type": "object",
    "description": "Structured information extracted from a review",
    "properties": {
        "key_themes": {
            "title": "Key Themes",
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Write down all key themes discussed in the review"
        },
        "summary": {
            "title": "Summary",
            "type": "string",
            "description": "A brief description of the review"
        },
        "sentiment": {
            "title": "Sentiment",
            "type": "string",
            "enum": ["pos", "neg"],
            "description": "Sentiment of the review, either positive or negative"
        },
        "pros": {
            "title": "Pros",
            "type": ["array", "null"],
            "items": {
                "type": "string"
            },
            "description": "List all pros mentioned in the review, if any"
        },
        "cons": {
            "title": "Cons",
            "type": ["array", "null"],
            "items": {
                "type": "string"
            },
            "description": "List all cons mentioned in the review, if any"
        },
        "reviewer_name": {
            "title": "Reviewer Name",
            "type": ["string", "null"],
            "description": "Name of the reviewer, if provided"
        }
    },
    "required": [
        "key_themes",
        "summary",
        "sentiment"
    ],
    "additionalProperties": False
}
     
structured_model = model.with_structured_output(review_schema)
 
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


print(type(result))
print(result["sentiment"])
# print(result["reviewer_name"])