var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var contactSchema = new Schema({
    _id: Schema.Types.ObjectId,
    name: { type: String, required: true },
    contactNumbers: [{ type: Schema.Types.ObjectId, ref: 'ContactNumber' }],
    groups: [{ type: Schema.Types.ObjectId, ref: 'Group' }],
});

var Contact = mongoose.model('Contact', contactSchema);

module.exports = Contact;
