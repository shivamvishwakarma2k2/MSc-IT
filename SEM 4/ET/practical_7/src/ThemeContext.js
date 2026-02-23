import React, { createContext, useState } from "react";

// Create Context
export const ThemeContext = createContext();

// Provider Component
const ThemeProvider = ({ children }) => {
    const [theme, setTheme] = useState("light");

    // Toggle Function
    const toggleTheme = () => {
        setTheme(prevTheme => (prevTheme === "light" ? "dark" : "light"));
    };

    return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}>
            {children}
        </ThemeContext.Provider>
    );
};

export default ThemeProvider;