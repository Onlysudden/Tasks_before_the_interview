"""Напишите функцию, которая на вход принимает единственное целое число N, а возвращает целый квадратный корень из этого числа, если такой существует,
или None, если такого корня нет. Нельзя использовать функцию sqrt() из модуля math для извлечения квадратного корня."""

x = int(input())

def sqrt(x:int) -> int:
    n = 1
    while n ** 2 <= x:
        if n ** 2 == x:
            return n
        n += 1

print(sqrt(x))