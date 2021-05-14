from greedy_algorithm import *


def generate_random_path(length, dataset_size):
    points = np.arange(dataset_size)
    np.random.shuffle(points)
    return points[:length], points[length:]


def calculate_distance(matrix, visited_vertexes):
    sum_of_distance = 0
    for i in range(len(visited_vertexes) - 1):
        sum_of_distance += matrix[visited_vertexes[i]][visited_vertexes[i + 1]]
    sum_of_distance += matrix[visited_vertexes[-1]][visited_vertexes[0]]
    return sum_of_distance


def msls(path, outside, matrix, path_length):
    all_paths = []
    all_distances = []
    for i in range(0, 100):
        path_in, out = generate_random_path(path_length, len(matrix[0]))
        path_out = GreedyEdgesAlgorithm(path_in, out, matrix, path_length)
        current_len = calculate_distance(matrix, path_out)
        all_distances.append(current_len)
        all_paths.append(path_out)
    best = np.asarray(all_distances).argmin(axis=0)
    return all_paths[best]
