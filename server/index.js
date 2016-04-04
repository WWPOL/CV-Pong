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
    vx: 0,
    vy: 0,
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
        unpackedData = JSON.parse(data)
        if (userNumber == 0) {
            paddle0.x = unpackedData["x"]
            paddle0.y = unpackedData["y"]
            io.to(users[1]).emit("OpponentPaddle", data);
        } else {
            paddle1.x = unpackedData["x"]
            paddle1.y = unpackedData["y"]
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
    checkCollisionWithWalls()
    checkCollisionWithPaddle(ball, paddle0, 0)
    checkCollisionWithPaddle(ball, paddle1, 1)
    updateVelocity()
    updatePosition()
}

var checkCollisionWithWalls = function(){
    if(((ball.z - ball.r < -2560) && (ball.vz < 0)) || ((ball.z + ball.r > 0) && ball.vz > 0)){
        ball.x = 0
        ball.y = 0
        ball.z = -1280
        ball.vz = 5
    }
    if(((ball.x - ball.r < -640) && (ball.vx < 0)) || ((ball.x + ball.r > 640) && ball.vx > 0)){
        ball.vx *= -1
    }
    if(((ball.y - ball.r < -360) && (ball.vy < 0)) || ((ball.y + ball.r > 360) && ball.vy > 0)){
        ball.vy *= -1
    }
}

var checkCollisionWithPaddle = function(ball, colPaddle, playerNum){
    // var x = Math.max((colPaddle.x - 100), Math.min((ball.x, colPaddle.x+100)))
    // var y = Math.max((colPaddle.y - 50), Math.min((ball.y, colPaddle.y+50)))
    // if(playerNum == 0){
    //     var z = Math.max(colPaddle.z-20, Math.min((ball.z), colPaddle.z))
    // }else if(playerNum == 1){
    //     var z = Math.max(colPaddle.z, Math.min((ball.z), colPaddle.z+20))
    // }
    // var distance = Math.sqrt((x - ball.x) * (x - ball.x) +(y - ball.y) * (y - ball.y) +(z - ball.z) * (z - ball.z))
    // console.log(distance)
    // if(distance < ball.r){
    //     ball.vz *= -1
    //     //console.log("Collision!")
    // }
    if(ball.x > colPaddle.x - 100 && ball.x < colPaddle.x + 100 && ball.y > colPaddle.y - 50 && ball.y < colPaddle.y + 50){
        if(playerNum == 0 && ball.z + ball.r > colPaddle.z - 20 && ball.vz > 0){
            ball.vz *= -1
            console.log("Collision")
        }
        if(playerNum == 1 && ball.z - ball.r < colPaddle.z + 20 && ball.vz < 0){
            ball.vz *= -1
            console.log("Collision")
        }
    }
}

var updateVelocity = function(){
    ball.vx += ball.ax
    ball.vy += ball.ay
    ball.vz += ball.az
    ball.vz = Math.round(ball.vz)
}

var updatePosition = function(){
    ball.x += ball.vx;
    ball.y += ball.vy;
    ball.z += ball.vz;
}