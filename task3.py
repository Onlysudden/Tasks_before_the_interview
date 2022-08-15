"""Напишите функцию, которая принимает на вход строку, состояющую из символов '(' и ')', задающих скобочную последовательность, и возвращает True,
если последовательность корректна, иначе False."""

x = input()

def correct_brackets(x:str) -> bool:
    left_bracket = x.count("(")
    right_bracket = x.count(")")
    if left_bracket == right_bracket:
        return True
    return False

print(correct_brackets(x))