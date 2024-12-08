def shell_sort(digits: list[int]) -> list[int]:
    n = len(digits)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            # Сохраняем текущий элемент для последующего перемещения
            temp = digits[i]
            j = i
            while j >= interval and digits[j - interval] > temp:
                # Сдвигаем элемент на interval вправо
                digits[j] = digits[j - interval]
                j -= interval

            # Помещаем сохраненное значение на его новое место
            digits[j] = temp
        interval //= 2
    return digits


print(shell_sort([37, 5, 42, 17, 23, 9, 11, 88, 31, 74, 56, 2, 49]))
