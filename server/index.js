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
    vx: 3,
    vy: 2,
    vz: 5,
    ax: 0,
    ay: 0,
    az: 0
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
    if(((ball.z - ball.r < -2560) && (ball.vz < 0)) || ((ball.z + ball.r > 0) && ball.vz > 0)){
        ball.vz *= -1
    }
    if(((ball.x - ball.r < -640) && (ball.vx < 0)) || ((ball.x + ball.r > 640) && ball.vx > 0)){
        ball.vx *= -1
    }
    if(((ball.y - ball.r < -360) && (ball.vy < 0)) || ((ball.y + ball.r > 360) && ball.vy > 0)){
        ball.vy *= -1
    }
    
    ball.vx += ball.ax
    ball.vy += ball.ay
    ball.vz += ball.az
    ball.vz = Math.round(ball.vz)
    ball.x += ball.vx;
    ball.y += ball.vy;
    ball.z += ball.vz;
}
