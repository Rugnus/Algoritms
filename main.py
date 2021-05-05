import random
import time
import operator

N = int(input())
array = random.sample(range(0, N), N)
print(array)


# ----------------Декоратор----------------
def my_timer(f):
    def tmp(*args, **kwargs):
        ref_point = time.time()
        result = f(*args, **kwargs)
        delta_time = time.time() - ref_point
        print('Время выполнения функции {}'.format(delta_time))
        return result

    return tmp


# ----------------Вставками----------------
# @my_timer
# def insert_sort(array):
#     for index in range(1, len(array)):
#         currentVal = array[index]
#         currPos = index
#
#         while currPos > 0 and array[currPos - 1] > currentVal:
#             array[currPos] = array[currPos - 1]
#             currPos = currPos - 1
#         array[currPos] = currentVal
#
#
# insert_sort(array)
# print(array)


# ----------------Выбором----------------
# @my_timer
# def sel_sort(array):
#     for i in range(len(array) - 1):
#         m = i
#         j = i + 1
#         while j < len(array):
#             if array[j] < array[m]:
#                 m = j
#             j = j + 1
#         array[i], array[m] = array[m], array[i]
#
#
# sel_sort(array)
# print(array)


# ----------------Обменом----------------
# @my_timer
# def bubble_sort(array):
#     for i in range(N - 1):
#         for j in range(N - i - 1):
#             if array[j] > array[j + 1]:
#                 buffer = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = buffer
#
#
#
# bubble_sort(array)
# print(array)


# ----------------Слиянием----------------
# @my_timer
# def merge_sort(alist):
#     print("Разделение ",alist)
#     if len(alist)>1:
#         mid = len(alist)//2
#         left = alist[:mid]
#         right = alist[mid:]
#
#         merge_sort(left)
#         merge_sort(right)
#
#         i=0
#         j=0
#         k=0
#         while i<len(left) and j<len(right):
#             if left[i]<right[j]:
#                 alist[k]=left[i]
#                 i=i+1
#             else:
#                 alist[k]=right[j]
#                 j=j+1
#             k=k+1
#
#         while i<len(left):
#             alist[k]=left[i]
#             i=i+1
#             k=k+1
#
#         while j<len(right):
#             alist[k]=right[j]
#             j=j+1
#             k=k+1
#     print("Merging ",alist)
#
#
# merge_sort(array)
# print(array)


# ----------------Пирамидальная----------------
# def heapify(arr, n, i):
#     large = i
#     l = 2 * i + 1
#     r = 2 * i + 2
#
#     if l < n and arr[i] < arr[l]:
#         large = l
#
#     if r < n and arr[large] < arr[r]:
#         large = r
#
#     if large != i:
#         arr[i], arr[large] = arr[large], arr[i]
#         heapify(arr, n, large)
#
#
# @my_timer
# def heap_sort(arr):
#     n = len(arr)
#
#     for i in range(n // 2, -1, -1):
#         heapify(arr, n, i)
#
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#
#         heapify(arr, i, 0)
#
#
# heap_sort(array)
# n = len(array)
# for i in range(n):
#     print("%d " % array[i], end='')


# ----------------Быстрая----------------
@my_timer
def FastSort(array):
    elements = len(array)

    if elements < 2:
        return array

    curr_pos = 0

    for i in range(1, elements):
        if array[i] <= array[0]:
            curr_pos += 1
            temp = array[i]
            array[i] = array[curr_pos]
            array[curr_pos] = temp

    temp = array[0]
    array[0] = array[curr_pos]
    array[curr_pos] = temp

    left = QuickSort(array[0:curr_pos])
    right = QuickSort(array[curr_pos + 1:elements])

    array = left + [array[curr_pos]] + right

    return arr


print("Отсортированный массив: ", QuickSort(array))