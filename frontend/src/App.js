import React, { useState } from "react";

function App() {
  const [schema, setSchema] = useState("");
  const [result, setResult] = useState(null);

  const runCompare = async () => {
    try {
      const response = await fetch("https://schemasync.onrender.com/compare", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: schema
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Error connecting to backend");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>SchemaSync Dashboard</h1>

      <textarea
        rows="10"
        cols="50"
        placeholder='Enter schema JSON...'
        value={schema}
        onChange={(e) => setSchema(e.target.value)}
      />

      <br /><br />

      <button onClick={runCompare}>Run Compare</button>

      <br /><br />

      {result && (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}
    </div>
  );
}

export default App;