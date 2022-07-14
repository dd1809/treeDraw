import copy
import random


def change_matrix_BFS(matrix):
    start_position = next((i, j) for i, row in enumerate(matrix)
                          for j, item in enumerate(row) if item == 'S')
    buffer_matrix = copy.deepcopy(matrix)
    queue = [start_position]
    while queue:
        current_position = queue.pop(0)
        for neighbour in get_neighbours_BFS(buffer_matrix, current_position):
            queue.append(neighbour)
            process_neighbours_BFS(buffer_matrix, current_position)
        yield buffer_matrix


def change_matrix_DFS(matrix):
    start_position = next((i, j) for i, row in enumerate(matrix)
                          for j, item in enumerate(row) if item == 'S')
    buffer_matrix = copy.deepcopy(matrix)
    stack = [start_position]
    while stack:
        current_position = stack[-1]
        child = get_neighbours_DFS(buffer_matrix, current_position)
        if child:
            stack.append(child)
            process_neighbours_DFS(buffer_matrix, current_position)
        else:
            stack.pop(-1)
        yield buffer_matrix


def get_neighbours_DFS(matrix, element):
    i, j = element
    if matrix[i + 1][j] == '.':
        return i + 1, j
    if matrix[i][j + 1] == '.':
        return i, j + 1
    if matrix[i - 1][j] == '.':
        return i - 1, j
    if matrix[i][j - 1] == '.':
        return i, j - 1


def process_neighbours_DFS(matrix, element):
    i, j = element
    if matrix[i + 1][j] == '.':
        matrix[i + 1][j] = 'D'
        return
    if matrix[i][j + 1] == '.':
        matrix[i][j + 1] = 'R'
        return
    if matrix[i - 1][j] == '.':
        matrix[i - 1][j] = 'U'
        return
    if matrix[i][j - 1] == '.':
        matrix[i][j - 1] = 'L'
        return


def get_neighbours_BFS(matrix, element):
    i, j = element
    all_neighbours = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
    return [neighbour for neighbour in all_neighbours if matrix[neighbour[0]][neighbour[1]] == '.']


def process_neighbours_BFS(matrix, element):
    i, j = element
    if matrix[i + 1][j] == '.':
        matrix[i + 1][j] = 'D'
    if matrix[i][j + 1] == '.':
        matrix[i][j + 1] = 'R'
    if matrix[i - 1][j] == '.':
        matrix[i - 1][j] = 'U'
    if matrix[i][j - 1] == '.':
        matrix[i][j - 1] = 'L'


def get_all_neighbours(matrix, element):
    rows, cols = len(matrix), len(matrix[0])
    i, j = element
    return [x for x in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)] if 0 < x[0] < rows and 0 < x[1] < cols]


def generate_matrix(rows, cols):
    buffer_matrix = [['#' for _ in range(cols)] for _ in range(rows)]
    start_position = i_start, j_start = (random.randint(1, rows - 2), random.randint(1, cols - 2))
    buffer_matrix[i_start][j_start] = 'S'

    queue = [start_position]
    visited_set = set()
    while queue:
        current_position = queue.pop(0)
        for neighbour in get_neighbours_random(buffer_matrix, current_position, visited_set):
            queue.append(neighbour)
            buffer_matrix[neighbour[0]][neighbour[1]] = '.'
            visited_set.add(current_position)
    return buffer_matrix


def get_neighbours_random(matrix, element, visited_set):
    rows, cols = len(matrix), len(matrix[0])
    i, j = element

    def neighbour_is_correct(neighbour):
        random_factor = (random.random() > 0.3)
        within_the_borders = (1 <= neighbour[0] <= rows - 2 and 1 <= neighbour[1] <= cols - 2)
        no_dots_nearly = [x for x in get_all_neighbours(matrix, neighbour) if
                          matrix[x[0]][x[1]] == '.' or matrix[x[0]][x[1]] == 'S']
        no_branches_nearly = len(no_dots_nearly) <= 1
        return within_the_borders and no_branches_nearly and random_factor and neighbour not in visited_set

    all_neighbours = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
    return [neighbour for neighbour in all_neighbours if neighbour_is_correct(neighbour)]


def test(test_matrix):
    for frame in change_matrix_DFS(test_matrix):
        for row in frame:
            print(row)
    print('\n')
    for frame in change_matrix_BFS(test_matrix):
        for row in frame:
            print(row)


test_matrix4 = generate_matrix(5, 5)
test(test_matrix4)
