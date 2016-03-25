var app = require('http').createServer();
var io = require('socket.io')(app)

var users = [];
var userReadyStates = {};
var idToUser = {};

ball = {
    r: 50,
    x: 0,
    y: 0,
    z: -1280,
    vx: .1,
    vy: .8,
    vz: .1
};

paddle0 = {
    x: 0,
    y: 0,
    z: 0
};

paddle1 = {
    x: 0,
    y: 0,
    z: -2560
};

io.on('connection', function(socket) {
    console.log("User " + socket.id + " has joined.");
    users.push([socket.id]);
    userReadyStates[socket.id] = false;
    socket.emit("AssignId", socket.id, users.length);

    update();

    idToUser[socket.id] = users.length - 1;
            
    socket.on("Ready", function() {
        userReadyStates[socket.id] = true;
        usersReady = true;
        for (var user in userReadyStates) {
            if (userReadyStates.hasOwnProperty(user)) {
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
        // console.log(userNumber + ":" +  data);
        if (userNumber == 0) {
            paddle0.x = 
            io.to(users[1]).emit("OpponentPaddle", data);
        } else {
            io.to(users[0]).emit("OpponentPaddle", data);
        }
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
    performPhysics();
    var gameData = {
       "ballX": ball.x,
       "ballY": ball.y,
       "ballZ": ball.z
    };
    io.emit("BallData", gameData);
    setTimeout(update, 15);
}

var performPhysics = function() {
    if ((ball.z+ball.r == paddle0.z-20 && ball.vz > 0) || (ball.z-ball.r == paddle1.z+20 && ball.vz < 0)) {
        // Reverse direction.
        ball.zVel *= -1.1;
    }
    ball.x += ball.vx;
    ball.y += ball.vy;
    ball.z += ball.vz;
}
