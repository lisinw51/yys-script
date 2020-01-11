from pymouse import PyMouse
import random
def click(x1,y1,x2,y2):
    rad = random.randint(-9,9)
    m = PyMouse()
    m.click((x1+x2)/2+rad,(y1+y2)/2+rad)