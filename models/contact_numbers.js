var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var contactNumberSchema = new Schema({
    number: { type: Number, required: true },
    contact: [{ type: Schema.Types.ObjectId, ref: 'Contact' }]
});

var ContactNumber = mongoose.model('ContactNumber', contactNumberSchema);

module.exports = ContactNumber;
