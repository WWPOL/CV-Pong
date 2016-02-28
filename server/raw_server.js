var http = require("http");
var url = require('url');


update();

var server = http.createServer(function (req, res) {
	console.log('request received');
	res.end("200");
});

server.listen(8888);
console.log("Listening on port 8888");