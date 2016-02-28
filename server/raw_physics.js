
ball = {
	r: 50
	x: 0,
	y: 0,
	z: 0,
	vx: 0,
	vy: 0,
	vz: 0
};

paddle1 = {
	x: 0,
	y: 0
};

paddle2 = {
	x: 0,
	y: 0
};


var update = function() {
    performPhysics();

    ball.x += ball.vx;
    ball.y += ball.vy;
    ball.z += ball.vz;

    // io.emit("BallData", gameData);
    setTimeout(update, 15);
}

var performPhysics = function() {
    console.log("Beginning physics pass..."); 
    // ball.x += ball.xVel;
    // ball.y += ball.yVel;
    // ball.z += ball.zVel;

    if (ball.z == paddle0.z || ball.z == paddle1.z) {
        // Reverse direction.
        ball.zVel *= -1;
    }
}