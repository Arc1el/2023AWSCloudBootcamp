var express = require('express');
var router = express.Router();
const fs = require('fs/promises');

// ICS file generate function
// Parameter : title, startDate, endDate
// Result : Generate ICS file
async function generateIcs(title, startDate, endDate, receivedData) {
  try {
    const content = "BEGIN:VCALENDAR\r\n"
                  + "VERSION:2.0\r\n"
                  + "CALSCALE:GREGORIAN\r\n"
                  + "BEGIN:VEVENT\r\n"
                  + "DTSTART:" + startDate + "\r\n"
                  + "DTEND:" + endDate + "\r\n"
                  + "SUMMARY:" + title + "\r\n"
                  + "END:VEVENT"
    const filename = "./generatedFiles/" + title + ".ics"
    await fs.writeFile(filename, content);
    return receivedData;
  } catch (err) {
    console.log(err);
  }
}

/*
ICS Generate Router
input data = {
              startDate(yyyyMMdd'T'HHmmss) : String
              endDate(yyyyMMdd'T'HHmmss) : String
              title(ex. AWS Cloud Bootcamp) : String
            } : JSON format

ex. {
  "startDate" : "20230120T130000",
  "endDate" : "20230120T163000",
  "title" : "AWS CloudBootCamp OfflineSession"
}

outputdata : .ics file -> save to local storage
response : send the generated ics filename
*/

router.post('/ics_gen', async function(req, res, next) {
  // Define the data from request
  const receivedData = req.body;
  const title = receivedData.title;
  const startDate = receivedData.startDate;
  const endDate = receivedData.endDate;

  // Create the ICS file
  const filename = await generateIcs(title, startDate, endDate, receivedData);
  console.log(filename + " is generated.\r\n");

  // Send the Response with filename
  res.send(filename);
});

module.exports = router;
