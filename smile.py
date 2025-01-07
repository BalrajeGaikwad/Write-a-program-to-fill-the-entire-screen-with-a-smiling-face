#Write a program to fill the entire screen with a smiling face

import os

# ASCII value 1 corresponds to ☺ in the extended ASCII table
smiley = chr(1)

# Get the terminal size
rows, columns = os.get_terminal_size()

# Fill the screen with the smiley face
for _ in range(rows):  # Print rows of smileys
    print(smiley * columns)
