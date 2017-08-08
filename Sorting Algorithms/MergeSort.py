import numpy as np

def mergesort(a): # A = Array to be sorted /p = 0 / l = length of A 
    p = 0
    l = len(a)
    if (len(a) == 1) or (len(a)== 0):
        return a    
                 
    mid = int((p + l) / 2)      #mid
    L = mergesort(a[0:mid])     #mergeSort the left
    R = mergesort(a[mid:l])     #mergeSort the right
    M = merge(L,R)              #MERGE 
        
    return M                  

def merge(B,C):      
    D = np.empty(len(B) + len(C))
    i = j = k = 0
    while k < (len(B) + len(C)):
        # check left Array is out of bounds
        if (i == len(B)):
             D[k] = C[j]
             j = j + 1
        # check right Array is out of bounds
        elif(j == len(C)):
            D[k] = B[i]
            i = i + 1
            
        elif B[i] < C[j]:
            D[k] = B[i]
            i = i + 1
        else:
            D[k] = C[j]
            j = j + 1
                
        k = k + 1
    return D

a = np.array([4,7,9,6,7,4,5,4,2])
a = mergesort(a)
print(a)

