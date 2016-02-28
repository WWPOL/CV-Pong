import math
from pyglet.gl import *
def drawCircle(cx, cy, cz, r, num_segments):
	angle = 2 * math.pi / float(num_segments)
	tan = math.tan(angle)
	radial = math.cos(angle)
	x = r
	y = 0
	glBegin(GL_LINE_LOOP)
	for i in range(0, num_segments):
		glVertex3d(x + cx, y + cy, cz)
		tx = -y
		ty = x
		x+=tx*tan
		y+=ty*tan
		x*=radial
		y*=radial
	glEnd()