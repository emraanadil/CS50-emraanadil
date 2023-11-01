# built the pyramid of mario using hashes

from cs50 import get_int

# getting user input but valid
while True:
    height = get_int("Height: ")
    if (height > 0 and height < 9):
        break
# build a pyramid
for i in range(height):
    print((height - (i + 1)) * " ", end="")
    print((i + 1) * "#")