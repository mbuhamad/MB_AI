# Save image in set directory
# Read RGB image
import cv2
img = cv2.imread('paper.png') 
img2 = cv2.imread("bullet.png")
  
# Output img with window name as 'image'
cv2.imshow('image', img) 
cv2.imshow('image', img2) 

  
# Maintain output window utill
# user presses a key
cv2.waitKey(0)        
  
# Destroying present windows on screen
cv2.destroyAllWindows() 