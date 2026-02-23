import "./ToDo.css";  

export default function ToDoItem({ task, removeTask }) {
  return (
    <li className="task-item">
      {task}
      <button onClick={removeTask} className="delete-btn">
        ❌
      </button>
    </li>
  );
}