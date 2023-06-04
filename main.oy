import cv2
import numpy as np
import time

# Define the colors of the map
BLACK = (0, 0, 0)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)
RED = (0, 0, 255)
WHITE = (255, 255, 255)  

# Create the game window
canvas = np.zeros((500, 500, 3), dtype=np.uint8)
canvas.fill(0)

# Set variables for Pacman
circle_center = (250, 250)
triangle_height = 60
triangle_width = 30
mouth_open = False

# Set initial position and direction for Pacman
pacman_x_pos = 250
pacman_y_pos = 250
pacman_radius =20
pacman_direction = "right"

# Create a list to store the positions of the pellets
pellet_positions = []

# Create a list to store the positions of the ghost
ghost_positions = []

# Set variables for the ghost
ghost_x_pos = 250
ghost_y_pos = 250
ghost_radius = 15

# Flag to determine if the ghost should appear
show_ghost = False

# Flag to determine if the ghost has caught Pacman
game_over = False

# Start time to delay the appearance of the ghost
start_time = time.time()

# Draw the maze walls and pellets
cv2.rectangle(canvas, (40, 40), (460, 60), BLUE, -1)
cv2.rectangle(canvas, (40, 440), (460, 460), BLUE, -1)
cv2.rectangle(canvas, (40, 40), (60, 200), BLUE, -1)
cv2.rectangle(canvas, (40, 320), (60, 460), BLUE, -1)
cv2.rectangle(canvas, (440, 40), (460, 200), BLUE, -1)
cv2.rectangle(canvas, (440, 320), (460, 460), BLUE, -1)
cv2.rectangle(canvas, (160, 40), (340, 60), BLUE, -1)
cv2.rectangle(canvas, (160, 440), (340, 460), BLUE, -1)
cv2.rectangle(canvas, (160, 200), (200, 240), BLUE, -1)
cv2.rectangle(canvas, (300, 200), (340, 240), BLUE, -1)
cv2.rectangle(canvas, (160, 320), (200, 360), BLUE, -1)
cv2.rectangle(canvas, (300, 320), (340, 360), BLUE, -1)

# Add the pellets to the maze
for i in range(60, 441, 40):
    for j in range(60, 441, 40):
        cv2.circle(canvas, (i, j), 3, YELLOW, -1)
        pellet_positions.append((i, j))

