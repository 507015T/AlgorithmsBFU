def merge_sort(arr):
    # Базовый случай: массив длиной 0 или 1 уже отсортирован
    if len(arr) <= 1:
        return arr
    
    # Разделяем массив на две части
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Рекурсивно сортируем каждую половину
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Сливаем отсортированные половины
    return merge(left, right)

def merge(left, right):
    result = []  # Список для хранения результата слияния
    i = j = 0    # Индексы для обхода левого и правого массивов
    
    # Сравниваем элементы из left и right, добавляя меньший в result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Добавляем оставшиеся элементы из left (если есть)
    result.extend(left[i:])
    # Добавляем оставшиеся элементы из right (если есть)
    result.extend(right[j:])
    
    return result

# Пример использования
arr = [12, 11, 13, 5, 6, 7]
print("Отсортированный список:", merge_sort(arr))
