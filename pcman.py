import cv2
import numpy as np

# Initialize image
img = np.zeros((400, 400, 3), np.uint8)
img[:] = (0, 0, 0) #set background color to white

#set variables
circle_center = (200, 200)
triangle_height = 60
triangle_width = 30
mouth_open = False

while True:
    # Draw circle
    cv2.circle(img, circle_center, 50, (0, 255, 255), -1)
    
    # Draw triangle
    x1 = circle_center[0] - int(triangle_width/2)
    x2 = circle_center[0] + int(triangle_width/2)
    y = circle_center[1] + int(triangle_height)
   
    pts = np.array([[x1,y],[x2,y],[circle_center[0], circle_center[1]]], np.int32)
    cv2.fillPoly(img, [pts], (0,0,0))
   
    # Increase or decrease triangle base width
    if mouth_open:
        triangle_width += 10
    else:
        triangle_width -= 10
       
    # Reverse direction when reaching max or min width
    if triangle_width == 100:
        mouth_open = False
    elif triangle_width == 10:
        mouth_open = True
   
    # Display image and wait for key press
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27: #exit if ESC key pressed
        break

# Clean up and exit
cv2.destroyAllWindows()