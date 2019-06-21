# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
def max_summ(a):
    n = 0
    m = 0
    while a > 0:
        n = a % 10
        m += n
        a = a//10
    return m

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

# print(max_summ(a))
# print(max_summ(b))
# print(max_summ(c))

max = max_summ(a)
max_num = a

if max < max_summ(b):
    max = max_summ(b)
    max_num = b
elif max < max_summ(c):
    max = max_summ(c)
    max_num = c

print(f'Наибольшая сумма цифр у числа {max_num}, она равна {max}')
