import math
import random

from PIL import Image

from tools.shape_generator import ShapeGenerator


class Agglomerator:
    CANVAS_SIZE = (800, 800)

    @staticmethod
    def __draw_shape(canvas, shape, mean_distance, reference_position=None):
        if reference_position is not None:
            degree_from_reference = 2 * math.pi * random.random()
            x_position = math.floor(math.cos(degree_from_reference) * mean_distance) + reference_position[0]
            y_position = math.floor(math.sin(degree_from_reference) * mean_distance) + reference_position[1]
            canvas.paste(shape, (x_position, y_position), shape)
            return x_position, y_position
        else:
            canvas_w, canvas_h = canvas.size
            x_position = math.floor(random.randrange(0, canvas_w))
            y_position = math.floor(random.randrange(0, canvas_h))
            canvas.paste(shape, (x_position, y_position), shape)
            return x_position, y_position

    @staticmethod
    def generate_aglomeration(shapes_per_island, number_of_points_in_shape, mean_distance, number_of_islands, shape_scale,  rotation, noise=0.0):
        canvas = Image.new('RGB', Agglomerator.CANVAS_SIZE, (255, 255, 255))

        for i in range(0, number_of_islands):
            reference_position = None
            for j in range(0, shapes_per_island):
                shape = ShapeGenerator.create_shape(shape_scale, number_of_points_in_shape, noise).rotate(rotation)
                reference_position = Agglomerator.__draw_shape(canvas, shape, mean_distance, reference_position)

        return canvas
