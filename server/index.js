var app = require('http').createServer();
var io = require('socket.io')(app)

var users = [];
var userstates = {};
var idToUser = {};

var paddle1;
var paddle2;
var ball;

io.on('connection', function(socket) {
    console.log("User " + socket.id + " has joined.");
    users.push([socket.id]);
    userstates[socket.id] = false;
    socket.emit("AssignId", socket.id, users.length);
    update();

    idToUser[socket.id] = users.length;
            
    socket.on("Ready", function() {
        userstates[socket.id] = true;
        usersReady = true;
        for (var user in userstates) {
          if (userstates.hasOwnProperty(user)) {
            if (user === false) {
                usersReady = false;
            }
          }
        }
        if (usersReady) {
            socket.emit("StartGame")
        }
    });

    socket.on("UpdatePaddle", function(data) {
        userNumber = idToUser[socket.id];
        
        // Fuck my life.
        io.to(users[(idToUser[socket.id] - 1 % 2)].emit("OpponentPaddle", data);
    });

    socket.on("disconnect", function() {
        console.log("User " + socket.id + " left.");
        users.splice(users.indexOf(socket.id), 1);
        // end gamex
    });
});

app.listen((process.env.PORT || 8888), function() {
    console.log("Listening for connections on port 8888.");
});

var update = function() {
    var gameData = {
        ballX: ball.x,
        ballY: ball.y,
        ballZ: ball.z
    };

    io.emit("BallData", gameData);
    setTimeout(update, 15);
}

var performPhysics = function(data) {
    console.log("Beginning physics pass..."); 
    ball.x += ball.xVel;
    ball.y += ball.yVel;
    ball.z += ball.zVel;

    if (ball.z == paddle0.z || ball.z == paddle1.z) {
        // Reverse direction.
        ball.zVel *= -1;
    }
}
