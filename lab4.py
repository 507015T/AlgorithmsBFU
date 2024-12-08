# Сортировка метод прочесывания

def comb_sort(numbers_array):
    step = len(numbers_array)
    double_factor = 1.3
    sorted_flag = False
    while step > 1 or not sorted_flag:
        # Уменьшаем шаг на фактор
        step = max(1, int(step / double_factor))
        sorted_flag = True  # Предполагаем, что массив отсортирован
        for i in range(len(numbers_array) - step):
            if numbers_array[i] > numbers_array[i + step]:
                numbers_array[i], numbers_array[i + step] = numbers_array[i + step], numbers_array[i]
                sorted_flag = False  # Если был обмен, значит, еще не отсортирован список
    print(numbers_array)

comb_sort([1, 5, 10, 5, -4, 24, 2, 3, 32, 4])
