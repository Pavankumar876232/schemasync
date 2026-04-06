import os

def generate_migration(diff):
    try:
        api_key = os.getenv("OPENAI_API_KEY")

        # 🔹 Case 1: No API key
        if not api_key:
            return "⚠️ AI not configured (missing OPENAI_API_KEY)"

        # 🔹 Lazy import (prevents startup crash)
        from openai import OpenAI
        client = OpenAI(api_key=api_key)

        prompt = f"""
You are a database migration expert.

Given the schema difference:
{diff}

Generate:
1. SQL migration (PostgreSQL)
2. Clear explanation

Rules:
- Prefer safe, backward-compatible changes
- Avoid data loss
- Keep SQL clean and production-ready
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    # 🔹 Handle quota / billing issue
    except Exception as e:
        error_msg = str(e)

        if "insufficient_quota" in error_msg:
            return "⚠️ OpenAI quota exceeded. Please add billing to continue."

        if "authentication" in error_msg.lower():
            return "⚠️ Invalid API key. Check your OPENAI_API_KEY."

        return f"⚠️ LLM Error: {error_msg}"