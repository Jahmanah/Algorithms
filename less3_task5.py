# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве
import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)
print('*' * 40)

i = 0
max_min = -1
while i < SIZE:
    if arr[i] < 0 and max_min == -1:
        max_min = i
    elif arr[i] < 0 and arr[i] > arr[max_min]:
        max_min = i
    i += 1

print(f'Позиция: {max_min}; Значение: {arr[max_min]}')