import os
from PIL import Image
from array import *
from random import shuffle
from PIL import ImageFilter
import unicodedata


# Make sure that your folders have the same names as written in first portion of each set of the names array
# Load from and save to

Names = [['./training_images','train'], ['./testing_images','test']]

for name in Names:
    
    data_image = array('B')
    data_label = array('B')

    FileList = []
    for dirname in os.listdir(name[0]):
             path= os.path.join(name[0],dirname)
             FileList.append(path)
                     
    shuffle(FileList)

    #make sure that your label are numbers
    for filename in FileList:
        label = filename.split('\\')[1]
        ways= 0
        for i in label:
            ways = ways + 1
            if i == '.':
                label= label[:ways-1]
                break
        convertLabel = int(label)

        data_label.append(convertLabel)
        
        Im = Image.open(filename)
        newImg= Im.convert('L')
        pixel = newImg.load()
        width, height = Im.size

        for x in range(0,width):
            for y in range(0,height):
                data_image.append(pixel[x,y])
                
         
    hexval = "{0:#0{1}x}".format(len(FileList),6)
    header= array('B')
    header.extend([0,0,8,1,0,0])
    header.append(int('0x'+hexval[2:][:2],16))
    header.append(int('0x'+hexval[2:][2:],16))
    print()
    k='The hex value for {0:*^10} set is {1:*^10} and Array is'.format(name[1],hexval)
    print(k)
    data_label= header + data_label
    print(data_label)

    if max([width, height]) <=256:
        header.extend([0,0,0,width,0,0,0,height])
    else:
        raise ValueError('Image exceeds maximum size')    
        

    header[3]= 3 #Chainging MSB for image data (0x00000803)

    data_image= header + data_image   

    output_file = open(name[1]+'-images-idx3-ubyte', 'wb')
    data_image.tofile(output_file)
    output_file.close()

    output_file =open(name[1]+'-labels-idx1-ubyte', 'wb')
    data_label.tofile(output_file)
    output_file.close()

#gzip resulting files

for name in Names:
    os.system('gzip '+name[1]+'-images-idx3-ubyte')
    os.system('gzip '+name[1]+'-labels-idx1-ubyte')
    

#references
#https://github.com/gskielian/JPG-PNG-to-MNIST-NN-Format
