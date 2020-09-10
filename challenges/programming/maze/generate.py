#!/usr/bin/env python3
import enum
import random
import sys


def show(maze, spaces = False):
    print()
    for y in range(len(maze)):
        for x in range(len(maze)):
            print(maze[x][y] if maze[x][y] != "0" or not spaces else " ", end="")
        
        print()


if len(sys.argv) == 2:
    seed = int(sys.argv[1])
else:
    seed = random.randrange(sys.maxsize)

rng = random.Random(seed)
print(f"Seed was: {seed}")


size = rng.randint(8, 14)
maze = [["#"] * size for _ in range(size)]

for y in range(1, size - 1):
    for x in range(1, size - 1):
        maze[x][y] = "0"

# Generate a maze by recursive divison
def generate(maze, sx, sy, dx, dy, hhole = None, vhole = None, debug = False):
    if sx == dx or sy == dy:
        return
    
    vchoices = [x for x in range(sx + 1, dx) if x != hhole]
    hchoices = [y for y in range(sy + 1, dy) if y != vhole]

    # We can divide the chamber vertically (width more than 2)
    if dx - sx > 1 and len(vchoices) > 0:
        vwall = rng.choice(vchoices)

        for y in range(sy, dy + 1):
            maze[vwall][y] = "#"
    else:
        vwall = None

    if dy - sy > 1 and len(hchoices) > 0:
        hwall = rng.choice(hchoices)
    
        for x in range(sx, dx + 1):
            if x != hhole:
                maze[x][hwall] = "#"
    else:
        hwall = None

    if hwall is None and vwall is None:
        maze[rng.randint(sx, sx + 1)][rng.randint(sy, sy + 1)] = "#"

        if debug:
            show(maze, spaces = True)
        
        return

    calls = []
    if hwall is not None and vwall is not None:
        hhole1 = rng.randint(sx, vwall - 1)
        hhole2 = rng.randint(vwall + 1, dx)
        vhole1 = rng.randint(hwall + 1, dy)

        maze[hhole1][hwall] = "0"
        maze[hhole2][hwall] = "0"
        maze[vwall][vhole1] = "0"

        if debug:
            show(maze, spaces = True)

        calls.append((sx, sy, vwall -1, hwall - 1, hhole1, vhole1))
        calls.append((vwall + 1, sy, dx, hwall - 1, hhole2, vhole1))
        calls.append((sx, hwall + 1, vwall - 1, dy, hhole1, vhole1))
        calls.append((vwall + 1, hwall + 1, dx, dy, hhole2, vhole1))
    elif vwall is not None:
        vhole1 = rng.randint(sy, dy)
        maze[vwall][vhole1] = "0"

        if debug:
            show(maze, spaces = True)

        calls.append((sx, sy, vwall - 1, dy, None, vhole1))
        calls.append((vwall + 1, sy, dx, dy, None, vhole1))
    else:
        hhole1 = rng.randint(sx, dx)
        maze[hhole1][hwall] = "0"

        if debug:
            show(maze, spaces = True)

        calls.append((sx, sy, dx, hwall - 1, hhole1, None))
        calls.append((sx, hwall + 1, dx, dy, hhole1, None))

    for args in calls:
        generate(maze, *args, debug = debug)

generate(maze, 1, 1, size - 2, size - 2, debug = True)
show(maze)
