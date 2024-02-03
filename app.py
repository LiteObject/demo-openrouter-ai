from openai import OpenAI
from os import getenv
from dotenv import load_dotenv, find_dotenv
import timeit
import streamlit as st

load_dotenv(find_dotenv())


def main():
    # gets API Key from environment variable OPENAI_API_KEY
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=getenv("OPENROUTER_API_KEY"),
    )

    user_query = st.text_input("Enter your query")

    if st.button('Submit'):
        startTime = timeit.default_timer()
        completion = client.chat.completions.create(
            extra_headers={
                # "HTTP-Referer": $YOUR_SITE_URL, # Optional, for including your app on openrouter.ai rankings.
                # "X-Title": $YOUR_APP_NAME, # Optional. Shows in rankings on openrouter.ai.
            },
            model="openai/gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": user_query,
                },
            ],
        )

        endTime = timeit.default_timer()
        st.write(completion.choices[0].message.content)
        st.write(f"\n\nQuery execution time: {endTime - startTime:.3f} s.")        

if __name__ == "__main__":
    main()
