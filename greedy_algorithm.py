from swap import *
from delta import *


def GreedyVerticlesAlgorithm(path, outside, matrix, path_length):
    combinations_to_swap_inside = generate_inside_swap_combinations(path)
    combinations_to_swap_outside = generate_outside_swap_combinations(path, outside)
    np.random.shuffle(combinations_to_swap_inside)
    np.random.shuffle(combinations_to_swap_outside)
    was_swapped = False
    counter_in = 0
    counter_out = 0
    while counter_in < len(combinations_to_swap_inside) and counter_out < len(combinations_to_swap_outside):
        if (np.random.random() < 0.5 and counter_out < len(combinations_to_swap_outside)) or counter_in >= len(combinations_to_swap_inside):
            vertices_to_swap = combinations_to_swap_outside[counter_out]
            delta = calculate_delta_outside(path, outside, vertices_to_swap, matrix)
            if delta > 0:
                path, outside = swap_vertices(path, outside, vertices_to_swap[0], vertices_to_swap[1])
                combinations_to_swap_inside = generate_inside_swap_combinations(path)
                combinations_to_swap_outside = generate_outside_swap_combinations(path, outside)
                counter_in, counter_out = 0, 0
                was_swapped = True
            else:
                was_swapped = False
                counter_out += 1
        else:
            vertices_to_swap = combinations_to_swap_inside[counter_in]
            delta = calculate_delta_inside_vertices(path, vertices_to_swap, matrix)
            if delta > 0:
                path[vertices_to_swap[0]], path[vertices_to_swap[1]] = path[vertices_to_swap[1]], path[vertices_to_swap[0]]
                combinations_to_swap_inside = generate_inside_swap_combinations(path)
                combinations_to_swap_outside = generate_outside_swap_combinations(path, outside)
                counter_in, counter_out = 0, 0
                was_swapped = True
            else:
                was_swapped = False
                counter_in += 1
        if was_swapped:
            np.random.shuffle(combinations_to_swap_inside)
            np.random.shuffle(combinations_to_swap_outside)
    return path


def GreedyEdgesAlgorithm(path, outside, matrix, path_length):
    combinations_to_swap_inside = generate_inside_swap_edge_combinations(path)
    combinations_to_swap_outside = generate_outside_swap_combinations(path, outside)
    np.random.shuffle(combinations_to_swap_inside)
    np.random.shuffle(combinations_to_swap_outside)
    counter_in = 0
    counter_out = 0
    while counter_in < len(combinations_to_swap_inside) and counter_out < len(combinations_to_swap_outside):
        if (np.random.random() < 0.5 and counter_out < len(combinations_to_swap_outside)) or counter_in >= len(combinations_to_swap_inside):
            vertices_to_swap = combinations_to_swap_outside[counter_out]
            delta = calculate_delta_outside(path, outside, vertices_to_swap, matrix)
            if delta > 0:
                path, outside = swap_vertices(path, outside, vertices_to_swap[0], vertices_to_swap[1])
                combinations_to_swap_inside = generate_inside_swap_edge_combinations(path)
                combinations_to_swap_outside = generate_outside_swap_combinations(path, outside)
                np.random.shuffle(combinations_to_swap_inside)
                np.random.shuffle(combinations_to_swap_outside)
                counter_in, counter_out = 0, 0
            else:
                counter_out += 1
        else:
            vertices_to_swap = combinations_to_swap_inside[counter_in]
            delta = calculate_delta_inside_edges(path, vertices_to_swap, matrix)
            if delta > 0:
                a = path[vertices_to_swap[0]:vertices_to_swap[1] + 1]
                a = np.flip(a)
                path[vertices_to_swap[0]:vertices_to_swap[1] + 1] = a
                combinations_to_swap_inside = generate_inside_swap_edge_combinations(path)
                combinations_to_swap_outside = generate_outside_swap_combinations(path, outside)
                np.random.shuffle(combinations_to_swap_inside)
                np.random.shuffle(combinations_to_swap_outside)
                counter_in, counter_out = 0, 0
            else:
                counter_in += 1
    return path
