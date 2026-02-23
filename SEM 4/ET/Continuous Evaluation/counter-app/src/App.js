import React, { useState } from 'react';
import './App.css';

// Main App component
function App() {

  // State variable to store counter value (initial value = 0)
  const [count, setCount] = useState(0);

  // Function to increase counter by 1
  const increase = () => {
    setCount(count + 1);
  };

  // Function to decrease counter by 1
  const decrease = () => {
    setCount(count - 1);
  };

  // Function to reset counter to 0
  const reset = () => {
    setCount(0);
  };

  // JSX returned by component
  return (
    <div style={{ textAlign: "center" }}>

      {/* App title */}
      <h2>Counter App - 6709</h2>

      {/* Display current counter value */}
      <h1>{count}</h1>

      {/* Button to decrease counter */}
      <button style={styles.spacing} onClick={decrease}>
        Decrease (-1)
      </button>

      {/* Button to reset counter */}
      <button style={styles.spacing} onClick={reset}>
        Reset (0)
      </button>

      {/* Button to increase counter */}
      <button style={styles.spacing} onClick={increase}>
        Increase (1)
      </button>

    </div>
  );
}

// Style object for button spacing
const styles = {
  spacing: {
    margin: "10px",   // Space outside button
    padding: "10px",  // Space inside button
  }
};

export default App;