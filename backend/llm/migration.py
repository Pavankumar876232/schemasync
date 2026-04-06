import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_migration(diff):
    try:
        prompt = f"""
You are a database migration expert.

Given schema diff:
{diff}

Generate:
1. Safe SQL migration
2. Explanation
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"LLM Error: {str(e)}"