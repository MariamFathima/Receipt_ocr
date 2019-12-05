import base64

from os import walk

mypath = "/home/xia/projects/Receipts/"

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
imagefile = open("images.txt", "a")

for file in f:
    with open(imagefile, "rb" ) as image_file:
        encoded_string = base64.b64encode(image_file.read())
        imagefile.write(encoded_string+"\n")

imagefile.close()