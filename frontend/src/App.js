import React, { useState } from "react";
import "./App.css";

function App() {
  const [schema, setSchema] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

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
      alert("Invalid JSON or backend error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>🚀 SchemaSync Dashboard</h1>

      {/* INPUT CARD */}
      <div className="card">
        <h3>Enter Schema</h3>
        <textarea
          placeholder="Paste schema JSON..."
          value={schema}
          onChange={(e) => setSchema(e.target.value)}
        />
        <button onClick={runCompare}>
          {loading ? "Processing..." : "Run Compare"}
        </button>
      </div>

      {/* RESULTS */}
      {result && (
        <div className="results">
          
          <div className="card">
            <h3>📊 Diff</h3>
            <pre>{JSON.stringify(result.diff, null, 2)}</pre>
          </div>

          <div className="card">
            <h3>⚠️ Compatibility</h3>
            <pre>{JSON.stringify(result.compatibility, null, 2)}</pre>
          </div>

          <div className="card">
            <h3>🧾 Migration SQL</h3>
            <pre>{JSON.stringify(result.migration_sql, null, 2)}</pre>
          </div>

        </div>
      )}
    </div>
  );
}

export default App;