# Дан текстовый файл с некоторым текстом на русском или английском языках
# произвольной длины (организовать чтение). Выбрав некоторую хеш-функцию, создать хеш-таблицу с:
# Лаба №13 “с наложением”
import hashlib  # Импортируем библиотеку для работы с хеш-функциями

def sha256_hash_function(word):
    """
    Хеш-функция на основе алгоритма SHA-256.
    Преобразует строку в уникальное числовое значение.

    :param word: Слово для хеширования.
    :return: Числовое значение хеша.
    """
    sha256 = hashlib.sha256()  # Создаем объект хеш-функции SHA-256
    sha256.update(word.encode('utf-8'))  # Кодируем строку в байты и добавляем в хеш-функцию
    return int(sha256.hexdigest(), 16)  # Преобразуем хеш из шестнадцатеричного формата в целое число


def create_hash_table(input_file, output_file):
    """
    Создает хеш-таблицу из текста файла и записывает результат в другой файл.

    :param input_file: Имя входного файла с текстом.
    :param output_file: Имя выходного файла для сохранения хеш-таблицы.
    """
    # Открываем файл для чтения текста
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()  # Считываем весь текст из файла

    # Разбиваем текст на отдельные слова
    words = text.split()

    # Определяем размер хеш-таблицы как количество слов в тексте
    hash_table_size = len(words)  # Таблица будет иметь столько ячеек, сколько слов в тексте
    hash_table = [None] * hash_table_size  # Инициализируем пустую таблицу

    for word in words:
        # Вычисляем хеш-значение для слова
        # print(sha256_hash_function(word), ';')
        hash_value = sha256_hash_function(word) % hash_table_size

        # Разрешение коллизий методом линейного пробирования
        while hash_table[hash_value] is not None:  # Если ячейка уже занята
            hash_value = (hash_value + 1) % hash_table_size  # Переходим к следующей ячейке

        # Помещаем слово в найденную свободную ячейку таблицы
        hash_table[hash_value] = word

    # Открываем файл для записи результата
    with open(output_file, 'w', encoding='utf-8') as result_file:
        # Проходим по всем индексам таблицы
        for index, word in enumerate(hash_table):
            if word is not None:  # Если ячейка содержит слово
                result_file.write(f"{index}: {word}\n")  # Записываем индекс и слово в файл


# Пример использования
create_hash_table('input.txt', 'output13.txt')
