ball = {
    r: 50
    x: 0,
    y: 0,
    z: 2560,
    vx: 1,
    vy: .8,
    vz: 2
};

paddle0 = {
    x: 0,
    y: 0,
    z: 0
};

paddle1 = {
    x: 0,
    y: 0,
    z: 2560
};


var update = function() {
    if ((ball.z+ball.r == paddle0.z-20 && ball.vz > 0) || (ball.z-ball.r == paddle1.z+20 && ball.vz < 0)) {
        // Reverse direction.
        ball.zVel *= -1.1;
    }
    ball.x += ball.vx;
    ball.y += ball.vy;
    ball.z += ball.vz;

    // io.emit("BallData", gameData);
    setTimeout(update, 15);
}