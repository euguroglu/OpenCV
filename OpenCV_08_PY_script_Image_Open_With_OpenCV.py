import cv2
img = cv2.imread('C:/Users/eugur/Downloads/Jupyter_lab/Computer-Vision-with-Python/DATA/00-puppy.jpg')


while True:
    cv2.imshow('Puppy',img)
    
    # if we have waited at least 1 ms AND we ve pressed the escepace key
    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()