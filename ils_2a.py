from swap import *
import time
import random
from greedy_cycle_algorithm import *


def calculate_distance(matrix, visited_vertexes):
    sum_of_distance = 0
    for i in range(len(visited_vertexes) - 1):
        sum_of_distance += matrix[visited_vertexes[i]][visited_vertexes[i + 1]]
    sum_of_distance += matrix[visited_vertexes[-1]][visited_vertexes[0]]
    return sum_of_distance


def ils_2a(path, outside, matrix, path_length):
    timeout = time.time() + 700
    combinations_to_swap_inside = generate_inside_swap_edge_combinations(path)
    combinations_to_swap_outside = generate_outside_swap_combinations(path, outside)
    np.random.shuffle(combinations_to_swap_inside)
    np.random.shuffle(combinations_to_swap_outside)

    while time.time() < timeout:
        path_y = np.copy(path)
        outside_y = np.copy(outside)

        # ---------------------------------------
        counter = 20
        while counter > 0:
            if random.randint(0, 1) == 0:
                rand_elem = random.randint(0, len(path_y)-1)
                path_y = np.delete(path_y, rand_elem)
                counter -= 1
            else:
                rand_elem = random.randint(0, len(path_y)-1)
                path_y = np.delete(path_y, [rand_elem, (rand_elem+1) % len(path_y)])
                counter -= 2

        greed = GreedyCycleAlgorithm(distance_matrix=matrix)
        path_y = greed.run(path_y, path_length-len(path_y))
        outside_y = [e for e in range(0, len(matrix[0])) if e not in path_y]
        # ---------------------------------------
        path_x_len = calculate_distance(matrix, path)
        path_y_len = calculate_distance(matrix, path_y)
        if path_y_len < path_x_len:
            path = path_y
            outside = outside_y

        combinations_to_swap_inside = generate_inside_swap_edge_combinations(path)
        combinations_to_swap_outside = generate_outside_swap_combinations(path, outside)
        np.random.shuffle(combinations_to_swap_inside)
        np.random.shuffle(combinations_to_swap_outside)

    return path