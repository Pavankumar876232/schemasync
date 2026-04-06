import React, { useState, useEffect } from "react";
import "./App.css";
import supabase from "./supabase";

function App() {
  const [schema, setSchema] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);

  // 🔐 AUTH
  const [user, setUser] = useState(null);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  useEffect(() => {
    supabase.auth.getSession().then(({ data }) => {
      setUser(data.session?.user || null);
    });

    supabase.auth.onAuthStateChange((_event, session) => {
      setUser(session?.user || null);
    });
  }, []);

  // 🔐 AUTH FUNCTIONS
  const signUp = async () => {
    const { error } = await supabase.auth.signUp({
      email,
      password
    });
    if (error) alert(error.message);
    else alert("Signup successful! Please login.");
  };

  const login = async () => {
    const { error } = await supabase.auth.signInWithPassword({
      email,
      password
    });
    if (error) alert(error.message);
  };

  const logout = async () => {
    await supabase.auth.signOut();
  };

  // 🔹 FORMAT TIME
  const formatTime = (timestamp) => {
    return timestamp; // already formatted from backend
  };

  // 🔹 COMPARE
  const runCompare = async () => {
    try {
      setLoading(true);

      const response = await fetch("https://schemasync.onrender.com/compare", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          schema: JSON.parse(schema),
          user_id: user.id
        })
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      alert("Invalid JSON or backend error");
    } finally {
      setLoading(false);
    }
  };

  // 🔹 LOAD HISTORY (USER SPECIFIC)
  const loadHistory = async () => {
    try {
      const res = await fetch("https://schemasync.onrender.com/history", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ user_id: user.id })
      });

      const data = await res.json();
      setHistory(data.history || []);
    } catch (error) {
      alert("Error loading history");
    }
  };

  // 🔐 LOGIN UI
  if (!user) {
    return (
      <div className="container">
        <h2>🔐 Login</h2>

        <input
          type="email"
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button onClick={login}>Login</button>
        <button onClick={signUp}>Sign Up</button>
      </div>
    );
  }

  // 🔓 MAIN UI
  return (
    <div className="container">
      <h1>🚀 SchemaSync Dashboard</h1>

      <p>👤 Logged in as: {user.email}</p>
      <button onClick={logout}>Logout</button>

      {/* INPUT */}
      <div className="card">
        <h3>📥 Enter Schema</h3>
        <textarea
          placeholder="Paste schema JSON here..."
          value={schema}
          onChange={(e) => setSchema(e.target.value)}
        />

        <div style={{ display: "flex", gap: "10px" }}>
          <button onClick={runCompare}>
            {loading ? "Processing..." : "Run Compare"}
          </button>

          <button onClick={loadHistory}>
            Load History
          </button>
        </div>
      </div>

      {/* RESULTS */}
      {result && (
        <div className="results">

          {/* DIFF */}
          <div className="card">
            <h3>📊 Diff</h3>
            <ul>
              <li><b>Added:</b> {result.diff.added.join(", ") || "None"}</li>
              <li><b>Removed:</b> {result.diff.removed.join(", ") || "None"}</li>
              <li><b>Modified:</b> {result.diff.modified.join(", ") || "None"}</li>
            </ul>
          </div>

          {/* COMPATIBILITY */}
          <div className="card">
            <h3>⚠️ Compatibility</h3>
            {result.compatibility.length === 0 && <p>No issues</p>}
            {result.compatibility.map((item, index) => (
              <div key={index} className={`badge ${item.status.toLowerCase()}`}>
                <strong>{item.column}</strong> → {item.status}
              </div>
            ))}
          </div>

          {/* SQL */}
          <div className="card">
            <h3>🧾 Migration SQL</h3>
            {result.migration_sql.length === 0 && <p>No changes</p>}
            {result.migration_sql.map((sql, index) => (
              <pre key={index}>{sql}</pre>
            ))}
          </div>

          {/* 🤖 AI */}
          {result.llm_suggestion && (
            <div className="card">
              <h3>🤖 AI Migration Suggestion</h3>
              <pre style={{ whiteSpace: "pre-wrap" }}>
                {result.llm_suggestion}
              </pre>
            </div>
          )}

        </div>
      )}

      {/* 📦 USER HISTORY */}
      {history.length > 0 && (
        <div className="card">
          <h3>📦 Your Schema Timeline</h3>

          {history.map((item, index) => (
            <div key={index} className="timeline-item">
              🟢 {formatTime(item.timestamp)} <br />

              ➕ Added: {item.diff?.added?.join(", ") || "None"} <br />
              ❌ Removed: {item.diff?.removed?.join(", ") || "None"} <br />
              🔁 Modified: {item.diff?.modified?.join(", ") || "None"} <br />
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;