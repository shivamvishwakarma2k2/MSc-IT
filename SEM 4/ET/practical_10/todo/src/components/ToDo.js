import { useState } from "react";
import "./ToDo.css";
import { useTheme } from "./ThemeContext";
import ToDoItem from "./ToDoItem";

// Parent Component
export default function TodoList() {
    const { darkMode, toggleTheme } = useTheme();
    const [tasks, setTasks] = useState([]);
    const [task, setTask] = useState("");

    const addTask = () => {
        if (task.trim() !== "") {
            setTasks([...tasks, task]);
            setTask("");
        }
    };

    const removeTask = (index) => {
        setTasks(tasks.filter((_, i) => i !== index));
    };

    return (
        <div className={darkMode ? "container dark" : "container light"}>

            <button onClick={toggleTheme} className="toggle-btn">
                {darkMode ? "Switch to Light Mode" : "Switch to Dark Mode"}
            </button>

            <div className="todo-card">
                <h2>To-Do List</h2>

                <div className="input-container">
                    <input
                        type="text"
                        value={task}
                        onChange={(e) => setTask(e.target.value)}
                        placeholder="Add a task..."
                    />
                    <button onClick={addTask}>Add</button>
                </div>

                <ul>
                    {tasks.map((t, index) => (
                        <ToDoItem
                            key={index}
                            task={t}
                            removeTask={() => removeTask(index)}
                        />
                    ))}
                </ul>
            </div>
        </div>
    );
}
