var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


/*
ICS Generate Router
input data = [
StartDate(yyyyMMdd'T'HHmmss)
EndDate(yyyyMMdd'T'HHmmss)
Description(ex. AWS Cloud Bootcamp)
*/
router.get('/ics_gen', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


module.exports = router;
