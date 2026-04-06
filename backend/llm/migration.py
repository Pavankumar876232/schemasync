import os

def generate_migration(diff):
    try:
        api_key = os.getenv("OPENAI_API_KEY")

        # If API key missing → fallback
        if not api_key:
            return "AI not configured (missing API key)"

        from openai import OpenAI
        client = OpenAI(api_key=api_key)

        prompt = f"""
You are a database migration expert.

Given schema diff:
{diff}

Generate SQL migration and explanation.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"LLM Error: {str(e)}"