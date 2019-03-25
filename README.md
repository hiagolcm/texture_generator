# texture_generator

A really simple texture generator based on polygons.

## Requirements
* [Python](https://www.python.org/)
* [Pip](https://pypi.org/project/pip/)
* [Pipenv](https://github.com/pypa/pipenv)

## Setup
On the project folder run:

`pipenv install`

## Run
Activate the virtual enviroment by running:

`pipenv shell`

And then run:

`python example.py`

## Settings
By modifying example.py parameters you can generate different textures.

Parameter | Description
--- | ---
`number_of_islands` | Number of islands on the canvas
`island_radius` | Radius of the island circumference
`shapes_per_island ` | Number of polygons by island
`number_of_points_in_shape` | Number of vertices
`shape_radius` | Polygon radius
`noise` | noise applied to all variables
