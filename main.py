from image import Image


img1 = "./pics/img1.jpeg"

image = Image(img1)

print("Image shape: " + image.getShape().__str__())

print("Image dtype: ") 
print(image.getDtype())


image.removeBackground()
image.showFinalImage()
