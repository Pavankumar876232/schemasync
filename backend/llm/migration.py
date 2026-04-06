import os
from openai import OpenAI

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_migration(diff):
    prompt = f"""
    You are a database expert.

    Given this schema difference:
    {diff}

    Generate:
    1. SQL migration queries
    2. Short explanation

    Output JSON like:
    {{
        "sql": ["SQL query here"],
        "explanation": "Explanation here"
    }}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return str(e)