# 🚀 SchemaSync — Distributed Schema Evolution Manager

## 📌 Overview

SchemaSync is a full-stack system that tracks database schema changes, detects differences, evaluates compatibility, and generates SQL migration scripts automatically.

It helps developers avoid breaking changes and safely evolve database schemas across applications.

---

## 🧠 Problem Statement

Managing database schema changes manually is risky and error-prone.

* ❌ Breaking changes can crash production systems
* ❌ Manual SQL migrations are tedious
* ❌ No visibility into schema evolution

---

## ✅ Solution

SchemaSync automates schema management by:

* Extracting current database schema
* Comparing with new schema input
* Detecting added, removed, and modified fields
* Classifying changes (SAFE / BREAKING / WARNING)
* Generating SQL migration scripts automatically

---

## 🏗️ Architecture

```
Frontend (React - Vercel)
        ↓
Backend (FastAPI - Render)
        ↓
Database (PostgreSQL - Supabase)
```

---

## ⚙️ Tech Stack

| Layer      | Technology               |
| ---------- | ------------------------ |
| Frontend   | React                    |
| Backend    | FastAPI                  |
| Database   | PostgreSQL               |
| Deployment | Render, Vercel, Supabase |
| Language   | Python, JavaScript       |

---

## ✨ Features

* 🔍 Schema extraction from PostgreSQL
* 🔄 Schema diff detection
* ⚠️ Compatibility analysis (SAFE / BREAKING / WARNING)
* 🧾 Automatic SQL migration generation
* 🌐 Web-based dashboard
* ☁️ Fully deployed cloud system

---

## 📸 Demo

👉 Live Demo: https://schemasync-five.vercel.app
👉 Backend API: https://schemasync.onrender.com

---

## 🧪 Example Input

```json
{
  "users": {
    "id": "integer",
    "name": "character varying",
    "age": "integer"
  }
}
```

---

## 📤 Example Output

```json
{
  "diff": {
    "added": ["age"],
    "removed": [],
    "modified": []
  },
  "compatibility": [
    {
      "column": "age",
      "status": "SAFE",
      "message": "New column added"
    }
  ],
  "migration_sql": [
    "ALTER TABLE users ADD COLUMN age integer;"
  ]
}
```

---

## 🚀 How to Run Locally

### 🔹 Clone repo

```bash
git clone https://github.com/Pavankumar876232/schemasync.git
cd schemasync
```

---

### 🔹 Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
```

---

### 🔹 Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

### 🔹 Environment Variable

Create `.env` or set:

```
DATABASE_URL=your_postgresql_connection_string
```

---

## ☁️ Deployment

* Backend → Render
* Frontend → Vercel
* Database → Supabase

---

## 📈 Future Improvements

* 📦 Schema version history tracking
* 🤖 LLM-based smart migration generation
* 📊 Advanced UI dashboard
* 🔐 Authentication & multi-user support

---

## 👨‍💻 Author

**Pavankumar B**

* LinkedIn: https://www.linkedin.com/in/pavankumar-b-6754b9265
* Email: [pavanbabunaik631@gmail.com](mailto:pavanbabunaik631@gmail.com)

---

## ⭐ Conclusion

SchemaSync simplifies database schema evolution by automating detection, validation, and migration — making systems more reliable and developer-friendly.

---

⭐ If you like this project, give it a star!
