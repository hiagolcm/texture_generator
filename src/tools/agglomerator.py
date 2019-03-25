import math
import random

from PIL import Image, ImageDraw

from src.helpers.math_helper import MathHelper
from src.tools.shape_generator import ShapeGenerator


class Agglomerator:
    CANVAS_SIZE = (800, 800)

    @staticmethod
    def generate_agglomeration(number_of_islands, island_radius, shapes_per_island, number_of_points_in_shape,
                              shape_radius, noise=0.0, show_islands=True):
        number_of_islands_with_noise = round(MathHelper.apply_noise(number_of_islands, noise))  # apply noise

        canvas = Image.new('RGB', Agglomerator.CANVAS_SIZE, (255, 255, 255))
        draw = ImageDraw.Draw(canvas)

        for i in range(0, number_of_islands_with_noise):
            canvas_w, canvas_h = canvas.size
            island_position = (round(random.randrange(0, canvas_w)), round(random.randrange(0, canvas_h)))

            shapes_per_island_with_noise = round(MathHelper.apply_noise(shapes_per_island, noise))  # apply noise

            for j in range(0, shapes_per_island_with_noise):
                island_radius_with_noise = round(MathHelper.apply_noise(island_radius, noise))  # apply noise
                ShapeGenerator.draw_shape(draw, island_position, island_radius_with_noise, shape_radius,
                                          number_of_points_in_shape, noise)

            if show_islands:
                draw.ellipse((island_position[0] - island_radius, island_position[1] - island_radius,
                             island_position[0] + island_radius, island_position[1] + island_radius),
                             outline=(255, 0, 0))

        return canvas
