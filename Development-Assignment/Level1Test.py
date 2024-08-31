from groq import Groq
from dotenv import load_dotenv
import os

# Loads environment variables (in this case just the API key)
load_dotenv()

# Instantiates a client which uses the key to authenticate API calls
client = Groq(
    api_key = os.getenv("API_KEY")
)

# Makes a request using the create method for a chat completion
chat_completion_test = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Describe the Computer Science department of BITS Pilani, Goa Campus",
        }
    ],
    model="llama3-70b-8192",
)
# Outputs the generated content
print(chat_completion_test.choices[0].message.content)