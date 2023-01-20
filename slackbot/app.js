var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

// for the slack api
const secrets = require("../secrets/secrets.json")
const { createEventAdapter } = require("@slack/events-api");
const { WebClient } = require("@slack/web-api")
const slackEvents = createEventAdapter("")
const web = new WebClient(secrets.token);

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// slack api
slackEvents.on('message', async (event) => {
    // event hanle
    const result = await web.chat.postMessage({
    text: 'text',
    channel: 'channel',
    });

    console.log(
    `Successfully send message ${result.ts} in conversation ${event.channel}`
    );
}
);

slackEvents.on('error', console.error);

app.use('/slack/events', slackEvents.requestListener());
   // url 유효성 검사를 위한 requestListener


app.use('/', indexRouter);
app.use('/users', usersRouter);

module.exports = app;