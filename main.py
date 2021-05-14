import json
from datetime import datetime
import types
from preparedata import *
from draw import *
from msls_algorithm import *
from ils_1 import *
from ils_2 import *
from ils_2a import *


PATH = ""

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


def test(matrix, alg, number_of_tests, path_length):
    global PATH
    all_paths = []
    all_distances = []
    all_times = []
    for i in range(number_of_tests):
        path_in, out = generate_random_path(path_length, len(matrix[0]))
        start = datetime.now()
        path_in = alg(path_in, out, matrix, path_length)
        stop = datetime.now()
        current_len = calculate_distance(matrix, path_in)
        all_distances.append(current_len)
        all_paths.append(path_in)
        all_times.append(stop - start)

    print("Distances")
    best, worst, mean = results(np.asarray(all_distances))
    print(all_distances[best])
    print(all_distances[worst])
    print(mean)
    print("Times")
    best_time, worst_time, mean_time = results(np.asarray(all_times))
    if isinstance(alg, msls.__class__):
        data = {}
        with open('times.json', 'a') as outfile:
            data[PATH] = str(mean_time)
            json.dump(data, outfile)
    print(all_times[best_time])
    print(all_times[worst_time])
    print(mean_time)

    return all_paths[best]


def results(all_distance):
    best = all_distance.argmin(axis=0)
    mean = all_distance.mean(axis=0)
    worst = all_distance.argmax(axis=0)
    return best, worst, mean


def main(path):
    loaded_data = PrepareData(path)
    coordinates = loaded_data.get_coords()
    drawing = DrawPlot(coordinates)
    matrix = loaded_data.calculate_distance_matrix()
    number_of_tests = 10
    path_length = 100
    print("MSLS - Greedy edge")
    min_path = test(matrix, msls, number_of_tests, path_length)
    drawing.draw_results(min_path, "images/msls_greed_edge" + path + ".png", 'msls_greed_edge_' + path)

    print("ILS1 - Greedy edge")
    min_path = test(matrix, ils_1, number_of_tests, path_length)
    drawing.draw_results(min_path, "images/ILS1_greed_edge" + path + ".png", 'ILS1_greed_edge_' + path)

    print("ILS2 - Greedy edge")
    min_path = test(matrix, ils_2, number_of_tests, path_length)
    drawing.draw_results(min_path, "images/ILS2_greed_edge" + path + ".png", 'ILS2_greed_edge_' + path)

    print("ILS2 ver a - Greedy edge")
    min_path = test(matrix, ils_2a, number_of_tests, path_length)
    drawing.draw_results(min_path, "images/ILS2a_greed_edge" + path + ".png", 'ILS2a_greededge' + path)


if __name__ == '__main__':
    print("kroA200")
    PATH = "kroA200"
    main(pathA)
    print("kroB200")
    PATH = "kroB200"
    main(pathB)