while True:
    # Update the canvas image
    canvas = np.zeros((500, 500, 3), dtype=np.uint8)
    canvas.fill(0)

    # Draw the maze walls and remaining pellets
    cv2.rectangle(canvas, (40, 40), (460, 60), BLUE, -1)
    cv2.rectangle(canvas, (40, 440), (460, 460), BLUE, -1)
    cv2.rectangle(canvas, (40, 40), (60, 200), BLUE, -1)
    cv2.rectangle(canvas, (40, 320), (60, 460), BLUE, -1)
    cv2.rectangle(canvas, (440, 40), (460, 200), BLUE, -1)
    cv2.rectangle(canvas, (440, 320), (460, 460), BLUE, -1)
    cv2.rectangle(canvas, (160, 40), (340, 60), BLUE, -1)
    cv2.rectangle(canvas, (160, 440), (340, 460), BLUE, -1)
    cv2.rectangle(canvas, (160, 200), (200, 240), BLUE, -1)
    cv2.rectangle(canvas, (300, 200), (340, 240), BLUE, -1)
    cv2.rectangle(canvas, (160, 320), (200, 360), BLUE, -1)
    cv2.rectangle(canvas, (300, 320), (340, 360), BLUE, -1)

    # Draw the remaining pellets
    for pellet_pos in pellet_positions:
        cv2.circle(canvas, pellet_pos, 3, YELLOW, -1)

    # Update Pacman direction and position
    key = cv2.waitKey(100)  # Delay of 100 milliseconds

    # Check if Pacman has collided with a pellet
    pellet_index = None
    for i, (pellet_x, pellet_y) in enumerate(pellet_positions):
        if pellet_x == pacman_x_pos and pellet_y == pacman_y_pos:
            pellet_index = i
            break

    # If collided, remove the pellet from the list and update the image
    if pellet_index is not None:
        pellet_positions.pop(pellet_index)
        cv2.circle(canvas, (pellet_x, pellet_y), 3, BLACK, -1)

    # Update Pacman direction and position
    if key == ord('w') and pacman_y_pos > 60:
        pacman_direction = "up"
        pacman_y_pos -= 10
    elif key == ord('s') and pacman_y_pos < 440:
        pacman_direction = "down"
        pacman_y_pos += 10
    elif key == ord('a') and pacman_x_pos > 60:
        pacman_direction = "left"
        pacman_x_pos -= 10
    elif key == ord('d') and pacman_x_pos < 440:
        pacman_direction = "right"
        pacman_x_pos += 10

    # Update Pacman mouth position based on direction
    if pacman_direction == "right":
        pacman_angle_start = 0
        pacman_angle_end = 360
    elif pacman_direction == "left":
        pacman_angle_start = 180
        pacman_angle_end = 540
    elif pacman_direction == "up":
        pacman_angle_start = 270
        pacman_angle_end = 630
    elif pacman_direction == "down":
        pacman_angle_start = 90
        pacman_angle_end = 450

    # Update mouth angle for animation
    if mouth_open:
        mouth_angle = 45
        mouth_open = False
    else:
        mouth_angle = 0
        mouth_open = True

    # Draw Pacman
    cv2.ellipse(canvas, (pacman_x_pos, pacman_y_pos), (pacman_radius, pacman_radius),
                0, pacman_angle_start + mouth_angle, pacman_angle_end - mouth_angle, YELLOW, -1)

    # Check if the ghost should appear
    if not show_ghost and time.time() - start_time >= 5:
        show_ghost = True

    # Update the ghost position based on Pacman's position
    if show_ghost:
        if ghost_x_pos < pacman_x_pos:
            ghost_x_pos += 2
        elif ghost_x_pos > pacman_x_pos:
            ghost_x_pos -= 2
        if ghost_y_pos < pacman_y_pos:
            ghost_y_pos += 2
        elif ghost_y_pos > pacman_y_pos:
            ghost_y_pos -= 2

    # Draw the ghost if it should appear
    if show_ghost:
        cv2.circle(canvas, (ghost_x_pos, ghost_y_pos), ghost_radius, RED, -1)
        cv2.rectangle(canvas, (ghost_x_pos - ghost_radius, ghost_y_pos), (ghost_x_pos + ghost_radius, ghost_y_pos + ghost_radius), RED, -1)
        cv2.circle(canvas, (ghost_x_pos, ghost_y_pos), ghost_radius, RED, -1)
        cv2.rectangle(canvas, (ghost_x_pos - ghost_radius, ghost_y_pos), (ghost_x_pos + ghost_radius, ghost_y_pos + ghost_radius), RED, -1)
        
        # Calculate the eye positions
        eye_radius = 3
        eye_y_offset = int(ghost_radius * 0.4)
        left_eye_x = ghost_x_pos - int(ghost_radius * 0.3)
        right_eye_x = ghost_x_pos + int(ghost_radius * 0.3)
        left_eye_y = ghost_y_pos - eye_y_offset
        right_eye_y = ghost_y_pos - eye_y_offset

# Draw the eyes
        cv2.circle(canvas, (left_eye_x, left_eye_y), eye_radius, WHITE, -1)
        cv2.circle(canvas, (right_eye_x, right_eye_y), eye_radius, WHITE, -1)
        
        # Draw the pupils
        cv2.circle(canvas, (left_eye_x, left_eye_y), 1, BLUE, -1)
        cv2.circle(canvas, (right_eye_x, right_eye_y), 1, BLUE, -1)
 # Change color to BLUE
    # Check if the ghost has caught Pacman
    if show_ghost and abs(ghost_x_pos - pacman_x_pos) < pacman_radius and abs(ghost_y_pos - pacman_y_pos) < pacman_radius:
        game_over = True

    # Show the game over message if game over
    if game_over:
        cv2.putText(canvas, "GAME OVER", (180, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow("Pacman Game", canvas)
        cv2.waitKey(0)
        break

    # Show the image
    cv2.imshow("Pacman Game", canvas)

    # Quit the game if the ESC key is pressed or if all the pellets are eaten
    if key == 27 or len(pellet_positions) == 0:
        break

# Clean up and exit
cv2.destroyAllWindows()
