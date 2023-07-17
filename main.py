from sketchpy import library as lib
from sketchpy import canvas

obj = canvas.sketch_from_image(path="ladki.png", save=False)
# obj.load_svg(file="data.npy")
# obj.draw(threshold=100)
# obj = lib.rdj()
obj.draw()
