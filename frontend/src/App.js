import React, { useState } from "react";
import "./App.css";

function App() {
  const [schema, setSchema] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);

  // 🔹 Format timestamp
  const formatTime = (filename) => {
    const raw = filename.replace("schema_", "").replace(".json", "");

    const year = raw.slice(0, 4);
    const month = raw.slice(4, 6);
    const day = raw.slice(6, 8);
    const hour = raw.slice(9, 11);
    const min = raw.slice(11, 13);
    const sec = raw.slice(13, 15);

    return `${day}/${month}/${year} ${hour}:${min}:${sec}`;
  };

  // 🔹 Compare API
  const runCompare = async () => {
    try {
      setLoading(true);

      const response = await fetch("https://schemasync.onrender.com/compare", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(JSON.parse(schema))
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Invalid JSON or backend error");
    } finally {
      setLoading(false);
    }
  };

  // 🔹 Load History
  const loadHistory = async () => {
    try {
      const res = await fetch("https://schemasync.onrender.com/history");
      const data = await res.json();
      setHistory(data.versions);
    } catch (error) {
      alert("Error loading history");
    }
  };

  return (
    <div className="container">
      <h1>🚀 SchemaSync Dashboard</h1>

      {/* INPUT */}
      <div className="card">
        <h3>📥 Enter Schema</h3>
        <textarea
          placeholder='Paste schema JSON here...'
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

          {/* 🤖 AI SUGGESTION */}
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

      {/* TIMELINE */}
      {history.length > 0 && (
        <div className="card">
          <h3>📦 Schema Timeline</h3>
          {history.map((item, index) => (
            <div key={index} className="timeline-item">
              🟢 Schema updated at {formatTime(item)}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;