import random
import socket
import socketserver

import flag

def distance(sx, sy, dx, dy):
    return abs(sx - dx) + abs(sy - dy)

# Generate a maze by recursive divison
def generate(maze, sx, sy, dx, dy, hhole = None, vhole = None, debug = False):
    if sx == dx or sy == dy:
        return
    
    vchoices = [x for x in range(sx + 1, dx) if x != hhole]
    hchoices = [y for y in range(sy + 1, dy) if y != vhole]

    # We can divide the chamber vertically (width more than 2)
    if dx - sx > 1 and len(vchoices) > 0:
        vwall = random.choice(vchoices)

        for y in range(sy, dy + 1):
            maze[vwall][y] = "#"
    else:
        vwall = None

    if dy - sy > 1 and len(hchoices) > 0:
        hwall = random.choice(hchoices)
    
        for x in range(sx, dx + 1):
            if x != hhole:
                maze[x][hwall] = "#"
    else:
        hwall = None

    if hwall is None and vwall is None:
        maze[random.randint(sx, sx + 1)][random.randint(sy, sy + 1)] = "#"

        if debug:
            show(maze, spaces = True)
        
        return

    calls = []
    if hwall is not None and vwall is not None:
        hhole1 = random.randint(sx, vwall - 1)
        hhole2 = random.randint(vwall + 1, dx)
        vhole1 = random.randint(hwall + 1, dy)

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
        vhole1 = random.randint(sy, dy)
        maze[vwall][vhole1] = "0"

        if debug:
            show(maze, spaces = True)

        calls.append((sx, sy, vwall - 1, dy, None, vhole1))
        calls.append((vwall + 1, sy, dx, dy, None, vhole1))
    else:
        hhole1 = random.randint(sx, dx)
        maze[hhole1][hwall] = "0"

        if debug:
            show(maze, spaces = True)

        calls.append((sx, sy, dx, hwall - 1, hhole1, None))
        calls.append((sx, hwall + 1, dx, dy, hhole1, None))

    for args in calls:
        generate(maze, *args, debug = debug)


def free_neighbors(maze, tile):
    print(tile, len(maze))
    return sum([
        int(maze[tile[0] - 1][tile[1]] == "0"),
        int(maze[tile[0] + 1][tile[1]] == "0"),
        int(maze[tile[0]][tile[1] - 1] == "0"),
        int(maze[tile[0]][tile[1] + 1] == "0")
    ])


class TaskHandler(socketserver.BaseRequestHandler):
    def main(self, client):
        size = random.randint(8, 14)

        maze = [["#"] * size for _ in range(size)]
        for y in range(1, size - 1):
            for x in range(1, size - 1):
                maze[x][y] = "0"
        
        generate(maze, 1, 1, size - 2, size - 2)

        # From (1, 1) to (size - 2, size - 2)
        tiles = [(i % size, i // size) for i in range(size * size) if i % size != 0 and i % size != size - 1 and i // size != 0 and i // size != size - 1]
        isolated_tiles = [tile for tile in tiles if free_neighbors(maze, tile) == 1]

        # Try 10 times to choose a start and a goal, otherwise restart the whole thing (broken maze) :)
        for _ in range(10):
            start = random.choice(isolated_tiles)
            goal = random.choice([tile for tile in isolated_tiles if tile != start])

            # TODO: Make sure there's a path between start and goal
        
        maze[start[0]][start[1]] = "D"
        maze[goal[0]][goal[1]] = "F"

        data = f"{size}\n"

        for y in range(size):
            for x in range(size):
                data += maze[x][y]
            
            data += "\n"
        
        client.sendall(data.encode())
        answer = client.recv(1024).decode()

        if answer == child:
            client.sendall(flag.flag.encode())
        else:
            client.sendall(b"Wrong answer!")
        
        client.shutdown(socket.SHUT_RDWR)
        client.close()

    def handle(self):
        self.main(self.request)

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 3000), TaskHandler)
    server.serve_forever()
