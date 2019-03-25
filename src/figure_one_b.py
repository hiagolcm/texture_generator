import random

from PIL import Image, ImageDraw

from src.tools.shape_generator import ShapeGenerator

random.seed(0)

canvas_size = (800, 800)

canvas = Image.new('RGB', canvas_size, (255, 255, 255))
draw = ImageDraw.Draw(canvas)

axis_interval = 90
radius = 30
number_of_points = 8
noise_interval = 0.011

for i in range(0, 8):
    x = (i + 1) * axis_interval
    noise = i * noise_interval
    ShapeGenerator.draw_shape(draw, (x, 400), radius, number_of_points, noise=noise)

canvas.save('figure.png')
