# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# from langchain.chains import ConversationChain
# from langchain.memory import ConversationBufferMemory
# from langchain.schema import SystemMessage, HumanMessage, AIMessage
# import os 

# # Load environment variables from .env file
# load_dotenv()

# # Get the API key from environment variables
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# llm = ChatGoogleGenerativeAI(
#     api_key=GEMINI_API_KEY,
#     model="gemini-2.0-flash-exp",
#     max_tokens=100,
#     temperature=0.7
# )
# memory = ConversationBufferMemory(return_messages=True)

# conversation = ConversationChain(
#     llm=llm, 
#     verbose=True, 
#     memory=memory
# )

# persona = "I am a friendly AI assistant. I am here to help you with any questions you have. Feel free to ask me anything!"
# while True:
#     try:
#         conversation.memory.buffer.append(SystemMessage(content=persona))
#         user_input = input("Ask something! ")
#         if user_input.lower() == 'exit':
#             print("Exiting conversation. Goodbye!")
#             break
#         ai_response = conversation.predict(input=user_input)
#         print(f"AI: {ai_response}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv # type: ignore
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import os 

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def main():
    llm = ChatGoogleGenerativeAI(
        api_key=GEMINI_API_KEY,
        model="gemini-2.0-flash-exp",
        max_tokens=100,
        temperature=0.7
    )
    memory = ConversationBufferMemory(return_messages=True)

    conversation = ConversationChain(
        llm=llm, 
        verbose=True, 
        memory=memory
    )

    persona = "I am a friendly AI assistant. I am here to help you with any questions you have. Feel free to ask me anything!"
    while True:
        try:
            conversation.memory.buffer.append(SystemMessage(content=persona))
            user_input = input("Ask something! ")
            if user_input.lower() == 'exit':
                print("Exiting conversation. Goodbye!")
                break
            ai_response = conversation.predict(input=user_input)
            print(f"AI: {ai_response}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
