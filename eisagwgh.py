import math    #eisagei vivliothikh gia math
import random
import os
import numpy
import functions


metavlhth=math.sqrt(16)
print(metavlhth)

metavlhth2=random.uniform(1,metavlhth)
print(metavlhth2)

print(os.getcwd())   #printarei to current directory sto operating system aka os
osdirectory = os.getcwd()
print(os.listdir(osdirectory))  #printarei ta arxeia sto osdirectory a.k.a. list directory

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)

print (functions.my_function(10, 3))    #kalw th my_function apo to functions