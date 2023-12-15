def solve_maze(maze, x, y, path):
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
        return False
    if maze[x][y] == 1:
        return False
    if is_exit(x, y, maze):
        path.append((x, y))
        return True

    maze[x][y] = 1  # Marcamos la posición actual como visitada

    # Intentamos moverse en todas las direcciones posibles
    if (solve_maze(maze, x-1, y, path) or
        solve_maze(maze, x+1, y, path) or
        solve_maze(maze, x, y-1, path) or
            solve_maze(maze, x, y+1, path)):
        path.append((x, y))
        return True

    return False


def is_exit(x, y, maze):
    # Verifica si la posición es una salida (en los bordes del laberinto)
    return x == 0 or y == 0 or x == len(maze) - 1 or y == len(maze[0]) - 1


# Laberinto de ejemplo
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Coordenadas de la entrada
start_x, start_y = 1, 1

# Llamamos a la función solve_maze para resolver el laberinto desde la entrada
path_to_exit = []
if solve_maze(maze, start_x, start_y, path_to_exit):
    print("Se encontró un camino a la salida:")
    # Imprime la penúltima coordenada del camino, que es la salida
    print(path_to_exit[-2])
else:
    print("No se encontró un camino a la salida.")
