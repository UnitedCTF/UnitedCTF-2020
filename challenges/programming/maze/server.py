import random
import socket
import socketserver

import flag

def distance(sx, sy, dx, dy):
    return abs(sx - dx) + abs(sy - dy)


def show(maze, spaces = False):
    print()
    for y in range(len(maze)):
        for x in range(len(maze)):
            print(maze[x][y] if maze[x][y] != "0" or not spaces else " ", end="")

        print()


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

    # We can divide the chamber horizontally (height more than 2)
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
    return sum([
        int(maze[tile[0] - 1][tile[1]] == "0"),
        int(maze[tile[0] + 1][tile[1]] == "0"),
        int(maze[tile[0]][tile[1] - 1] == "0"),
        int(maze[tile[0]][tile[1] + 1] == "0")
    ])

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


class TaskHandler(socketserver.BaseRequestHandler):
    def main(self, client):
        while True:
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

                maze[start[0]][start[1]] = "D"
                maze[goal[0]][goal[1]] = "F"

                show(maze, spaces = True)
                path = solve(maze, start)

                if path and len(path) > 5:
                    break
                else:
                    maze[start[0]][start[1]] = "0"
                    maze[goal[0]][goal[1]] = "0"

            if path is not None:
                break

        print(path)
        data = f"{size}\n"

        for y in range(size):
            for x in range(size):
                data += maze[x][y]
            
            data += "\n"
        
        client.sendall(data.encode())
        client.settimeout(5)
        try:
            answer = client.recv(1024).decode()
        except socket.timeout:
            print("Client timed out")
            client.sendall(b"Time out!\n")
            client.shutdown(socket.SHUT_RDWR)
            client.close()
            return

        print(answer)

        lines = answer.split("\n")

        try:
            if len(lines) > 0 and len(lines) >= int(lines[0]):
                n = int(lines[0])

                if n <= 0:
                    raise ValueError("Invalid line count")

                path = []

                for line in lines[1 : n + 1]:
                    x, y = map(int, line.split(" "))
                    path.append((x, y))
                
                previous = path[0]

                if maze[path[0][0]][path[0][1]] != "D":
                    raise ValueError("Invalid start point")
                
                if maze[path[-1][0]][path[-1][1]] != "F":
                    raise ValueError("Invalid end point")
                
                for tile in path[1 : -1]:
                    if distance(previous[0], previous[1], tile[0], tile[1]) > 1 or maze[tile[0]][tile[1]] != "0":
                        raise ValueError("Invalid move")

                    previous = tile

                client.sendall(flag.flag.encode() + b"\n")
            else:
                client.sendall(b"Wrong answer!\n")
        except ValueError as e:
            print(e)
            client.sendall(b"Wrong answer!\n")
        
        client.shutdown(socket.SHUT_RDWR)
        client.close()

    def handle(self):
        self.main(self.request)

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 3000), TaskHandler)
    server.serve_forever()
