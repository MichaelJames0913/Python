 
import numpy as np

def insertionsort(a):
   for i in range(1,len(a),1): # i is the dividing line 
     temp = a[i]               # remove marked item 
     inner = i                 # starts shifts at i
     while inner>0 and a[inner-1] >= temp: # loop untill one is smaller
                a[inner] = a[inner-1]   #shift item to right
                inner -= 1              #go left one index
                a[inner] = temp         #insert marked item
          

a = np.array([10, 30, 18, 40, 1, 14, 78, 13])  
insertionsort(a)
print(a)

