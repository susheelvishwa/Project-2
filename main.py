from sketchpy import library as lib
from sketchpy import canvas

obj = canvas.sketch_from_image(
    path="C:\\Users\\sushe\\OneDrive\\Documents\\project\\sketch\\susheel Vishwakarma .jpg",
    save=False,
)
# obj.load_svg(file="data.npy")
obj.draw(threshold=50)
# obj = lib.rdj()
