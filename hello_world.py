from openai import OpenAI
from os import getenv
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=getenv("OPENROUTER_API_KEY"),
)

completion = client.chat.completions.create(
  extra_headers={
    # "HTTP-Referer": $YOUR_SITE_URL, # Optional, for including your app on openrouter.ai rankings.
    # "X-Title": $YOUR_APP_NAME, # Optional. Shows in rankings on openrouter.ai.
  },
  model="openai/gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Say this Hello World!",
    },
  ],
)

print(completion.choices[0].message.content)