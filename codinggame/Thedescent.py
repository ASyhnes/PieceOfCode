import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Osef pour le code, c'est le nombre de temp a analyser
t_comparée = None

if n == 0 or None:
    t_comparée = 0

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

    if t_comparée == None:
        t_comparée = t

    if abs(t) < abs(t_comparée):
        t_comparée = t

    if abs(t) == abs(t_comparée) and t > t_comparée:
        t_comparée = t

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(t_comparée)
