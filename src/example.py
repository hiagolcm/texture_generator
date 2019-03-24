from PIL import ImageFilter

from tools.agglomerator import Agglomerator


canvas = Agglomerator.generate_aglomeration(30, 3, 50, 5, (50, 50), 0, 0.9)

canvas.filter(ImageFilter.EMBOSS).show()
