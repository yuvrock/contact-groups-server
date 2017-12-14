var express = require('express');
var router = express.Router();

var contacts = require('./apis/contacts.js');
var groups = require('./apis/groups.js');

router.use('/contacts', contacts);
router.use('/groups', groups);

module.exports = router;