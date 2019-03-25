import math
import numpy

class MathHelper:
    @staticmethod
    def get_euclidean_distance(point_a, point_b):
        return math.sqrt(pow(point_a[0] - point_b[0], 2) + pow(point_a[1] - point_b[1], 2))

    @staticmethod
    def get_polygon(position, shape_radius, number_of_points, noise=0):
        center = position
        degree_partition = (2 * math.pi) / number_of_points

        points = []
        for i in range(0, number_of_points):
            current_degree = MathHelper.apply_noise(i * degree_partition, noise)

            shape_radius_with_noise = MathHelper.apply_noise(shape_radius, noise)

            x = shape_radius_with_noise * math.cos(current_degree) + center[0]
            y = shape_radius_with_noise * math.sin(current_degree) + center[1]

            points.append((x, y))

        return points

    @staticmethod
    def apply_noise(x, noise):
        return x * numpy.random.normal(1, noise)
