import os
from PIL import Image
from array import *
from random import shuffle
from PIL import ImageFilter
import base64




    
hexval= "{0:o}".format(2051)
print(hexval)


k= 'franck'

print(k.encode("utf32"))
o= k.encode("utf32")

def franckoEncoder(value, base):
        value= str(value)
        try:
               valueBase= int(value,base)
               print('Your value in base {0:*^5} is {1:*^5}'.format(base,valueBase))
               print()
               print('binaryForm: {0:*^8b}, {0:#b}, base8Form: {0:*^5o}, {0:#o}, hexagonalForm: {0:*^5x}, {0:#x}'.format(valueBase))
               print()
               print('further encoding transformation')
               print('binaryForm: {0:#0{1}b}, {0:#0{2}b}, {0:#0{3}b}'.format(valueBase,6,10,18))
               print('base8Form: {0:#0{1}o}, {0:#0{2}o}, {0:#0{3}o}'.format(valueBase,6,10,18))
               print('hexagonalForm: {0:#0{1}x}, {0:#0{2}x}, {0:#0{3}x}'.format(valueBase,6,10,18))
               
        except ValueError as err:
               print('Your value is incorrect',err)

        except TypeError as err:
               print('your base is not valid',err)

        
                
              
                
             
franckoEncoder('xff',12)
