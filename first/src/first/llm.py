from litellm import completion
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# os.environ["GEMINI_API_KEY"] = "AIzaSyDbXGBxDyh4eIefWweoEQz-8Ic6woz14io"
os.environ["GEMINI_API_KEY"] =  os.getenv("GEMINI_API_KEY")

# os.environ["OPENAI_API_KEY"] = ""


# openai
# def openai():
#     response = completion(
#         model="openai/gpt-4o",
#         messages=[{ "content": "Hello, how are you?","role": "user"}]
#     )

#     print(response)

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )

    print(response)

def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )

   
    ai_response=response.choices[0].message.content
    print(ai_response)