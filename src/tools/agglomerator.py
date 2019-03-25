import math
import random

from PIL import Image, ImageDraw

from src.helpers.math_helper import MathHelper
from src.tools.shape_generator import ShapeGenerator


class Agglomerator:
    CANVAS_SIZE = (800, 800)

    @staticmethod
    def __randomize_shape_position(position, island_radius):
        while True:
            x = random.randrange(position[0] - island_radius, position[0] + island_radius)
            y = random.randrange(position[1] - island_radius, position[1] + island_radius)

            if MathHelper.get_euclidean_distance((x, y), position) <= island_radius:
                break

        return x, y

    @staticmethod
    def generate_agglomeration(number_of_islands, island_radius, shapes_per_island, number_of_points_in_shape,
                               shape_radius, noise_island=0.0, noise_shape=0.0, show_islands=False):
        number_of_islands_with_noise = round(MathHelper.apply_noise(number_of_islands, noise_island))  # apply noise

        canvas = Image.new('RGB', Agglomerator.CANVAS_SIZE, (255, 255, 255))
        draw = ImageDraw.Draw(canvas)

        for i in range(0, number_of_islands_with_noise):
            canvas_w, canvas_h = canvas.size
            island_position = (round(random.randrange(0, canvas_w)), round(random.randrange(0, canvas_h)))

            shapes_per_island_with_noise = round(MathHelper.apply_noise(shapes_per_island, noise_island))  # apply noise

            for j in range(0, shapes_per_island_with_noise):
                island_radius_with_noise = round(MathHelper.apply_noise(island_radius, noise_island))  # apply noise
                shape_position = Agglomerator.__randomize_shape_position(island_position, island_radius_with_noise)

                ShapeGenerator.draw_shape(draw, shape_position, shape_radius,
                                          number_of_points_in_shape, noise_shape)

            if show_islands:
                draw.ellipse((island_position[0] - island_radius, island_position[1] - island_radius,
                             island_position[0] + island_radius, island_position[1] + island_radius),
                             outline=(255, 0, 0), width=3)

        return canvas
