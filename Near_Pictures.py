import PIL
from PIL import Image
from os import listdir
from os.path import isfile, join

def ImageConfig(JpgName,JpgFront):
    basewidth = 1080
    img = Image.open(JpgName)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save(JpgName)
    
    #---

    image = Image.open(JpgName)
    logo = Image.open(JpgFront)
    image_copy = image.copy()
    position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
    # modify the paste by adding the logo as the third argument as per the explanation above.
    image_copy.paste(logo, position, logo)

    image_copy.save(JpgName)
    
def JpegFiles():
    Files=[]
    for i in [f for f in listdir() if isfile(join( f))]:
        if ".jpg" in i or ".jpeg" in i:
            Files.append(i)
    return Files


for Name in JpegFiles():
    ImageConfig(Name,"/home/harvey/Urge_Photo/_Logo.png")
