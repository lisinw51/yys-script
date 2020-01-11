import getImg as GI
import compare as CP
import mouseclick as MC
import math
import time
import random
def startcg():
    GI.getImg(1350,710,1490,855)
    similar =  CP.compare('./temp.png','./cg.png')
    if similar>0.9:
        print('cgicom match,start yuhun')
        MC.click(1350,710,1490,855)
        return True
def endcg():
    GI.getImg(900,660,1010,750)
    similar =  CP.compare('./temp.png','./cgend.png')
    if similar>0.5:
        print('cgicom match,end yuhun')
        MC.click(900,660,1010,750)
        return True
if __name__ == "__main__":
    while True:
        if startcg() == True:
            time.sleep(30)
        else:
            endcg()
            time.sleep(1)