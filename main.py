import random
import time

print("Introdu numarul de elemente din lista de sortat: ", end="")
e = int(input())

print("Introdu limita inferioara a elementelor din lista de sortat:", end="")
inf = int(input())

print("Introdu limita superioara a elementelor din lista de sortat: ", end="")
sup = int(input())

a = [random.randint(inf, sup) for i in range(0, e)]
print("Lista de sortat =", end=" ")

print("Alege Sortarea:")
print("1. Bubble")
print("2. Insertion")
print("3. Selection")
print("4. Merge")
print("5. Quick")
print("6. Radix")
print("7. Heap")
print("Sortarea aleasa:", end=" ")
sort = int(input())


def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return



def insertionSort(arr):
    n = len(arr)

    if n <= 1:
        return

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selectionSort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

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
        m = l + (r - l) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)


def countingSort(arr, exp1):
    n = len(arr)

    output = [0] * (n)

    count = [0] * (10)

    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int((index) % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max1 = max(arr)

    exp = 1
    while max1 // exp > 0:
        countingSort(arr, exp)
        exp *= 10


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)


match sort:
    case 1:
        s = time.time()
        bubbleSort(a)
        print("Timpul de executie: ", end="")
        print(time.time() - s)
    case 2:
        s = time.time()
        insertionSort(a)
        print("Timpul de executie: ", end="")
        print(time.time() - s)
    case 3:
        s = time.time()
        selectionSort(a)
        print("Timpul de executie: ", end="")
        print(time.time() - s)
    case 4:
        s = time.time()
        mergeSort(a, 0, e-1)
        print("Timpul de executie: ", end="")
        print(time.time() - s)
    case 5:
        s = time.time()
        quickSort(a, 0, e-1)
        print("Timpul de executie: ", end="")
        print(time.time() - s)
    case 6:
        s = time.time()
        radixSort(a)
        print("Timpul de executie: ", end="")
        print(time.time() - s)
    case 7:
        s = time.time()
        heapSort(a)
        print("Timpul de executie: ", end="")
        print(time.time() - s)

