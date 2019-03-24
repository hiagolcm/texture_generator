from PIL import Image, ImageDraw

from helpers.math_helper import MathHelper


class ShapeGenerator:
    FILL = (0, 0, 0)

    @staticmethod
    def __create_empty_canvas(canvas_size):
        return Image.new('RGBA', canvas_size, (255, 255, 255, 1))

    @staticmethod
    def create_shape(canvas_size, number_of_points, degree_noise=0):
        canvas = ShapeGenerator.__create_empty_canvas(canvas_size)
        draw = ImageDraw.Draw(canvas)
        points = MathHelper.get_equally_spaced_points(canvas_size, number_of_points, noise=degree_noise)

        draw.polygon(points, fill=(0, 0, 0))
        return canvas

