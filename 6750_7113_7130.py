import random
import time
import numpy as np

#Insertion Sort
def insertionSort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >=0 and key < arr[i]:
            arr[i+1] = arr[i]
            i=i-1
        arr[i+1] = key
#Selection Sort
def selectionSort(array, size):
        for i in range(0, size - 2):
            min_i = i
            for j in range(i + 1, size - 1):

                if array[j] < array[min_i]:

                    min_i = j
            (array[i], array[min_i]) = (array[min_i], array[i])


def kthSmallest(arr, first, last, k):
    if (k > 0 and k <= len(arr)):
        pos = randompartition(arr, first, last)
        if (pos - first == k - 1):
            return arr[pos]
        if (pos - first > k - 1):
            return kthSmallest(arr, first, pos - 1, k)

        return kthSmallest(arr, pos + 1, last, k - pos + first - 1)

    return (print("out of range"))
#Random Partioning Random Pivot is the last element
def randompartition(arr,first,last):
    randpiv= random.randint(first,last)
    arr[first],arr[randpiv]= arr[randpiv],arr[first]
    return partition(arr,first,last)
def partition(arr,first,last):
    pivot = random.randint(first, last)
    arr[pivot], arr[last] = arr[last], arr[pivot]
    pivot=last
    i=first-1
    for j in range (first,last):
        if (arr[j]<=arr[pivot]):
            i = i + 1
            arr[i],arr[j]= arr[j],arr[i]
    arr[last],arr[i+1]= arr[i+1] , arr[last]
    #pivot=i+1
    return(i+1)
def quick_sort(arr,first,last):
        if (first<last):
            q=randompartition(arr,first,last)
            quick_sort(arr,first,q-1)
            quick_sort(arr,q+1,last)
 #Merge Sort
def merge(arr, l, M, r):
    n1 = M - l + 1
    n2 = r - M
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[M + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
def mergeSort(arr, l, r):
    if l < r:
        M = l + (r - l) // 2
        mergeSort(arr, l, M)
        mergeSort(arr, M + 1, r)
        merge(arr, l, M, r)
def mergePlusSelection(arr, l, r, T):
    if l < r:
        M = l + (r - l) // 2
        if M <= T:
            return selectionSort(arr, len(arr))
        else:
            mergeSort(arr, l, M)
            mergeSort(arr, M + 1, r)
            merge(arr, l, M, r)
if __name__ == "__main__":
    print('        **WELCOME TO OUR SORTING TECHNIQUES IMPLIMENTATION**')
    randnums = np.random.randint(1, 84605202, 100000)
    arr = randnums
    print('Random Array Not Sorted:')
    print(arr)
    start_time = time.time()
    insertionSort(arr)
    print('Array After InsertionSort : ')
    print(arr)
    print("*****Runtime of Insertion Sort=%s milliseconds " % (1000 * (time.time() - start_time)))
    start_time = time.time()
    quick_sort(arr, 0, len(arr) -1)
    print('After Quick Sort')
    print(arr)
    print("*****Runtime of Quick Sort=%s milliseconds " % (1000 * (time.time() - start_time)))
    start_time = time.time()
    size = len(arr)
    selectionSort(arr, size + 1)
    quick_sort(arr, 0, len(arr) - 1)
    print('After Selecction Sort')
    print(arr)
    print("*****Runtime of Selection Sort=%s milliseconds " % (1000 * (time.time() - start_time)))
    start_time = time.time()
    mergeSort(arr, 0, len(arr) - 1)
    print('After Megre Sort')
    print(arr)
    print("*****Runtime of Merge Sort=%s milliseconds " % (1000 * (time.time() - start_time)))
    print('               *****Using Hybrid*****')
    mergePlusSelection(arr, 0, len(arr) - 1, len(arr) - 5)
    print("Sorted array is: ")
    print(arr)
    x = input("Enter the order of the smallest element: ")
    k = int(x)
    print("K'th smallest element is", kthSmallest(arr, 0, len(arr) - 1, k))