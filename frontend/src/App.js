import { useState } from "react";
import axios from "axios";

function App() {
  const [data, setData] = useState(null);

  const runCompare = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/compare");
      setData(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>SchemaSync Dashboard</h1>

      <button onClick={runCompare}>Run Compare</button>

      {data && (
        <div>
          <h2>Result:</h2>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;