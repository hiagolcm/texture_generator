import random

from src.helpers.math_helper import MathHelper


class ShapeGenerator:
    FILL = (0, 0, 0)

    @staticmethod
    def draw_shape(draw, position, shape_radius, number_of_points, noise=0):
        points = MathHelper.get_polygon(position, shape_radius, number_of_points, noise=noise)

        draw.polygon(points, fill=(0, 0, 0))
