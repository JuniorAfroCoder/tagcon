const mongoose = require('mongoose')

const AttendeeSchema= new mongoose.Schema({
    name: String,
    email: String,
    phoneNumber: String,
    age: Number,
    sex: { type: String, default:'sex', enum: ['male', 'female']},
    createdAt: { type: Date, default: Date.now },
}, { collection : 'tagcon_attendees'});

module.exports = mongoose.model('AttendeeForm', AttendeeSchema)