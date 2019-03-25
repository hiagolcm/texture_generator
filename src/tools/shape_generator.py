import random

from src.helpers.math_helper import MathHelper


class ShapeGenerator:
    FILL = (0, 0, 0)

    @staticmethod
    def draw_shape(draw, position, island_radius, shape_radius, number_of_points, noise=0):
        while True:
            x = random.randrange(position[0] - island_radius, position[0] + island_radius)
            y = random.randrange(position[1] - island_radius, position[1] + island_radius)

            if MathHelper.get_euclidean_distance((x, y), position) <= island_radius:
                break

        points = MathHelper.get_polygon((x, y), shape_radius, number_of_points, noise=noise)

        draw.polygon(points, fill=(0, 0, 0))
