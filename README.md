🚀 SchemaSync — AI-Powered Schema Evolution Manager
📌 Overview

SchemaSync is a full-stack system that tracks database schema changes, detects differences, evaluates compatibility, and generates SQL migration scripts automatically.

It is enhanced with AI-powered migration suggestions and user-based schema history, helping developers safely evolve database schemas without breaking production systems.

🧠 Problem Statement

Managing database schema changes manually is risky and error-prone.

❌ Breaking changes can crash production systems
❌ Manual SQL migrations are tedious
❌ No visibility into schema evolution
❌ No intelligent guidance for safe migrations
✅ Solution

SchemaSync automates schema management by:

Extracting current database schema
Comparing with new schema input
Detecting added, removed, and modified fields
Classifying changes (SAFE / BREAKING / WARNING)
Generating SQL migration scripts automatically
🤖 Providing AI-based migration suggestions
📦 Storing schema history per user
🏗️ Architecture
Frontend (React - Vercel)
        ↓
Backend (FastAPI - Render)
        ↓
Database (PostgreSQL - Supabase)
        ↓
AI Layer (OpenAI API)
⚙️ Tech Stack
Layer	Technology
Frontend	React
Backend	FastAPI
Database	PostgreSQL (Supabase)
Auth	Supabase Auth
AI	OpenAI API
Deployment	Render, Vercel, Supabase
Language	Python, JavaScript
✨ Features
🔍 Schema extraction from PostgreSQL
🔄 Schema diff detection
⚠️ Compatibility analysis (SAFE / BREAKING / WARNING)
🧾 Automatic SQL migration generation
🤖 AI-powered migration suggestions
📦 Schema timeline (history tracking)
🔐 User authentication system
🌐 Web-based dashboard
☁️ Fully deployed cloud system
📸 Demo

👉 Live Demo: https://schemasync-five.vercel.app

👉 Backend API: https://schemasync.onrender.com

🧪 Example Input
{
  "users": {
    "id": "integer",
    "name": "character varying",
    "age": "integer"
  }
}
📤 Example Output
{
  "diff": {
    "added": ["age"],
    "removed": [],
    "modified": []
  },
  "compatibility": [
    {
      "column": "age",
      "status": "SAFE"
    }
  ],
  "migration_sql": [
    "ALTER TABLE users ADD COLUMN age integer;"
  ],
  "llm_suggestion": "Safe migration detected. This change is backward compatible."
}
🚀 How to Run Locally
🔹 Clone repo
git clone https://github.com/Pavankumar876232/schemasync.git
cd schemasync
🔹 Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
🔹 Frontend Setup
cd frontend
npm install
npm start
🔹 Environment Variable

Create .env file or set:

DATABASE_URL=your_postgresql_connection_string
OPENAI_API_KEY=your_openai_api_key
☁️ Deployment
Backend → Render
Frontend → Vercel
Database → Supabase
📈 Future Improvements
📊 Schema visualization (ER diagram)
🔁 Rollback SQL generation
🧠 Smarter AI suggestions
👥 Team collaboration
🌍 Multi-database support
👨‍💻 Author

Pavankumar B

LinkedIn: https://www.linkedin.com/in/pavankumar-b-6754b9265
Email: pavanbabunaik631@gmail.com
⭐ Conclusion

SchemaSync simplifies database schema evolution by combining automation, AI intelligence, and user tracking, making migrations safer, faster, and more reliable.

⭐ If you like this project, give it a star!
