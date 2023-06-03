import cv2
import numpy as np


# initialize game window
canvas = np.zeros((500, 500, 3), dtype=np.uint8)
canvas.fill(0)

# set colors
black = (0, 0, 0)
yellow = (0, 255, 255)
pink = (255, 192, 203)
blue = (255, 0, 0)
green = (0, 128, 0)

# initialize Pacman
pacman_x_pos = 250
pacman_y_pos = 250
pacman_radius = 20
pacman_angle_start = 30
pacman_angle_end = 330
pacman_direction = "right"

while True:
    # draw Pacman
    cv2.ellipse(canvas, (pacman_x_pos, pacman_y_pos), (pacman_radius, pacman_radius),
                0, pacman_angle_start, pacman_angle_end, yellow, -1)

    # update Pacman direction and position
    if cv2.waitKey(1) & 0xFF == ord('w'):
        pacman_direction = "up"
        pacman_y_pos -= 10
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        pacman_direction = "down"
        pacman_y_pos += 10
    elif cv2.waitKey(1) & 0xFF == ord('a'):
        pacman_direction = "left"
        pacman_x_pos -= 10
    elif cv2.waitKey(1) & 0xFF == ord('d'):
        pacman_direction = "right"
        pacman_x_pos += 10

    # show image
    cv2.imshow("Pacman Game", canvas)

    # quit game
    if cv2.waitKey(1) == 27:
        break

    # Clear image for next frame
    img = np.zeros((500, 500, 3), np.uint8)
cv2.destroyAllWindows()
