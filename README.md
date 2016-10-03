# PROJECT: FIELD PONY (aka CV-Pong)

**1st Place Creation at MIT Blueprint 2016!**

##Instructions

Your goal is to move your hand to control your paddle and beat your opponent. Before playing, make sure to sample your hand (preferably inside a brightly colored glove) by clicking on different parts of it using your mouse. The detection threshold used to calculate your paddle's location will be shown by a yellow outline and red dot. The game is played in 3D, therefore your paddle can be moved in 2 dimensions instead of just one.

Requires OpenCV 2.4 or 3 and Pyglet 1.

[ **Game demo video**](http://i.imgur.com/fIPxxGI.gif)

![Game demo still picture](http://i.imgur.com/mkMdFDX.png)

##Technical Details
We used the OpenCV computer vision library to implement hand control via webcam. The program uses the sampled points the user provides to generate multiple threshold masks, which are then merged into one large mask, which is more resilient to adverse lighting conditions. The centroid of the largest contour of the mask is used as the paddle position. The multiple thresholds allow for robust object detection despite webcam noise and suboptimal lighting conditions.
