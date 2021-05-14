import numpy as np
from operator import itemgetter


def shortest_next(distances_matrix, visited, last):
    new_row_of_distance_matrix = distances_matrix[last].copy()
    max_value = np.max(new_row_of_distance_matrix)
    new_row_of_distance_matrix[last] = 2*max_value
    for v in visited:
        new_row_of_distance_matrix[v] = 2*max_value
    return np.argmin(new_row_of_distance_matrix)


class GreedyCycleAlgorithm:

    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix

    def length_gain(self, vertex_a, vertex_b, new_vertex):
        # Cost = Cost_after - Cost_before
        return self.distance_matrix[vertex_a, new_vertex] + self.distance_matrix[new_vertex, vertex_b] - \
               self.distance_matrix[vertex_a, vertex_b]

    def search(self, unchecked_vertex, visited_vertexes, j):
        list_tuples_vertex_length = []
        for u in unchecked_vertex:
            x = self.length_gain(visited_vertexes[j], visited_vertexes[j + 1], u)
            list_tuples_vertex_length.append((u, x))
        vertex_with_min_length = min(list_tuples_vertex_length, key=itemgetter(1))[0]
        min_length = min(list_tuples_vertex_length, key=itemgetter(1))[1]
        if j < 0:
            return (len(visited_vertexes) - 1, j + 1), (min_length, vertex_with_min_length)
        return (j, j + 1), (min_length, vertex_with_min_length)

    def run(self, visited_vertexes, vertexes):

        for i in range(0, vertexes):
            best_value_for_next_cycle = []
            unchecked_vertex = [e for e in range(len(self.distance_matrix)) if e not in visited_vertexes]

            for j in range(len(visited_vertexes) - 1):
                best_value_for_next_cycle.append(self.search(unchecked_vertex, visited_vertexes, j))

            final = self.search(unchecked_vertex, visited_vertexes, -1)
            best_value_for_next_cycle.append(final)

            best_place_to_put = min(best_value_for_next_cycle, key=itemgetter(1))
            visited_vertexes = np.insert(np.array(visited_vertexes), best_place_to_put[0][1], best_place_to_put[1][1])
        return visited_vertexes
