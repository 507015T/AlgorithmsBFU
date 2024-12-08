
# (Задача состоит из двух пунктов, но вы можете не париться и делать сразу второй)
# На вход подаётся строка, состоящая из скобок. Программа должна определить
# правильность введённого скобочного выражения. Савкин сказал, что программа
# должна работать на русском языке: "Введите строку", "Строка не существует", "Строка существует" и т.п.
# Пункт 1: В строке будут скобки только одного типа: или "()" , или "{}", или "[]"
# Пункт 2: В строке будут все три вида скобок
# Для успешной сдачи лабы оба пункта программа должна выполнять корректно
# (можно сделать отдельные программы на каждый пункт)
# Пример входа:
# ()[({}())]


def correct_brackets(string):
    while '()' in string or '[]' in string or '{}' in string:
        string = string.replace('()', '')
        string = string.replace('[]', '')
        string = string.replace('{}', '')

    return "Строка существует" if not string else "Строка не существует"


if __name__ == "__main__":
    print(correct_brackets(input("Введите строку:\n")))


# Pytests
def test1():
    assert correct_brackets('(((())))') == "Строка существует"


def test2():
    assert correct_brackets('(((())') == "Строка не существует"


def test3():
    assert correct_brackets('())))') == "Строка не существует"


def test4():
    assert correct_brackets('((((){}[]{}[])))') == "Строка существует"


def test5():
    assert correct_brackets('(){}[]{}[])))') == "Строка не существует"


def test6():
    assert correct_brackets('(){}[]{}[]') == "Строка существует"