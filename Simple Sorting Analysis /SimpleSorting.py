"""
Created on Sat Jun 25 12:31:40 2016

@author: Michael Schmidt
"""
import numpy as np
import matplotlib.pyplot as plt
import timeit
import random
from matplotlib.legend_handler import HandlerLine2D
#Question 1
#implement Sorting algorithms
#//////////////////////////////////////////////////////////////////////////////
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1): # outer loop 
        for i in range(passnum):    # inner loop
            if alist[i]>alist[i+1]:  # if the element in the next index is greater 
                temp = alist[i]      # then swap the two elements 
                alist[i] = alist[i+1]
                alist[i+1] = temp
#//////////////////////////////////////////////////////////////////////////////
def selectionsort(a):
    if (len(a) == 1) or (len(a)== 0):
        return a
    for i in range(0,len(a),1): # outer loop
        mIn = a[i]              # minimum value
        mInlnd = i              
        for j in range(i,len(a),1):# inner loop
            if a[j] < mIn:         # If min greater 
                mIn = a[j]         # there's a new min 
                mInlnd = j         # swap
                temp = a[i]
                a[i] = a[mInlnd]
                a[mInlnd] = temp
    return a
#//////////////////////////////////////////////////////////////////////////////
def insertionsort(a):
   if (len(a) == 1) or (len(a)== 0):
       return a 
   for i in range(1,len(a),1): # i is the dividing line 
     temp = a[i]               # remove marked item 
     inner = i                 # starts shifts at i
     while inner>0 and a[inner-1] >= temp: # loop untill one is smaller
                a[inner] = a[inner-1]   #shift item to right
                inner -= 1              #go left one index
                a[inner] = temp         #insert marked item   
   return a
#//////////////////////////////////////////////////////////////////////////////
#For n in [100,200,300,...,10000] feed each algorithmthe following two 
#instances a fully sorted array of length n and a reverse sorted array 
#of length n
#input size array 
A = np.arange(101)*100
inputSize = np.delete(A,0)
#magic number for now
n = 100
"""
#////////////////////////////////////////////////////////////////////////////// 
#/////////////////////sorting analysis on BUBBLE_SORT//////////////////////////
#arrays to store plotting coordinate info
#bubbleSort coordinate info
A_t_sort_bubbleSort = np.empty(n) # array to store sorted times (y coordinates)    
A_t_rev_bubbleSort = np.empty(n)  # array to store reversed times (y coordinates)
A_t_ran_bubbleSort = np.empty(n)  # array to store random times (y coordinates)
A_n_bubbleSort = np.empty(n)      # number of elements same for all 
#Plot1
# on each iteration create an array where (100 * i) = size of array 
# when n = 1 - 100 numbers when n = 2  - 200 numbers.....when n = 100 - 10,000
for i in range(n): 
    print("_____BubbleSort____________________________")
    print("iteration: ", i)
    # create arrays for sorting 
    A_sorted = np.arange(inputSize[i]) # create sorted array
    A_reverse = A_sorted[::-1]         # create reverse sorted array 
    A_ran = np.arange(inputSize[i])    # create a array for random array
    random.shuffle(A_ran)              # shuffle the array into random array 
    print("number of elements: ", A_sorted.size)
    # timeit and calls 
    t_sort = timeit.Timer(lambda: bubbleSort(A_sorted))  
    t_rev = timeit.Timer(lambda: bubbleSort(A_reverse))
    t_ren = timeit.Timer(lambda: bubbleSort(A_ran))
    # store time info 
    A_t_sort_bubbleSort[i] = t_sort.timeit(number=1) # y_coordinate for sorted 
    A_t_rev_bubbleSort[i] = t_rev.timeit(number=1) # y_coordinate for reversed   
    A_t_ran_bubbleSort[i] = t_ren.timeit(number=1) # y_coordinate for random
    A_n_bubbleSort[i] = inputSize[i] # n is the x coordinate 
    # print times     
    print("Sorted Time: ", t_sort.timeit(number =1))
    print("reversed Time: ", t_rev.timeit(number = 1))
    print("random time: ", t_ren.timeit(number = 1))
    print("___________________________________________")   
#draw plot 1 
plt.figure(1) #figure one is selectionSort Graph
plt.title("bubble sort analysis")
plt.ylabel("execution time in sec")
plt.xlabel("size of array (n)")
#x-axis of plots is n, the input size
#y-axis execution time
line1, = plt.plot(A_n_bubbleSort, A_t_sort_bubbleSort,'r--', label="sorted array")
line2, = plt.plot(A_n_bubbleSort , A_t_rev_bubbleSort, 'bs', label="reversed array") 
line3, = plt.plot(A_n_bubbleSort, A_t_ran_bubbleSort, 'g^',label="random array")
#legend
plt.legend(handler_map={line1: HandlerLine2D(numpoints=1)}, loc=2)
plt.show(1)
#//END_bubbleSort//////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////
#/////////////////////sorting analysis on SELECTION_SORT///////////////////////
#arrays to store plotting coordinate info
#bubbleSort coordinate info
A_t_sort_select = np.empty(n) 
A_t_rev_select = np.empty(n)
A_t_ran_select = np.empty(n)
A_n_select = np.empty(n)
for i in range(n):
    print("_____SELECTION_SORT____________________________")
    print(i)
    A_sorted = np.arange(inputSize[i])
    A_reverse = A_sorted[::-1]
    A_ran = np.arange(inputSize[i])    #create a array for random 
    random.shuffle(A_ran)               #shuffle the array
    #RUN selectionsort 
    t_sort = timeit.Timer(lambda: selectionsort(A_sorted))
    t_rev = timeit.Timer(lambda: selectionsort(A_reverse))
    t_ren = timeit.Timer(lambda: selectionsort(A_ran))
    #storing time and size variables in arrays
    A_t_sort_select[i] = t_sort.timeit(number=1)
    A_t_rev_select[i] = t_rev.timeit(number=1)
    A_t_ran_select[i] = t_ren.timeit(number=1) # y_coordinate for random
    A_n_select[i] = inputSize[i] # n is the x coordinate 
    print("Sorted Time: ", t_sort.timeit(number =1))
    print("reversed Time: ", t_rev.timeit(number = 1))
    print("random time: ", t_ren.timeit(number = 1))      
    #plot points
    #plt.plot(i,t_sort.timeit(number=1), 'bs', i, t_rev.timeit(number=1), 'g^')
    print("_________________________________")
#draw Plot 1 
plt.figure(1) #figure one is selectionSort Graph
plt.title("selection Sort analysis")
plt.ylabel("execution Time")
plt.xlabel("size of array (n)")
line1, = plt.plot(A_n_select, A_t_sort_select,'r--', label="sorted array")
line2 = plt.plot(A_n_select , A_t_rev_select, 'bs', label="reversed array")
line3 = plt.plot(A_n_select, A_t_ran_select, 'g^', label="random array")
#legend
plt.legend(handler_map={line1: HandlerLine2D(numpoints=1)}, loc=2)

plt.show(1)
#//END_SELECTION_SORT//////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////
#////////////////////////sorting analysis on INSERTIONSORT/////////////////////
#insertion sort
# create empty array to store time data 
A_t_sort_insert = np.empty(n) 
A_t_rev_insert = np.empty(n)
A_t_ran_insert = np.empty(n)
A_n_insert = np.empty(n)
#Run It
for i in range (n):
    print("_____INSERTION_SORT______________")
    print(i)  
    A_sorted = np.arange(inputSize[i])
    A_reverse = A_sorted[::-1]
    ran = np.arange(inputSize[i])
    random.shuffle(ran)  
    #RUN Insertion Sort 
    t_sort = timeit.Timer(lambda: insertionsort(A_sorted))
    t_rev = timeit.Timer(lambda: insertionsort(A_reverse))
    r_ran = timeit.Timer(lambda: insertionsort(ran))    
    #storing time and size variables in arrays
    A_t_sort_insert[i] = t_sort.timeit(number = 1)
    A_t_rev_insert[i] = t_rev.timeit(number = 1)
    A_t_ran_insert[i] = r_ran.timeit(number = 1 )
    A_n_insert[i] = inputSize[i]  
    print(t_sort.timeit(number = 1))
    print(t_rev.timeit(number = 1)) 
    print(r_ran.timeit(number = 1))
    print("_________________________________")   
#draw Plot 
plt.figure(1) #figure one is selectionSort Graph
plt.title("insertion sort analysis")
plt.ylabel("execution time")
plt.xlabel("size of array (n)")
line1, = plt.plot(A_n_insert, A_t_sort_insert, 'bs', label = "sorted array")
line2, = plt.plot(A_n_insert, A_t_rev_insert, 'g^' , label = "reversed array")
line3, = plt.plot(A_n_insert, A_t_ran_insert, 'r--' , label = "random array")
#legend
plt.legend(handler_map={line2: HandlerLine2D(numpoints=1)}, loc=2)
#//END_INSERTION_SORT//////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////
plt.show(1)
"""
#//////////////////////////////////////////////////////////////////////////////
#////////////////////////Simple Sorting analysis///////////////////////////////

