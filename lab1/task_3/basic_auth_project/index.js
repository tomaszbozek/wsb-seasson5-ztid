// Required modules
const express = require("express");
var path = require('path');

const app = express();

function authentication(req, res, next) {
    var authheader = req.headers.authorization;
    console.log(req.headers);

    if (!authheader) {
        var err = new Error('You are not authenticated!');
        res.setHeader('WWW-Authenticate', 'Basic');
        err.status = 401;
        return next(err)
    }

    var auth = new Buffer.from(authheader.split(' ')[1], 'base64').toString().split(':');
    var user = auth[0];
    var pass = auth[1];

    if (user == '' && pass == '') {
        // If user is authenticated then next but do not understand what next does?
        next();
    } else {
        var err = new Error('You are not authenticated!');
        res.setHeader('WWW-Authenticate', 'Basic');
        err.status = 401;
        return next(err);
    }

}

// First step is the authentication of the client
app.use(authentication)
app.use(express.static(path.join(__dirname, 'public')));

// Server setup
app.listen((4000), () => {
    console.log("Server is Running very well");
})
