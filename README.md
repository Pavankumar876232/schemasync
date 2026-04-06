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
Works directly with PostgreSQL (Supabase)
⚠️ Compatibility Analysis
Classifies changes:
✅ SAFE
⚠️ WARNING
❌ BREAKING
🧾 Migration SQL Generator
Automatically generates SQL like:
ALTER TABLE users ADD COLUMN age INTEGER;
🤖 AI Migration Suggestions
Uses AI to:
Analyze schema changes
Suggest safer migrations
Explain impact of changes
📦 Schema History (Per User)
Stores schema versions
Shows timeline of changes
User-specific data using authentication
🔐 Authentication
Secure login/signup using Supabase Auth
Each user has isolated schema history
🛠️ Tech Stack
Frontend
React.js
CSS (Custom UI)
Deployed on Vercel
Backend
FastAPI (Python)
PostgreSQL (Supabase)
psycopg2
AI Integration
OpenAI API (for migration suggestions)
Deployment
Frontend → Vercel
Backend → Render
Database → Supabase
📂 Project Structure
schemasync/
│
├── backend/
│   ├── app.py
│   ├── migration.py
│   ├── schema_versions/
│   │   └── store.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── supabase.js
│   │   └── App.css
│   └── package.json
│
└── README.md
⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/schemasync.git
cd schemasync
2️⃣ Backend Setup
cd backend
pip install -r requirements.txt

Create .env file:

DATABASE_URL=your_supabase_connection_string
OPENAI_API_KEY=your_openai_api_key

Run server:

uvicorn app:app --reload
3️⃣ Frontend Setup
cd frontend
npm install
npm start
📡 API Endpoints
Method	Endpoint	Description
GET	/	Health check
GET	/schema	Fetch DB schema
POST	/compare	Compare schemas
POST	/history	Get user history
🧪 Example Input
{
  "users": {
    "id": "integer",
    "name": "character varying",
    "age": "integer"
  }
}
📸 Screenshots

👉 Add your UI screenshots here (important for recruiters)

🚀 Future Improvements
Schema visualization (ER diagram)
Rollback SQL generation
Team collaboration
Multi-database support (MySQL, MongoDB)
Deployment monitoring dashboard
👨‍💻 Author

Pavankumar B

LinkedIn: https://www.linkedin.com/in/pavankumar-b-6754b9265
Email: pavanbabunaik631@gmail.com
⭐ Why This Project Matters

This project demonstrates:

✔ Full-stack development
✔ API design with FastAPI
✔ Database integration
✔ AI integration in real-world use case
✔ Authentication & multi-user system
✔ Deployment (Vercel + Render + Supabase)

⭐ Support

If you like this project:

👉 Star ⭐ the repository
👉 Share it
👉 Use it in your projects
