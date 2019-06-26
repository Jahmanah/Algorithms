# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)
print('*' * 40)

min_ = 0
max_ = 0
for i in range(SIZE):
    if arr[i] < arr[min_]:
        min_ = i
    elif arr[i] > arr[max_]:
        max_ = i

temp = arr[min_]
arr[min_] = arr[max_]
arr[max_] = temp

print(arr)