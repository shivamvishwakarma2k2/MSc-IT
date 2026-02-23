import React, { useContext, useEffect } from "react";
import { CounterContext } from "./CounterContext";

/**
 * CounterButtons - Component that provides UI controls to increment the counter
 * Uses the CounterContext to access and update the counter state.
 */
function CounterButtons() {
    // Extract setCount function from CounterContext using useContext hook
    // This allows us to update the counter state without prop drilling
    const { setCount } = useContext(CounterContext);

    // useEffect hook to log component lifecycle events
    // Empty dependency array [] means this effect runs only once on mount
    // The cleanup function runs when the component unmounts
    useEffect(() => {
        console.log("CounterButtons mounted");

        // Cleanup function: runs when component is removed from DOM
        return () => {
            console.log("CounterButtons unmounted");
        };
    }, []);

    // Render button that increments counter on click
    // Uses functional update form (prev => prev + 1) to ensure correct state updates
    return (
        <button onClick={() => setCount(prev => prev + 1)}>
            Increase Counter
        </button>
    );
}

export default CounterButtons;
