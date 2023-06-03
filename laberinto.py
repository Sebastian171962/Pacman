import numpy as np
import cv2

# Define the colors of the map
BLACK = (0, 0, 0)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)

# Create the map as a numpy array
map = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw the walls of the map
cv2.rectangle(map, (0, 0), (400, 20), BLUE, -1)
cv2.rectangle(map, (0, 380), (400, 400), BLUE, -1)
cv2.rectangle(map, (0, 0), (20, 400), BLUE, -1)
cv2.rectangle(map, (380, 0), (400, 400), BLUE, -1)
cv2.rectangle(map, (100, 0), (120, 300), BLUE, -1)
cv2.rectangle(map, (280, 100), (300, 400), BLUE, -1)

# Draw the pellets on the map
#for i in range(40, 361, 40):
    #for j in range(40, 361, 40):
        #cv2.circle(map, (i, j), 3, YELLOW, -1)

# Show the map
cv2.imshow('Pacman Map', map)
cv2.waitKey(0)
cv2.destroyAllWindows()
