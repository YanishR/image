import cv2

import matplotlib.pyplot as plt
import numpy as np

class Image():

    def __init__(self, url):
        self.url = url
        self.directory = url[0:url.find('/') + 1]
        self.file =  url[url.find('/')  + 1:]

        self.img = cv2.imread(url)
        self.final = None

    def getShape(self):
        return self.img.shape

    def getDtype(self):
        return self.img.dtype

    def showImage(self):
        plt.imshow(self.img)
        plt.show()

    def saveImage(self):
        print()
        print("Saving Image.")
        cv2.imwrite(self.directory + "final/" +  self.file, self.final)

    def showFinalImage(self):
        if self.final is not None:
            plt.imshow(self.final)
            plt.show()
        else:
            print("Background removal has not been executed.")

    def removeBackground(self, rectangle):

        # Convert to color
        image_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

        # Create initial mask
        mask = np.zeros(image_rgb.shape[:2], np.uint8)

        # Create temporary arrays used by grabCut
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)

        # Run grabCut
        cv2.grabCut(image_rgb, # Our image
                    mask, # The Mask
                    rectangle, # Our rectangle
                    bgdModel, # Temporary array for background
                    fgdModel, # Temporary array for background
                    5, # Number of iterations
                    cv2.GC_INIT_WITH_RECT) # Initiative using our rectangle

        # Create mask where sure and likely backgrounds set to 0, otherwise 1
        mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')

        # Multiply image with new mask to subtract background
        self.final  = image_rgb * mask_2[:, :, np.newaxis]
