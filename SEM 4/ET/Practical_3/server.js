const express = require("express");
const fs = require("fs");
const path = require("path");
const multer = require("multer");
const events = require("events");

// Initialize express app and event emitter
const app = express();
const eventEmitter = new events.EventEmitter();
const port = 3000;

// Create 'logAnalysis' directory if it doesn't exist
const logDir = path.join(__dirname, "logAnalysis");
if (!fs.existsSync(logDir)) {
    fs.mkdirSync(logDir);
}

// Configure multer for file upload
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, logDir);
    },
    filename: (req, file, cb) => {
        const timestamp = Date.now();
        cb(null, `log_${timestamp}.log`);
    }
});

const upload = multer({ storage });

// Function to analyze log file
function analyzeLogFile(filePath) {
    const logData = fs.readFileSync(filePath, "utf-8");

    let infoCount = 0,
        debugCount = 0,
        errorCount = 0;

    // Count log levels
    infoCount = (logData.match(/\[INFO\]/g) || []).length;
    debugCount = (logData.match(/\[DEBUG\]/g) || []).length;
    errorCount = (logData.match(/\[ERROR\]/g) || []).length;

    // Display results
    console.log(`Total "INFO" events  - ${infoCount}`);
    console.log(`Total "DEBUG" events - ${debugCount}`);
    console.log(`Total "ERROR" events - ${errorCount}`);

    // Emit event to notify completion
    eventEmitter.emit("logAnalysisCompleted");
}

// Event listener
eventEmitter.on("logAnalysisCompleted", () => {
    console.log("Log analysis is completed!");
});

// Serve static index.html file
app.use(express.static(path.join(__dirname, "public")));

// File upload endpoint
app.post("/upload", upload.single("logFile"), (req, res) => {
    const file = req.file;

    // validate file type
    if (file && path.extname(file.originalname) === ".log") {

        // Analyze the uploaded file
        analyzeLogFile(file.path);

        res.status(200).send("File uploaded and analysis is in progress!");
    } else {
        res.status(400).send("Invalid file type. Only .log files are allowed.");
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});