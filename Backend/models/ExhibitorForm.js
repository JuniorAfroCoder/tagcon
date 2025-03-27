const mongoose = require("mongoose")

const ExhibitorSchema = new mongoose.Schema({
    name: String,
    email: String,
    companyName: String,
    phoneNumber: String,
    companyDescription: String,
    spaceNeeded: String,
    createdAt: { type: Date, default: Date.now }
}, { collection: 'tagcon_exhibitors' });;

module.exports = mongoose.model('ExhibitorForm', ExhibitorSchema)