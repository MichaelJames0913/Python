def selectionsort(a):
    for i in range(0,len(a),1): #outer loop
        mIn = a[i]              #minimum value
        mInlnd = i              
        for j in range(i,len(a),1):#inner loop
            if a[j] < mIn:         # If min greater 
                mIn = a[j]         # there's a new min 
                mInlnd = j         # swap
                temp = a[i]
                a[i] = a[mInlnd]
                a[mInlnd] = temp

a = [5,4,2,3,1,6,9]
selectionsort(a)
print(a)