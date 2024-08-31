import time, json, os
from groq import Groq
from dotenv import load_dotenv

# Loads environment variables (in this case just the API key)
load_dotenv()

# Instantiates a client which uses the key to authenticate API calls
client = Groq(
    api_key = os.getenv("API_KEY")
)

# Opens the input file and reads it, then splits it line by line into list of prompts
inputFile = open("input.txt")
inputs = inputFile.read().split("\n")
outputList = []


# Loops through the list of prompts
for input in inputs:
  # Stores the time at which the request is sent by the client
  start_time = int(time.time())
  chat_completion_test = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": input,
          }
      ],
      model="llama3-70b-8192",
  )
  # Stores the time at which the response is received by the client
  end_time = int(time.time())

  # Puts the data into a python dict equivalent to the JSON object needed
  outputObject = {
      "Prompt": input,
      "Message": chat_completion_test.choices[0].message.content,
      "TimeSent": start_time,
      "TimeRecvd": end_time,
      "Source": "Groq"
  }
  # Adds the dict to the array of dicts
  outputList.append(outputObject)

# Writes the python list as a JSON array to the output.json file using the json.dump method
f = open('output.json', 'wt')
json.dump(outputList, f, indent=4)