
# importing the required modules
import os

from PIL import Image


# Function to compress the image
def compressImages(image_file):
    # accessing the image file
    filepath = os.path.join(os.getcwd(), image_file)
    # maximum pixel size
    maxwidth = 1200
    # opening the file
    image = Image.open(filepath)
    # Calculating the width and height of the original photo
    width, height = image.size
    # calculating the aspect ratio of the image
    aspectRatio = width / height

    # Calculating the new height of the compressed image
    newHeight = maxwidth / aspectRatio

    # Resizing the original image
    image = image.resize((maxwidth, round(newHeight)))

    # Saving the image
    filename = "compressed.png"
    image.save(filename, optimize=True, quality=85)
    return


# driver code
image_file = "/Users/mac/Downloads/IMG_6929.jpg"
# calling the function
compressImages(image_file)
print(
    "The given image has been compressed, download the files to notice the difference in file size."
)
