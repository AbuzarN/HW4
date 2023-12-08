swapquick=0
comparequick=0
swapmerge=0
comparemerge=0

import random as r
import time
def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swap =0;
    compare =0;
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            compare +=1
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap +=1
         
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            print("swaps: "+swap +" Compares: "+compare)
            return
    print("swaps: "+str(swap) +" Compares: "+str(compare))
def selectionSort(array):
    compare =0
    swap =0
    size = len(array)
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            compare+=1
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
        if (ind != min_index):swap+=1
        
    print("swaps: "+str(swap) +" Compares: "+str(compare))
def insertionSort(arr):
    compare =0
    swap=0
    
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            compare+=1
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        if arr[j+1]!=key :swap +=1
        arr[j+1] = key
       

    print("swaps: "+str(swap) +" Compares: "+str(compare))
# function to perform quicksort
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        global comparequick
        comparequick+=1
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            global swapquick
            swapquick+=1
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
# function to perform mergesort
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        global comparemerge
        comparemerge+=1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    global swapmerge
        
    while i < n1:
        arr[k] = L[i]
        swapmerge+=1
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        swapmerge+=1
        j += 1
        k += 1
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
#repeat test
def test(num, p, n):
    a=[]
    for i in range(n):
        r.shuffle(num)
        s=""
        start= time.time()

        if p == 1:
            bubbleSort(num);s="bubblesort"
        elif p == 2:
            selectionSort(num);s="selctionsort"
        elif p == 3:
            insertionSort(num);s="insertionsort"
        elif p == 4:
            global swapquick;global comparequick
            swapquick=0;comparequick=0
            quickSort(num,0,len(num)-1);s="quicksort"
            print("swaps: "+str(swapquick) +" Compares: "+str(comparequick))
        elif p == 5:
            global swapmerge;global comparemerge
            swapmerge=0;comparemerge=0
            mergeSort(num,0,len(num)-1);s="mergesort"
            print("swaps: "+str(swapmerge) +" Compares: "+str(comparemerge))
        end = time.time()
        a.append(end-start)

    print("The time of execution of "+ s +" program is :", (sum(a)/len(a)) * 10**3, "ms")

num = [i for i in range(50)]
n=10
for i in range (5):
    test(num,i+1,n)
