#Building data set for AI.
# Mashal Buhamad 2021
from PIL import Image
import PIL
import random
import concurrent.futures
import time
result = []
# Opening the primary image (used in background)
img1 = Image.open(r"paper.png")
width, height = img1.size
print (width,height)
# Opening the secondary image (overlay image)
img2 = Image.open(r"clip.png")
img2=img2.resize((round(img2.size[0]*.1), round(img2.size[1]*.1)))
width2, height2 = img2.size
print (width2,height2) 
 
# Pasting img2 image on top of img1 
with concurrent.futures.ProcessPoolExecutor() as executor:
    
    for i in range(random.randrange(10,90,1)):
        x=random.randrange(34, 500, 1)
        y=random.randrange(34, 390, 1)
        print (x,y)
        RT=img2.rotate(random.randrange(0,180,20),resample = PIL.Image.BICUBIC, expand = True)
        img1.paste(RT, (x,y), mask = RT)
# Displaying the image
img1.show()
print (i+1)