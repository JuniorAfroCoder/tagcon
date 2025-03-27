require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const ExhibitorSubmission = require('./Routes/exhibitorForms')
const VolunteerSubmission = require("./Routes/volunteerForms")
const rateLimit = require('express-rate-limit');
const slowDown = require('express-slow-down');



const app = express();
const PORT = process.env.PORT || 5000;
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per window
  message: 'Too many requests from this IP, please try again later',
  standardHeaders: true, // Return rate limit info in headers
  legacyHeaders: false,
});
const speedLimiter = slowDown({
  windowMs: 15 * 60 * 1000, // 15 minutes
  delayAfter: 50, // Allow 50 requests per window
  delayMs: 500 // Begin adding 500ms delay per request above 50
});

// Configure CORS
const corsOptions = {
  origin: [
    'https://tagconvention.netlify.app',  // Your Render frontend URL
    'http://localhost:5173',               // For local development
  ],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],  // Allowed HTTP methods
  allowedHeaders: ['Content-Type', 'Authorization'],  // Allowed headers
};

// Middlewares
app.use(cors());
app.use(express.json()); // Parse JSON requests
app.use('/api/', apiLimiter);
app.use(speedLimiter);
app.use(cors(corsOptions));

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log("MongoDB Connected"))
    .catch(err => console.error(err));


app.use('/api/submit-exhibitor-form', ExhibitorSubmission)
app.use('/api/submit-volunteer-form', VolunteerSubmission)




app.listen(PORT, () => console.log(`Server running on port ${PORT}`));