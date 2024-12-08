rlass Node:
    # Конструктор для узла бинарного дерева
    def __init__(self, key):
        self.left = None  # Левый потомок узла
        self.right = None  # Правый потомок узла
        self.val = key  # Значение узла

    # Прямой рекурсивный обход (Pre-order)
    # Корень -> Левое поддерево -> Правое поддерево
    def traversePreOrder(self) -> None:
        # Печатаем значение текущего узла
        print(self.val, end=' ')
        # Если есть левый потомок, рекурсивно обходим его
        if self.left:
            self.left.traversePreOrder()
        # Если есть правый потомок, рекурсивно обходим его
        if self.right:
            self.right.traversePreOrder()

    # Центральный(Симметричный) рекурсивный обход (In-order)
    # Левое поддерево -> Корень -> Правое поддерево
    def traverseInOrder(self) -> None:
        # Если есть левый потомок, рекурсивно обходим его
        if self.left:
            self.left.traverseInOrder()
        # Печатаем значение текущего узла
        print(self.val, end=' ')
        # Если есть правый потомок, рекурсивно обходим его
        if self.right:
            self.right.traverseInOrder()

    # Концевой(Обратный) рекурсивный обход (Post-order)
    # Левое поддерево -> Правое поддерево -> Корень
    def traversePostOrder(self) -> None:
        # Если есть левый потомок, рекурсивно обходим его
        if self.left:
            self.left.traversePostOrder()
        # Если есть правый потомок, рекурсивно обходим его
        if self.right:
            self.right.traversePostOrder()
        # Печатаем значение текущего узла после обхода всех потомков
        print(self.val, end=' ')

    # Прямой обход (Non-recursive Pre-order) с использованием стека
    # Корень -> Левое поддерево -> Правое поддерево
    def nonRecursiveTraversePreOrder(self) -> None:
        # Используем стек для обхода дерева
        stack = [self]  # Инициализируем стек с корнем дерева
        result = []  # Список для хранения значений обхода

        # Пока стек не пустой, извлекаем элементы
        while stack:
            node = stack.pop()  # Извлекаем узел из стека
            result.append(node.val)  # Добавляем значение текущего узла в результат обхода

            # Если у узла есть правый потомок, кладем его в стек
            if node.right:
                stack.append(node.right)

            # Если у узла есть левый потомок, кладем его в стек
            # Левый потомок кладется в стек последним, так как мы его должны обработать первым
            if node.left:
                stack.append(node.left)

        # Выводим результат обхода в виде строки
        print(" ".join(map(str, result)))




def create_tree(string: str) -> Node:
    # Создание дерева из строкового представления с использованием подфункции
    return create_subtree(string, 0, len(string))

def find_right_subtree(string: str, start: int, end: int):
    # Функция для нахождения позиции начала правого поддерева
    bracket_counter = -1  # Счетчик для отслеживания парных скобок
    while True:
        if (start >= end): return -1  # Если достигнут конец строки, выходим
        if ((string[start] == ',') and (bracket_counter == 0)): return start + 1  # Находим запятую после левого поддерева
        if string[start] == '(': bracket_counter += 1  # Открывающая скобка увеличивает счетчик
        if string[start] == ')': bracket_counter -= 1  # Закрывающая скобка уменьшает счетчик
        start += 1

def create_subtree(string: str, start: int, end: int) -> Node:
    # Создание поддерева для строки между start и end
    while string[start] == ' ' or string[start] == '(': start += 1  # Пропускаем пробелы и открывающие скобки
    if (start >= end): return  # Если нет данных для создания узла, выходим

    number = ''
    # Чтение числа (значения узла)
    while string[start] in '1234567890':
        number += string[start]
        start += 1
        if start >= end: return Node(int(number))  # Возвращаем узел с найденным числом

    # Создаем новый узел
    node = Node(int(number))

    # Находим конец левого поддерева и начало правого
    right_subtree_index = find_right_subtree(string, start, end) - 1

    if right_subtree_index == -1:
        raise Exception("Wrong bracket notation string!")  # Если структура неправильная, выбрасываем исключение
    
    if right_subtree_index:  # Если правое поддерево существует
        node.left = create_subtree(string, start+1, right_subtree_index)  # Создаем левое поддерево
        node.right = create_subtree(string, right_subtree_index+1, end-1)  # Создаем правое поддерево

    return node  # Возвращаем созданное поддерево


if __name__ == "__main__":
    # Пример строки для создания бинарного дерева
    bt = create_tree("8 (3 (1, 6 (4,7)), 10 (, 14(13,)))".strip())

    # Выводим результаты обходов дерева
    print('Прямой обход:')
    bt.traversePreOrder()  # Прямой обход
    print('\n')

    print('Центральный обход:')
    bt.traverseInOrder()  # Центральный обход
    print('\n')

    print('Концевой обход:')
    bt.traversePostOrder()  # Концевой обход
    print('\n')
    print("Не рекурсивный прямой обход:")
    bt.nonRecursiveTraversePreOrder()

