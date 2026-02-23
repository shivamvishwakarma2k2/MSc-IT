import React from "react";
import ReactDOM from "react-dom/client";
import reportWebVitals from "./reportWebVitals";
import { ThemeProvider } from "./components/ThemeContext";
import TodoList from "./components/ToDo";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <ThemeProvider>
      <TodoList />
    </ThemeProvider>
  </React.StrictMode>
);

reportWebVitals();