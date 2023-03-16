from colorama import Fore


def get_starting_finishing_points():
    """The function will find the starting and finishing points and returns a tuple containing the first and last
    rows of the maze"""
    _start = [i for i in range(len(maze[0])) if maze[0][i] == 'c']
    _end = [i for i in range(len(maze[0])) if maze[len(maze)-1][i] == 'c']
    return [0, _start[0]], [len(maze) - 1, _end[0]]


def maze_solver():
    """print a visual representation of the maze with colored characters, 'u' is for unexplored path, 'c' for 
    destination and 'p' for current position, other characters are for walls"""
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == 'u':
                print(Fore.WHITE, f'{maze[i][j]}', end=" ")
            elif maze[i][j] == 'c':
                print(Fore.GREEN, f'{maze[i][j]}', end=" ")
            elif maze[i][j] == 'p':
                print(Fore.BLUE, f'{maze[i][j]}', end=" ")
            else:
                print(Fore.RED, f'{maze[i][j]}', end=" ")
        print('\n')


def escape():
    current_cell = rat_path[len(rat_path) - 1]

    if current_cell == finish:
        return

    if maze[current_cell[0] + 1][current_cell[1]] == 'c':
        maze[current_cell[0] + 1][current_cell[1]] = 'p'
        rat_path.append([current_cell[0] + 1, current_cell[1]])
        escape()

    if maze[current_cell[0] + 1][current_cell[1] + 1] == 'c':
        maze[current_cell[0]][current_cell[1] + 1] = 'p'
        rat_path.append([current_cell[0], current_cell[1] + 1])
        escape()

    if maze[current_cell[0] - 1][current_cell[1]] == 'c':
        maze[current_cell[0] - 1][current_cell[1]] = 'p'
        rat_path.append([current_cell[0] - 1, current_cell[1]])
        escape()

    if maze[current_cell[0]][current_cell[1] - 1] == 'c':
        maze[current_cell[0]][current_cell[1] - 1] = 'p'
        rat_path.append([current_cell[0], current_cell[1] - 1])
        escape()

    # if we get here if means we made a wrong decision, so we must backtrack

    current_cell = rat_path[len(rat_path) - 1]
    if current_cell != finish:
        cell_to_remove = rat_path[len(rat_path) - 1]
        rat_path.remove(cell_to_remove)
        maze[cell_to_remove[0][cell_to_remove[1]]] = 'c'


if __name__ == '__main__':
    """
    w is for walls
    c is for clear path
    """
    maze = [
        ['w', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
         'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
        ['w', 'c', 'c', 'w', 'c', 'w', 'c', 'c', 'w', 'w', 'c', 'c', 'c', 'c',
         'c', 'w', 'w', 'c', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
        ['w', 'w', 'c', 'w', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
         'c', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w'],
        ['w', 'c', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
         'c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
        ['w', 'w', 'w', 'c', 'w', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'w', 'w',
         'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w', 'w', 'w', 'c', 'w'],
        ['w', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c',
         'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'w'],
        ['w', 'c', 'w', 'c', 'w', 'w', 'w', 'w', 'c', 'c', 'w', 'c', 'w', 'w',
         'w', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w'],
        ['w', 'w', 'w', 'w', 'w', 'w', 'c', 'w', 'w', 'c', 'c', 'c', 'w', 'c',
         'w', 'w', 'w', 'w', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
        ['w', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'c', 'w', 'c',
         'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'w', 'c', 'w', 'w'],
        ['w', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
         'w', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'w'],
        ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
         'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w']
    ]


start, finish = get_starting_finishing_points()
maze[start[0]][start[1]] = 'p'

rat_path = [start]
escape()
print(maze_solver())
