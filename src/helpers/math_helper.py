import math
import numpy

class MathHelper:
    @staticmethod
    def get_euclidean_distance(point_a, point_b):
        return math.sqrt(pow(point_a[0] - point_b[0], 2) + pow(point_a[1] - point_b[1], 2))

    @staticmethod
    def get_canvas_center(canvas_size):
        return canvas_size[0] / 2, canvas_size[1] / 2

    @staticmethod
    def get_equally_spaced_points(canvas_size, number_of_points, noise=0):
        center = MathHelper.get_canvas_center(canvas_size)
        degree_partition = (2 * math.pi) / number_of_points
        distance_from_edge = canvas_size[0] - center[0]

        points = []
        for i in range(0, number_of_points):
            current_degree = i * degree_partition + numpy.random.normal(0, noise)
            x = distance_from_edge * math.cos(current_degree) + center[0]
            y = distance_from_edge * math.sin(current_degree) + center[1]
            points.append((x, y))

        return points
