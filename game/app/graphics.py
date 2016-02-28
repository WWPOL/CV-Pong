import math
import pyglet
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
    glTranslatef(0,0,-565)
    draw_circle(0,0,0,1,30)
    draw_circle(4,0,-3,1,30)

def graphics_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65, width / float(height), .1, 1000)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED