var express = require('express');
var router = express.Router();
const axios = require("axios");

var data = {
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "📅 캘린더에 추가하기 "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Add to Calendar",
					"emoji": true
				},
				"value": "add_calendar_btn",
				"url": "https://www.phpclasses.org/browse/download/1/file/63438/name/example.ics",
				"action_id": "button-action"
			}
		},
		{
			"type": "divider"
		}
	]
}

router.get('/', async function(req, res, next) {
  axios.post("https://hooks.slack.com/services/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", data
  ).then(function () {
    res.send("data successfully sended");
  }).catch(function () {
    res.send("error occured");
  })
});

module.exports = router;
