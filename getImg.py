import time
import numpy as np
from PIL import ImageGrab

def getImg(x1,y1,x2,y2):
    img = ImageGrab.grab((x1,y1,x2,y2))
    #img = ImageGrab.grab(bbox=(950,315, 50, 60))
    # img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
    img.save('F:\\python-learn\\temp.png')
    #print('print success,named temp.png')
    #img.show()
