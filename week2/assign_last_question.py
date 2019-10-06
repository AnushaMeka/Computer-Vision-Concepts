import cv2

def draw_circle(event,x,y,flags,param):
        
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),5)

img = cv2.imread('/Users/anusha/Desktop/Projects/CV/Computer-Vision-with-Python/DATA/dog_backpack.jpg')

cv2.namedWindow(winname='DogBackpack')

cv2.setMouseCallback('DogBackpack',draw_circle)



while True:
    
    cv2.imshow('DogBackpack',img)
    
    if cv2.waitKey(20) & 0xFF ==27:
        break
        
cv2.destroyAllWindows()