import math
from pyglet.gl import *
def draw_circle(cx, cy, cz, r, num_segments):
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

def graphics_render():
	glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0,0,-5)
    drawCircle(0,0,0,1,30)
    drawCircle(4,0,-3,1,30)