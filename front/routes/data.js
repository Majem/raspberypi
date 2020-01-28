var express = require('express');
var router = express.Router();
var request = require('request');



/* GET users listing. */
router.get('/', function(req, res, next) {
  request({
    url: 'https://smartdom20200125032822.azurewebsites.net/api/temperatura?code=MmL13kZm9eOHjZjEsfn2KN5L4iQErBlT5MM7CjUa7apqjOiOZIcyOQ==',
    json: true
  }, function (error, response, body) {

    if (!error && response.statusCode === 200) {
      res.json(body);
    }
  })
});

module.exports = router;
