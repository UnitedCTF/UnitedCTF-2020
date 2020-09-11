#!/usr/bin/env python3
from pwn import *

def find_neighbors(maze, tile):
    neighbors = []

    if tile[0] > 1:
        neighbors.append((tile[0] - 1, tile[1]))
    if tile[0] < len(maze) - 1:
        neighbors.append((tile[0] + 1, tile[1]))
    if tile[1] > 1:
        neighbors.append((tile[0], tile[1] - 1))
    if tile[1] < len(maze) - 1:
        neighbors.append((tile[0], tile[1] + 1))

    return neighbors

def solve(maze, tile):
    x, y = tile

    if maze[x][y] == "F":
        return [tile]

    if maze[x][y] != "D":
        maze[x][y] = "X"

    path = None

    for neighbor in find_neighbors(maze, tile):
        if maze[neighbor[0]][neighbor[1]] not in "0F":
            continue

        path = solve(maze, neighbor)

        if path:
            break

    if maze[x][y] != "D":
        maze[x][y] = "0"

    if path is not None:
        return [tile] + path
    else:
        return None

def show(maze, spaces = False):
    print()
    for y in range(len(maze)):
        for x in range(len(maze)):
            print(maze[x][y] if maze[x][y] != "0" or not spaces else " ", end="")

        print()

def parse(r):
    n = int(r.recvline())

    maze = [[""] * n for _ in range(n)]

    for y in range(n):
        row = r.recvline().decode().strip()
        
        for x in range(n):
            maze[x][y] = row[x]

            if row[x] == "F":
                goal = (x, y)
            elif row[x] == "D":
                start = (x, y)
    
    return maze, start, goal


r = remote("127.0.0.1", 3000)

maze, start, goal = parse(r)
show(maze)
path = solve(maze, start)

answer = str(len(path)) + "\n"

for tile in path:
    answer += f"{tile[0]} {tile[1]}\n"

print(answer)
r.send(answer)
print(r.recvall().decode())
