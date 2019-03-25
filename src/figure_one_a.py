from PIL import Image, ImageDraw

from src.tools.shape_generator import ShapeGenerator

canvas_size = (800, 800)

canvas = Image.new('RGB', canvas_size, (255, 255, 255))
draw = ImageDraw.Draw(canvas)

radius_interval = 30
number_of_points_interval = 2
axis_interval = 200

for i in range(0, 3):
    y = (i + 1) * axis_interval
    number_of_points = i * number_of_points_interval + 3
    for j in range(0, 3):
        x = (j + 1) * axis_interval
        shape_radius = (j + 1) * radius_interval
        ShapeGenerator.draw_shape(draw, (x, y), shape_radius, number_of_points)

canvas.rotate(180).transpose(Image.FLIP_LEFT_RIGHT).show()

