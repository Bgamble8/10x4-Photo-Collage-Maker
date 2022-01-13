import cv2
import numpy as np
from numpy.core.shape_base import vstack
from PIL import Image
import os

def script(color):

    path = "C:\\Users\\bryan\\Documents\\Python_Envs\\Etsy_Upload_Bot\\Products\\raw\\" + color

    try:
        os.mkdir("C:\\Users\\bryan\\Documents\\Python_Envs\\Etsy_Upload_Bot\\Products\\resized\\" + color)
    except FileExistsError:
        print("Folder exisits")

    def loadImages(path = "."):
        return [os.path.join(path,f) for f in os.listdir(path)]

    def collage(path):
        files = loadImages(path)
        images = []
        for file in files:
            img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
            img = cv2.resize(img,(200,300))
            images.append(img)
        row1,row2,row3,row4 = [],[],[],[]
        count = 0
        while count < 40:
            row1.append(images[count])
            count += 1
            row2.append(images[count])
            count += 1
            row3.append(images[count])
            count += 1
            row4.append(images[count])
            count += 1

        h_stack1 = np.hstack(row1)
        h_stack2 = np.hstack(row2)
        h_stack3 = np.hstack(row3)
        h_stack4 = np.hstack(row4)

        v = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4])
        cv2.imwrite("C:\\Users\\bryan\\Documents\\Python_Envs\\Etsy_Upload_Bot\\Products\\temp\\thumb.png",v)

        background = Image.open('C:\\Users\\bryan\\Documents\\Python_Envs\\Etsy_Upload_Bot\\Products\\temp\\thumb.png')
        overlay = Image.open('C:\\Users\\bryan\\Documents\\Python_Envs\\Etsy_Upload_Bot\\images\\overlay.png')

        background.paste(overlay, (0, 0), overlay)

        background.save("C:\\Users\\bryan\\Documents\\Python_Envs\\Etsy_Upload_Bot\\Products\\thumbnails\\"+color+".png")

    def resize(path):
        files = loadImages(path)
        i = 0
        for file in files:
            img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
            imgResized = cv2.resize(img,(1200,1800))
            cv2.imwrite(("C:\\Users\\bryan\\Documents\\Python_Envs\\Etsy_Upload_Bot\\Products\\resized\\" +color+ "\\cropped%i.png" %i) ,imgResized)
            i += 1


    collage(path)
    resize(path)
