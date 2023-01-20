var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

/*
ICS Generate Router
input data = [
              StartDate(yyyyMMdd'T'HHmmss) : String
              EndDate(yyyyMMdd'T'HHmmss) : String
              Description(ex. AWS Cloud Bootcamp) : String
            ] : JSON format

ex. {
  "StartDate" : "20230120T130000",
  "EndDate" : "20230120T163000",
  "Description" : "AWS CloudBootCamp OfflineSession"
}

outputdata = .ics file -> save to local storage
*/
router.get('/ics_gen', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


module.exports = router;
