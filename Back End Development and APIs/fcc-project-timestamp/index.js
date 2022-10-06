// index.js
// where your node app starts

// init project
var express = require("express");
var app = express();

// enable CORS (https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
// so that your API is remotely testable by FCC
var cors = require("cors");
app.use(cors({ optionsSuccessStatus: 200 })); // some legacy browsers choke on 204

// http://expressjs.com/en/starter/static-files.html
app.use(express.static("public"));

// http://expressjs.com/en/starter/basic-routing.html
app.get("/", function (req, res) {
  res.sendFile(__dirname + "/views/index.html");
});

// your first API endpoint...
app.get("/api/hello", function (req, res) {
  res.json({ greeting: "hello API" });
});
app.get("/api", function (req, res) {
  let date = new Date();
  let utc = date.toUTCString();
  const timestampInMs = date.getTime();

  // 👇️ timestamp in seconds (Unix timestamp)
  // const unix = Math.floor(date.getTime() / 1000);
  res.json({ unix: timestampInMs, utc });
});
//parse date
app.get("/api/:date", function (req, res) {
  let dateInput = req.params.date;

  let unix = Date.parse(dateInput);
  if (dateInput.trim() == "") {
    unix = Date.now();
  } else if (!unix) {
    unix = parseInt(dateInput);
  }
  let date = new Date(unix);
  let utc = date.toUTCString();
  if (utc == "Invalid Date") {
    res.json({ error: utc });
  } else {
    res.json({ unix, utc });
  }
});

// listen for requests :)
var listener = app.listen(process.env.PORT || 3000, function () {
  console.log("Your app is listening on port " + listener.address().port);
});
