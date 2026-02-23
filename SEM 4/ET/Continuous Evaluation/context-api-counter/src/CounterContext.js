import React, { createContext, useEffect, useState } from "react";

/**
 * CounterContext - Creates a React Context for sharing counter state
 * across multiple components without prop drilling.
 * This context will hold the counter value and its setter function.
 */
export const CounterContext = createContext();

/**
 * CounterProvider - A context provider component that manages the counter state
 * and makes it available to all child components.
 */
export function CounterProvider({ children }) {
    // Initialize counter state with useState hook (starts at 0)
    const [count, setCount] = useState(0);

    // useEffect hook to log state changes for debugging purposes
    // Runs whenever the 'count' value changes
    useEffect(() => {
        console.log("Counter updated:", count);
    }, [count]);

    // Provide the counter state and setter function to all child components
    // via Context API's Provider component
    return (
        <CounterContext.Provider value={{ count, setCount }}>
            {children}
        </CounterContext.Provider>
    );
}