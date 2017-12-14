var express = require('express');
var router = express.Router();

var Group = require('../../models/groups.js');

router.get('/', function(req, res, next) {
    Group.findAsync()
    .then(function(groups) {
        res.send(groups);
    })
    .catch(next)
    .error(console.error);
});

router.post('/', function(req, res, next) {
    var group = new Group({
        _id: new mongoose.Types.ObjectId(),
        name: req.body.name
    });
    group.saveAsync()
    .then(function(group) {
        res.send(group);
    })
    .catch(next)
    .error(console.error);
});

router.get('/:id', function(req, res, next) {
    Group.findOneAsync({ _id: req.params.id })
    .then(function(group) {
        res.send(group);
    })
    .catch(next)
    .error(console.error);
});

router.put('/:id', function(req, res, next) {
    Group.updateAsync({ _id: req.params.id }, req.body)
    .then(function(group) {
        res.send(group);
    })
    .catch(next)
    .error(console.error);
});

router.delete('/:id', function(req, res, next) {
    Group.findByIdAndRemoveAsync(req.params.id)
    .then(function(group) {
        res.send(group);
    })
    .catch(next)
    .error(console.error);
});

module.exports = router;
