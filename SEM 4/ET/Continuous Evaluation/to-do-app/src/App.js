// Import useState hook from React
import { useState } from 'react';

// Main App component
function App() {

  // State to store list of tasks (initially empty)
  const [tasks, setTasks] = useState([]);

  // State to store input value from textbox
  const [input, setInput] = useState('');

  // JSX returned by the component
  return (
    <div>

      {/* App title */}
      <h2>Todo App - 6709</h2>

      {/* Input box to enter new task */}
      <input
        value={input}                     // Bind input value to state
        onChange={(e) =>                 // Trigger when user types
          setInput(e.target.value)       // Update input state
        }
        placeholder="Enter a new task"   // Placeholder text
      />

      {/* Button to add task */}
      <button
        onClick={() => {
          if (input) {                   // Check input is not empty
            setTasks([...tasks, input]); // Add new task to task list
            setInput('');                // Clear input box
          }
        }}
      >
        Add
      </button>

      {/* Display all tasks */}
      <div>
        {tasks.map((task, i) => (         // Loop through task array
          <div key={i}>                  {/* Unique key for each task */}
            
            {task}                       {/* Display task text */}

            {/* Delete button */}
            <button
              onClick={() =>
                setTasks(
                  tasks.filter((_, idx) => idx !== i)
                )                         // Remove selected task
              }
            >
              Delete
            </button>

          </div>
        ))}
      </div>

    </div>
  );
}

// Export App component
export default App;