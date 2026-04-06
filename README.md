🚀 SchemaSync – AI-Powered Database Migration Assistant

SchemaSync is a full-stack web application that helps developers compare database schemas, detect changes, and generate safe migration scripts using AI.

🌐 Live Demo
🔗 Frontend: https://schemasync-five.vercel.app
🔗 Backend API: https://schemasync.onrender.com
📌 Features
🔍 Schema Comparison
Detects:
Added columns
Removed columns
Modified columns
Works with PostgreSQL (Supabase)
⚠️ Compatibility Analysis
Classifies schema changes:
✅ SAFE
⚠️ WARNING
❌ BREAKING
🧾 Migration SQL Generator

Automatically generates SQL queries:

ALTER TABLE users ADD COLUMN age INTEGER;
🤖 AI Migration Suggestions
Analyze schema changes
Suggest safe migrations
Explain impact
📦 Schema History (Per User)
Stores schema versions
Displays timeline
User-specific data
🔐 Authentication
Login/signup using Supabase
Separate user data
🛠️ Tech Stack
Frontend
React.js
CSS
Vercel
Backend
FastAPI (Python)
PostgreSQL (Supabase)
psycopg2
AI
OpenAI API
📂 Project Structure
schemasync/
├── backend/
│   ├── app.py
│   ├── migration.py
│   ├── schema_versions/
│   │   └── store.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── supabase.js
│   │   └── App.css
│   └── package.json
└── README.md
⚙️ Setup Instructions
Clone
git clone https://github.com/Pavankumar876232/schemasync.git
cd schemasync
Backend
cd backend
pip install -r requirements.txt

Create .env:

DATABASE_URL=your_supabase_connection_string
OPENAI_API_KEY=your_openai_api_key

Run:

uvicorn app:app --reload
Frontend
cd frontend
npm install
npm start
📡 API
Method	Endpoint	Description
GET	/	Health
GET	/schema	Get schema
POST	/compare	Compare
POST	/history	History
🧪 Example Input
{
  "users": {
    "id": "integer",
    "name": "character varying",
    "age": "integer"
  }
}
📸 Screenshots

Add screenshots here (important)

🚀 Future Improvements
Schema visualizer
Rollback SQL
Multi-DB support
Team collaboration
👨‍💻 Author

Pavankumar B

LinkedIn: https://www.linkedin.com/in/pavankumar-b-6754b9265
Email: pavanbabunaik631@gmail.com
⭐ Why This Project Matters
Full-stack development
FastAPI backend
AI integration
Authentication system
Cloud deployment
⭐ Support

⭐ Star this repo
🔁 Share it
💡 Use it
