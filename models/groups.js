var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var groupSchema = new Schema({
    _id: Schema.Types.ObjectId,
    name: { type: String, required: true },
    contacts: [{ type: Schema.Types.ObjectId, ref: 'Contact' }]
});

var Group = mongoose.model('Group', groupSchema);

module.exports = Group;
