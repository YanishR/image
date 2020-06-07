from image import Image

img_url = "pics/img3.jpeg"

image = Image(img_url)

# Set rectangle to get more accurate results
rectangle = (100, 200, 350, 400)

# image.showImage() 

image.removeBackground(rectangle)

image.saveImage()
image.showFinalImage()
