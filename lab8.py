def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n # Массив для хранения отсортированного результата
    count = [0] * 10 # Массив для хранения количества цифр (0-9)

    # Подсчитываем количество цифр в arr
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index]  += 1

    # Изменяем count так, чтобы каждая позиция содержала фактическую поизицию
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Создаем отсортированный массив по текущей цифре
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Копируем отсортированный массив обратно в arr
    for i in range(n):
        arr[i] = output[i]



def radix_sort(arr):
    # Находим максимальное число, чтобы знать количество разрядов
    max_num = max(arr)
    # Выполняем сортировку для каждого разряда числа
    # Показатель степени
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10



arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Отсортированный массив:", arr)
