const mongoose = require('mongoose')

const VolunteerSchema = new mongoose.Schema ({
   name: String,
    email: String,
    phoneNumber: String,
    age: Number,
    sex: { type: String, default:'sex', enum: ['male', 'female']},
    createdAt: { type: Date, default: Date.now }
}, { collection: 'tagcon_volunteers' });;

module.exports = mongoose.model('VolunteerForm', VolunteerSchema)