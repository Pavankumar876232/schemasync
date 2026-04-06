import os

def generate_migration(diff):
    try:
        # Temporary mock (to avoid crash)
        return f"""
AI Suggestion:

Safe migration detected.

SQL:
ALTER TABLE users ADD COLUMN age INTEGER;

Explanation:
This change is backward compatible and safe.
"""
    except Exception as e:
        return f"LLM Error: {str(e)}"