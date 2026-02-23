import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

// Get the root DOM element (typically <div id="root"></div> in index.html)
// and create a React root container for React 18+ concurrent rendering
const root = ReactDOM.createRoot(document.getElementById("root"));

// Render the App component into the root container
// This starts the React application and renders all components
root.render(<App />);
