from sketchpy import library as lib
from sketchpy import canvas

obj = canvas.sketch_from_image(
    path="C:\\Users\\sushe\\OneDrive\\Documents\\project\\sketch\\image.jpg",
    save=False,
)
obj.draw(threshold=130)
