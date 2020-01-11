from skimage.measure import compare_ssim
import cv2

def compare(imgsrc1,imgsrc2):

    imageA = cv2.imread(imgsrc1)
    imageB = cv2.imread(imgsrc2)
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    #print("SSIM: {}".format(score))
    #print(format(score))
    #print(score)
    return score