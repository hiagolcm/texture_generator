from src.tools.agglomerator import Agglomerator

# island
number_of_islands = 10
island_radius = 60
shapes_per_island = 20

# shape
number_of_points_in_shape = 6
shape_radius = 12

noise_interval = 0.1

for i in range (0, 4):
    noise = i * noise_interval
    canvas = Agglomerator.generate_agglomeration(number_of_islands, island_radius, shapes_per_island,
                                                 number_of_points_in_shape, shape_radius, noise_island=noise,
                                                 noise_shape=0, show_islands=True)
    canvas.save('figure-{}.png'.format(i))
