const express = require("express");
const mongoose = require("mongoose");
const dotenv = require("dotenv");
const bcrypt = require("bcryptjs");
const cors = require("cors");

dotenv.config();

const app = express();
app.use(express.json());
app.use(cors());

// DEBUG: Check if .env loaded
console.log("MONGO_URI:", process.env.MONGO_URI);
console.log("PORT:", process.env.PORT);

mongoose.connect(process.env.MONGO_URI)
    .then(() => console.log("MongoDB connected"))
    .catch(err => console.error("MongoDB connection error:", err));

const userSchema = new mongoose.Schema({ name: String, email: String, password: String });
const User = mongoose.model("User", userSchema);

const taskSchema = new mongoose.Schema({
    title: String,
    description: String,
    dueDate: Date,
    priority: { type: String, enum: ["low", "medium", "high"], default: "medium" },
    status: { type: String, enum: ["not started", "in progress", "completed"], default: "not started" },
    userEmail: String
});
const Task = mongoose.model("Task", taskSchema);

// Register
app.post("/api/register", async (req, res) => {
    const { name, email, password } = req.body;
    const existingUser = await User.findOne({ email });
    if (existingUser) return res.status(400).json({ message: "User already exists" });
    const hashedPassword = await bcrypt.hash(password, 10);
    const user = new User({ name, email, password: hashedPassword });
    await user.save();
    res.json({ message: "User registered successfully" });
});

// Login
app.post("/api/login", async (req, res) => {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    if (!user) return res.status(400).json({ message: "User not found" });
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) return res.status(400).json({ message: "Invalid credentials" });
    res.json({ message: "Login successful" });
});

// Logout
app.get("/api/logout", (req, res) => res.json({ message: "Logout successful" }));

// Create Task
app.post("/api/tasks", async (req, res) => {
    const { title, description, dueDate, priority, status, email } = req.body;
    const task = new Task({ title, description, dueDate, priority, status, userEmail: email });
    await task.save();
    res.json(task);
});

// Get Tasks
app.get("/api/tasks", async (req, res) => {
    const { userEmail } = req.query; // optional filter
    const tasks = userEmail ? await Task.find({ userEmail }) : await Task.find();
    res.json(tasks);
});

// Start server
const PORT = process.env.PORT || 5000;

app.listen(PORT, () => console.log(`Server running at http://localhost:${PORT}`));