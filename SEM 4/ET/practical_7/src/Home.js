import React, { useContext } from "react";
import { ThemeContext } from "./ThemeContext";

const Home = () => {
    const { theme, toggleTheme } = useContext(ThemeContext);

    const styles = {
        container: {
            minHeight: "100vh", // Full viewport height
            display: "flex",
            flexDirection: "column", // Stack content vertically
            justifyContent: "center",
            alignItems: "center",
            padding: "16px",
            fontFamily: "Arial, sans-serif",
            transition: "all 0.3s ease",
            backgroundColor: theme === "light" ? "#f5f5f5" : "#222",
            color: theme === "light" ? "#222" : "#f5f5f5"
        },
        button: {
            marginTop: "16px",
            padding: "8px 14px",
            border: "none",
            borderRadius: "4px",
            cursor: "pointer",
            backgroundColor: theme === "light" ? "#222" : "#f5f5f5",
            color: theme === "light" ? "#fff" : "#222",
            fontSize: "16px"
        }
    };

    return (
        <div style={styles.container}>
            <h1>{theme === "light" ? "Light Mode ☀️" : "Dark Mode 🌙"}</h1>
            <p>Current theme: {theme}</p>
            <button style={styles.button} onClick={toggleTheme}>
                Toggle Theme
            </button>
        </div>
    );
};

export default Home;