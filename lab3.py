# На вход дается одно число х, нужно вывести все числа от 1 до х,
# удовлетворяющие условию:
# 3^K*5^L*7^M=x
# где K, L, M - натуральные числа или могут быть равны 0.


def correct_digits(digit):
    list_with_correct_digits = list()
    for i in range(digit):
        # Анулируем предполагаемое число, чтобы избежать раннего окончания программы
        desired_number = 0
        for j in range(digit):
            # Если в выражении j слишком велико
            if 3 ** i * 5 ** j > digit:
                break
            for k in range(digit):
                desired_number = 3 ** i * 5 ** j * 7 ** k
                # Если предполагаемое число в промежутке до "x", то число подходит, иначе k слишком великo
                if desired_number <= digit:
                    list_with_correct_digits.append(desired_number)
                else:
                    break
        # Если i слишком велико, то все варианты были подобраны
        if 3 ** i > digit:
            break
    # Отсортировываем полученные числа и исключаем все дубликаты
    print(sorted(set(list_with_correct_digits)))


correct_digits(10009000)
