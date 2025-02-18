from dotenv import load_dotenv
import os
import litellm 

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure liteLLM
litellm.api_key = GEMINI_API_KEY

def main():
    persona = "I am a friendly AI assistant. I am here to help you with any questions you have. Feel free to ask me anything!"
    print(persona)
    
    while True:
        try:
            user_input = input("Ask something! ")
            if user_input.lower() == 'exit':
                print("Exiting conversation. Goodbye!")
                break
            
            response = litellm.completion(
                model="gemini-pro",  # Adjust the model name as needed
                messages=[{"role": "system", "content": persona},
                          {"role": "user", "content": user_input}],
                max_tokens=100,
                temperature=0.7
            )
            
            print(f"AI: {response['choices'][0]['message']['content']}")
        except Exception as e:
            print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     main()
