# На вход подаётся математическое выражение.
# Элементы - числа. Операции - "+ - * /".
# Также есть скобочки. Окончанием выражения служит "=".
# Программа должна вывести результат выражения
# Пример ввода:
# 2+7*(3/9)-5=
# Замечание:
# Программа также должна делать "проверку на дурака": нет деления на 0,
# все скобки стоят верно (см лабу №1) и т.п.

def validate_and_calculate(expression):
    # Проверка, что выражение заканчивается на символ "="
    if '=' not in expression: return "Ошибка: выражение должно заканчиваться на символ '='"

    try:
        # Убираем символ "=" в конце выражения
        expression = expression.strip("=")
        # Выполняем вычисление выражения
        return str(parse_and_evaluate_expression(expression))
    except ZeroDivisionError:
        # Обработка ошибки деления на ноль
        return "Деление на ноль невозможно"
    except Exception as e:
        # Обработка других ошибок
        return f"{e}"

def parse_and_evaluate_expression(expression):
    # Преобразуем строку в список токенов (чисел и операторов)
    tokens = split_into_tokens(expression)
    # Преобразуем инфиксное выражение в постфиксное
    postfix = convert_infix_to_postfix(tokens)
    # Вычисляем результат постфиксного выражения
    return compute_postfix(postfix)

def split_into_tokens(expression):
    # Преобразует строку выражения в список токенов (чисел и операторов)
    tokens = []
    current_token = ""
    for char in expression:
        # Если символ — цифра или точка, продолжаем формировать токен (число)
        if char.isdigit() or char == '.':
            current_token += char
        else:
            # Если накоплен токен (число), добавляем его в список
            if current_token:
                tokens.append(current_token)
                current_token = ""
            # Если символ не пробел, добавляем его как отдельный токен (оператор или скобка)
            if char != ' ':
                tokens.append(char)
    # Если в конце есть не добавленное число, добавляем его
    if current_token:
        tokens.append(current_token)
    return tokens

def convert_infix_to_postfix(tokens):
    # Преобразует инфиксное выражение (с обычными скобками и операторами) в постфиксную запись
    output = []  # Здесь будут храниться операнды в постфиксном порядке
    stack = []    # Здесь будут храниться операторы и скобки
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}  # Приоритет операторов

    for token in tokens:
        # Если токен — число, добавляем его в выходной список
        if token.replace('.', '', 1).isdigit():
            output.append(token)
        # Если токен — открывающая скобка, помещаем её в стек
        elif token == '(':
            stack.append(token)
        # Если токен — закрывающая скобка, переносим операторы из стека в выходной список до открытия скобки
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Убираем '(' из стека
        else:  # Оператор
            # Переносим операторы из стека в выходной список, если их приоритет больше или равен текущему
            while stack and stack[-1] != '(' and precedence[token] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)  # Добавляем текущий оператор в стек

    # Переносим оставшиеся операторы из стека в выходной список
    while stack:
        output.append(stack.pop())

    return output

def compute_postfix(tokens):
    # Оценка постфиксного выражения
    stack = []
    for token in tokens:
        # Если токен — число, добавляем его в стек
        if token.replace('.', '', 1).isdigit():
            stack.append(float(token))
        else:  # Оператор
            # Извлекаем два операнда из стека
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Применяем операцию в зависимости от текущего оператора
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                if operand2 == 0:
                    raise ZeroDivisionError("Деление на ноль невозможно")
                stack.append(operand1 / operand2)
    # В стеке останется единственный элемент — результат выражения
    return stack.pop()

# Пример использования:
# (2+3)*2=
expression = input("Введите выражение (должно заканчиваться на '='): ")
result = validate_and_calculate(expression)
print(result)

