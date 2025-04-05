const express = require('express')
const router = express.Router()
const AttendeeForm= require('../models/AttendeeForm');


router.post('/', async (req, res) => {
try {
    const { name , email, phoneNumber, age,sex } = req.body;
    
    const newRequest = new AttendeeForm({ 
      name , email, phoneNumber, age, sex
    });
    
    await newRequest.save();
    
    res.status(201).json({
      message: 'Contact request submitted successfully',
      data: newRequest
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;