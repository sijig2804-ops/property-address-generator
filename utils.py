import json

import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

def generate_addresses(state, count):

    prompt = f"""
Generate {count} realistic synthetic property addresses.

State: {state}

Return ONLY valid JSON.

Schema:

[
  {{
    "Property Type":"",
    "Street Number":"",
    "Street Name":"",
    "City":"",
    "State":"",
    "County":"",
    "Zip Code":""
  }}
]

Requirements:
- No duplicate addresses
- Realistic city names
- Realistic county names
- Property Type must be one of:
  Single Family
  Condo
  Townhome
  Multi Family
"""

    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {
                "role":"system",
                "content":"Generate valid JSON only."
            },
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    content = response.choices[0].message.content

    return json.loads(content)
