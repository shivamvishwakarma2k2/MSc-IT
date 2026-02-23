import React, { useContext, useEffect } from "react";
import { CounterContext } from "./CounterContext";

/**
 * CounterDisplay - Component that displays the current counter value
 * Uses the CounterContext to access the counter state and render it.
 */
function CounterDisplay() {
    // Extract count value from CounterContext using useContext hook
    // This component will automatically re-render whenever count changes
    const { count } = useContext(CounterContext);

    // useEffect hook to log component lifecycle events
    // Empty dependency array [] means this effect runs only once on mount
    // The cleanup function runs when the component unmounts
    useEffect(() => {
        console.log("CounterDisplay mounted");

        // Cleanup function: runs when component is removed from DOM
        return () => {
            console.log("CounterDisplay unmounted");
        };
    }, []);

    // Render the current counter value
    // Component automatically updates when count changes in context
    return <h2>Counter Value: {count}</h2>;
}

export default CounterDisplay;
