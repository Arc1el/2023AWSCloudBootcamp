var express = require('express');
var router = express.Router();
const axios = require("axios");
require("dotenv").config();

router.get('/', async function(req, res, next) {
  axios.post(process.env.CHANNEL_WEBHOOK_URL, data
  ).then(function () {
    res.send("data successfully sended");
  }).catch(function (e) {
    res.send("error occured", e);
  })
});

function sendMessage(data){
	console.log("Send the Message to Slack api")
	console.log(data)
	title = "*" + data.title + "*"
	location = data.location
	position = data.position
	description = data.description
	fileUrl = "http://server.arc1el.kr:1111/" + data.title + ".ics"
	message = {
		"blocks": [
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*채용공고가 올라왔습니다!*"
				}
			},
			{
				"type": "divider"
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": title
				}
			},
			{
				"type": "section",
				"text": {
					"type": "plain_text",
					"text": location,
					"emoji": true
				}
			},
			{
				"type": "section",
				"text": {
					"type": "plain_text",
					"text": position,
					"emoji": true
				}
			},
			{
				"type": "section",
				"text": {
					"type": "plain_text",
					"text": description,
					"emoji": true
				}
			},
			{
				"type": "divider"
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "📅   캘린더에 추가하기"
				},
				"accessory": {
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Add to Calendar",
						"emoji": true
					},
					"value": "calendar_add_btn",
					"url": fileUrl,
					"action_id": "button-action"
				}
			}
		]
	}
	axios.post(process.env.CHANNEL_WEBHOOK_URL, message
		).then(function () {
		  console.log("data successfully sended");
		}).catch(function (e) {
		  console.log("error occured", e);
	})
}



router.post('/slack/sendMessage', async function(req, res, next) {
	// Request data example
	// { "title" : "title", "startDate" : "20230122T130000", "endDate" : "20230122T150000"} 
	len = req.body.length
	try{
		var file = ""
		for (i=0; i<len; i++) {
			dat = req.body[i]
			var file = axios.post("http://server.arc1el.kr:1111/ics_gen", dat
			).then(function(response) {
				return response.data;
			}).then(sendMessage)
			.catch(function (e) {
				res.send("error occured", e);
			})
		}
		res.sendStatus(200)
	}catch(e){
		console.log(e);
	}finally{
	}
});

router.post('/slack/request', async function(req, res, next) {
	try{
		//console.log(JSON.parse(req.body.payload));
		res.sendStatus(200)
	}catch(e){
		console.log(e)
	}
});

module.exports = router;
