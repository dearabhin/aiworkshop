import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

client = genai.Client(api_key=api_key)

# Generate content

response = client.models.generate_content(
    model="gemini-2.0-flash-exp",
    contents=["whats the date today?"]
)

# Print the generated response
print(response.text)
