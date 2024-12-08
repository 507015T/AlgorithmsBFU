def selection_sort(digits: list[int]) -> list[int]:
    list_len = len(digits)
    for i in range(0, list_len - 1):
        # Индекс потенциального самого малого числа
        min_index = i
        for j in range(i+1, list_len):
            # если если есть число меньше, то присвоить индекс этого числа переменной min_index
            if digits[j] < digits[min_index]:
                min_index = j
        digits[i], digits[min_index] = digits[min_index], digits[i]
    return digits


print(selection_sort([37, 5, 42, 17, 23, 9, 11, 88, 31, 74, 56, 2, 49]))
