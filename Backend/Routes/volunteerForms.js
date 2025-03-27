const express = require('express')
const router = express.Router()
const VolunteerForm = require('../models/Volunteerform')

router.post('/', async (req, res) => {
try {
    const { name , email, phoneNumber, age,  sex} = req.body;
    
    const newRequest = new VolunteerForm({ 
      name , email, phoneNumber, age, sex
    });
    
    await newRequest.save();
    
    res.status(201).json({
      message: ' Volunteer Registration Form submitted successfully',
      data: newRequest
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;