A_t_bubbleSort = np.empty(n)    
A_t_selectionSort = np.empty(n)  
A_t_insertionSort = np.empty(n)  
A_n = np.empty(n)      

for i in range(n): 
    print("_____Simple Sorting analysis____________________________")
    print("iteration: ", i)
    # create arrays for sorting, these arrays will be randomized array of size n

    A_ran = np.arange(inputSize[i])
    random.shuffle(A_ran)             
    
    A_ran2 = np.arange(inputSize[i])    
    random.shuffle(A_ran2) 
    
    A_ran3 = np.arange(inputSize[i])    
    random.shuffle(A_ran3) 
    
    print("number of elements: ", A_ran.size)
 
    t_bubble = timeit.Timer(lambda: bubbleSort(A_ran))  
   
    t_select = timeit.Timer(lambda: selectionsort(A_ran2))
    
    t_insertion = timeit.Timer(lambda: insertionsort(A_ran3))
    
    A_t_bubbleSort[i] = t_bubble.timeit(number=1) 
    A_t_selectionSort[i] = t_select.timeit(number=1)   
    A_t_insertionSort[i] = t_insertion.timeit(number=1) 
    A_n[i] = inputSize[i] 
    
    print("bubble Sort time: ", t_bubble.timeit(number =1))
    print("selection Sort time: ", t_select.timeit(number = 1))
    print("insertion Sort time: ", t_insertion.timeit(number = 1))
    print("___________________________________________")   
    
#draw plot 1 
plt.figure(1) #figure one is selectionSort Graph
plt.title("Simple Sorting analysis (sorting of random array)")
plt.ylabel("execution time in sec")
plt.xlabel("size of array (n)")
#x-axis of plots is n, the input size
#y-axis execution time
line1, = plt.plot(A_n, A_t_bubbleSort,'r--', label="bubble Sort")
line2, = plt.plot(A_n , A_t_selectionSort, 'bs', label="selection Sort") 
line3, = plt.plot(A_n, A_t_insertionSort, 'g^',label="insertion Sort")
#legend
plt.legend(handler_map={line1: HandlerLine2D(numpoints=1)}, loc=2)
plt.show(1)


