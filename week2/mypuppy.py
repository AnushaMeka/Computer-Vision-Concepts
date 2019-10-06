import cv2

img = cv2.imread('/Users/anusha/Desktop/Projects/CV/Computer-Vision-with-Python/DATA/00-puppy.jpg')

while True:
    # open in a new window of anaconda, when you close that window it gives 1 as       output here
    cv2.imshow('Puppy',img) 
    
    # IF we've waited atleast 1ms AND we've passed the Esc
    # search why 0xFF is used in waitKey() in stack overflow
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()