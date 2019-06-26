# Определить, какое число в массиве встречается чаще всего.
import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)
print('*' * 40)

arr_count = []
arr.append(None)
count = 1
i = MIN_ITEM

while MIN_ITEM <= i <= SIZE and arr[i] != None:
    if arr[i] == arr[i+1]:
        count += 1
        print(count)
        print(arr)
    i += 1
    arr.pop(0)
    arr.append(None)

#     elif
# arr_count[i] = count
print(arr_count)

# Задумка в том, чтобы сравнивать первый элемент массива с последующими и при совпадении, увеличивать count +=1. В конце
# итерации значение count записывать в массив arr_count с индексом, который был у проверяемого элемента и удалять
# первое значение массива arr. После окончания цикла найти максимальное значение в массиве arr_count и по индексу этого
# значения вывести значение из arr. Но чего-то не работает
