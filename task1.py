"""Напишите функцию, которая на вход принимает строку, состоящую из строчных и заглавных латинских символов, а возвращает кортеж из двух элементов:
cимвола, который встречается в строке чаще всего (без учета регистра!), и числа вхождений этого символа в строку.
Если таких символов несколько, функция должна вернуть любой из них. Например, для строки "aaaAAAbc" результатом работы функции будет ('a', 6)."""

x = input()

def count_max(x:str) -> tuple:
    new_x = x.lower()
    letters = []
    max_q = 0
    for elem in new_x:
        if elem not in letters:
            quantity = new_x.count(elem)
            if max_q < quantity:
                max_q = quantity
                max_elem = elem
            letters.append(elem)
    
    return (max_elem, max_q)

print(count_max(x))