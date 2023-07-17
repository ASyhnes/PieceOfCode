import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

top, left = 0, 0
bottom, right = h, w

# Initialize boundaries for search space
top, left = 0, 0
bottom, right = h, w

# Define functions to update search space boundaries
def move_up(y):
    global bottom
    bottom = y
def move_down(y):
    global top
    top = y
def move_left(x):
    global right
    right = x
def move_right(x):
    global left
    left = x
def move_up_left(x, y):
    move_up(y)
    move_left(x)
def move_up_right(x, y):
    move_up(y)
    move_right(x)
def move_down_left(x, y):
    move_down(y)
    move_left(x)
def move_down_right(x, y):
    move_down(y)
    move_right(x)

# Main game loop
while True:
    bomb_dir = input()

    if "U" in bomb_dir:
        move_up(y0-1)
    elif "D" in bomb_dir:
        move_down(y0+1)
    if "L" in bomb_dir:
        move_left(x0-1)
    elif "R" in bomb_dir:
        move_right(x0+1)
    if "U" in bomb_dir and "L" in bomb_dir:
        move_up_left(x0-1, y0-1)
    elif "U" in bomb_dir and "R" in bomb_dir:
        move_up_right(x0+1, y0-1)
    elif "D" in bomb_dir and "L" in bomb_dir:
        move_down_left(x0-1, y0+1)
    elif "D" in bomb_dir and "R" in bomb_dir:
        move_down_right(x0+1, y0+1)

    # Update Batman's position to the center of the search space
    x0 = (left + right) // 2
    y0 = (top + bottom) // 2

    print(x0, y0)