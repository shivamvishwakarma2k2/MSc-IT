import './App.css';
import React, { useState } from "react";

function App() {
  const [temp, setTemp] = useState("");
  const [message, setMessage] = useState(
    "Kindly enter a temperature in Celsius"
  );

  const checkWeather = (value) => {

    if (value === "") {
      setMessage("Kindly enter a temperature in Celsius");
    } else if (value < 10) {
      setMessage("Climate: Cold ❄️ | Wear warm clothes like jacket & sweater");
    } else if (value >= 10 && value < 25) {
      setMessage("Climate: Pleasant 🌤️ | Wear light sweater or full sleeves");
    } else {
      setMessage("Climate: Hot ☀️ | Wear cotton clothes & stay hydrated");
    }
  };

  const handleChange = (e) => {
    const value = e.target.value;
    setTemp(value);
    checkWeather(value);
  };

  return (
    <div className="container">
      <h2>Weather & Clothing Suggestion</h2>

      <input
        type="number"
        placeholder="Enter temperature in Celsius"
        value={temp}
        onChange={handleChange}
      />

      <p className="message">{message}</p>
    </div>
  );
}


export default App;
