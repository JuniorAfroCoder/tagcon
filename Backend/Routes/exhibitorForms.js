const express = require('express')
const router = express.Router()
const ExhibitorForm = require('../models/ExhibitorForm')

router.post('/', async (req, res) => {
try {
    const { name , email, companyName, phoneNumber, companyDescription, spaceNeeded } = req.body;
    
    const newRequest = new ExhibitorForm({ 
      name , email, companyName, phoneNumber, companyDescription, spaceNeeded
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
