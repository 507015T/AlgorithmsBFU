import heapq
import os

def merge_files(output_file, temp_files): 
    """
    Выполняет слияние отсортированных временных файлов в один выходной файл.

    :param output_file: Путь к результирующему выходному файлу.
    :param temp_files: Список путей к временным файлам.
    """
    heap_array = []  # Приоритетная очередь для слияния элементов.
    # Открываем все временные файлы для чтения.
    temp_files = [open(temp_file, 'r', encoding="utf-8") for temp_file in temp_files]

    with open(output_file, "w") as output:  # Открываем выходной файл для записи.
        # Считываем первую строку из каждого временного файла и добавляем в кучу.
        for i in range(len(temp_files)):
            element = temp_files[i].readline().strip()
            if element:  # Если строка не пустая, добавляем её в кучу.
                heapq.heappush(heap_array, (int(element), i))

        counter = 0  # Счётчик завершённых файлов.
        # Обрабатываем кучу, пока все файлы не будут исчерпаны.
        while counter < len(temp_files):
            if not heap_array:
                break
            root = heapq.heappop(heap_array)  # Извлекаем минимальный элемент из кучи.
            output.write(str(root[0]) + '\n')  # Записываем его в выходной файл.

            # Считываем следующую строку из файла, откуда был извлечён элемент.
            element = temp_files[root[1]].readline().strip()
            if element:  # Если строка не пустая, добавляем её в кучу.
                heapq.heappush(heap_array, (int(element), root[1]))
            else:  # Если файл исчерпан, увеличиваем счётчик.
                counter += 1

        # Закрываем все временные файлы.
        for temp_file in temp_files:
            temp_file.close()

def create_initial_runs(input_file, run_size, path): 
    """
    Разбивает входной файл на несколько временных файлов, каждый из которых содержит отсортированные данные.

    :param input_file: Путь к входному файлу.
    :param run_size: Количество строк, обрабатываемых за один прогон.
    :param path: Путь к директории для сохранения временных файлов.
    :return: Список путей к временным файлам.
    """
    temp_files = []  # Список временных файлов.
    with open(input_file, 'r', encoding="utf-8") as input: 
        end_of_file = False  # Флаг завершения чтения файла.
        temp_files_counter = 0  # Счётчик временных файлов.

        # Создаём директорию для временных файлов, если она не существует.
        os.makedirs(path, exist_ok = True)

        while True:
            data = []  # Буфер для хранения данных текущего прогона.
            # Читаем строки из входного файла.
            for _ in range(run_size):
                line = input.readline().strip()
                if not line:  # Если достигнут конец файла, выходим из цикла.
                    break
                data.append(int(line))  # Добавляем число в буфер.

            if not data:  # Если данных больше нет, выходим из цикла.
                break

            data.sort()  # Сортируем данные в буфере.

            # Создаём временный файл и записываем в него отсортированные данные.
            temp_file_path = os.path.join(path, f'f_{temp_files_counter}.txt')
            with open(temp_file_path, 'w', encoding="utf-8") as output:
                temp_files.append(temp_file_path)
                output.write('\n'.join(str(i) for i in data))

            temp_files_counter += 1  # Увеличиваем счётчик временных файлов.

    return temp_files  # Возвращаем список временных файлов.

def external_multiphase_sort(path: str, run_size: int) -> None: 
    """
    Выполняет внешнюю многофазную сортировку: создание временных файлов и их слияние.

    :param path: Путь к директории, содержащей входной файл.
    :param run_size: Количество строк, обрабатываемых за один прогон.
    """
    input_file = f"{path}/input.txt"  # Входной файл.
    output_file = f"{path}/output.txt"  # Выходной файл.
    temp_path = os.path.join(path, "Temp_files_linear")  # Директория для временных файлов.

    # Создаём временные отсортированные файлы.
    temp_files = create_initial_runs(input_file, run_size, temp_path)
    # Объединяем временные файлы в итоговый отсортированный файл.
    merge_files(output_file, temp_files)


test_path = "test_sort"

run_size = 3

external_multiphase_sort(test_path, run_size)

output_file = os.path.join(test_path, "output.txt")

print("Результат сортировки:")
with open(output_file, "r", encoding="utf-8") as output:
    print(output.read())
