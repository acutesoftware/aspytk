# as_image.py   written by Duncan Murray 6/7/2013 (C) Acute Software
# Acute Software library of functions for image manipulation

import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter

def TEST():
    # todo - make a jpg from desktop or something, use that as a test
    print(" \n --- Testing Image functions--- ")
    print(" ------------------------------ ")
    fileName = GetRandomImage("sunset", 1, "")
    tempFileList = ["resized_" + fileName, "contour_" + fileName, "text_" + fileName]
    resize(fileName, 600, tempFileList[0]) 
    filterContour(fileName, tempFileList[1])    
    addTextToImage(fileName, "This is a test", tempFileList[2])
    return tempFileList
    
    
def GetRandomImage(searchString, searchResultPosition, baseFileName):
    # searches Google images for searchString and returns the nth value and saves to 'fileName'
    return 'sunset.jpg'  # todo - implement this
        
def resize(fname, basewidth, opFilename):
    #print("HELLO")
    if basewidth == 0:
        basewidth = 300
    print("Resizing ", fname, " to ", basewidth, " pixels wide")
    img = Image.open(fname)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    img.save(opFilename)
    
    
def addTextToImage(fname, txt, opFilename):
    ft = ImageFont.load("C://user//dev//src//python//_AS_LIB//timR24.pil")  # Font - google name and download
    wh = ft.getsize(txt)
    print("Adding text '", txt, "' to", fname)
    im = Image.open(fname)
    draw = ImageDraw.Draw(im)
    # draw text in center 
    #draw.text((im.size[0]/2 - wh[0]/2, im.size[1]/2 + 20), txt, fill=(255, 255, 0), font=ft)
    # draw text on top left
#    draw.text((0, 0), txt, fill=(255, 255, 0), font=ft)
    draw.text((0, 0), txt, fill=(0, 0, 0), font=ft)
    del draw  
    im.save(opFilename)
    
def addCrossHairToImage(fname, opFilename):
    im = Image.open(fname)
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=(255, 255, 255))
    draw.line((0, im.size[1], im.size[0], 0), fill=(255, 255, 255))
    del draw  
    im.save(opFilename)

def filterContour(imageFile, opFile):
    print("Contouring ", imageFile, " to ", opFile)
    im = Image.open(imageFile)
    im1 = im.filter(ImageFilter.CONTOUR)
    im1.save(opFile)

def DetectFace(fname, opFile):
    storage = cv.CreateMemStorage()
    haar=cv.LoadHaarClassifierCascade('haarcascade_frontalface_default.xml')
    detected = cv.HaarDetectObjects(fname, haar, storage, 1.2, 2,cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))
    if detected:
        for face in detected:
            print (face)
            