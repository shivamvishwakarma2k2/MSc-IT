import React from "react";
import CounterButtons from "./CounterButtons";
import { CounterProvider } from "./CounterContext";
import CounterDisplay from "./CounterDisplay";

function App() {
  return (
    // CounterProvider wraps the app to provide counter context to all children
    // Any component inside this provider can access the counter state
    <CounterProvider>
      <div style={{ textAlign: "center", marginTop: "50px" }}>
        <h1>Context API Counter App</h1>
        {/* CounterDisplay component shows the current counter value */}
        <CounterDisplay />
        {/* CounterButtons component provides button to increment counter */}
        <CounterButtons />
      </div>
    </CounterProvider>
  );
}

export default App;
