var express = require('express');
var router = express.Router();
const axios = require("axios");

require("dotenv").config();
const webhook = process.env["CHANNEL_WEBHOOK_URL"]

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
				"url": "http://server.arc1el.kr:1111/AWS.ics",
				"action_id": "button-action"
			}
		},
		{
			"type": "divider"
		}
	]
}

router.get('/', async function(req, res, next) {
  axios.post(webhook, data
  ).then(function () {
    res.send("data successfully sended");
  }).catch(function (e) {
    res.send(e);
  })
});

module.exports = router;
