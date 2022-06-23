from PIL import Image
import numpy as np
im = Image.open("ascii-pineapple.jpg")
print("sucessfuly loaded image", im.format, im.size, im.mode)
print("And here is the image!")
im.show()

image_sequence = im.getdata()
image_array = np.array(image_sequence)
print(image_array)
