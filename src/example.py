from PIL import ImageFilter

from src.tools.agglomerator import Agglomerator

# island
number_of_islands = 10
island_radius = 60
shapes_per_island = 20

# shape
number_of_points_in_shape = 5
shape_radius = 12

noise = 0.1

canvas = Agglomerator.generate_agglomeration(number_of_islands, island_radius, shapes_per_island,
                                             number_of_points_in_shape, shape_radius, noise=noise).show()

#canvas.filter(ImageFilter.EMBOSS).show()
