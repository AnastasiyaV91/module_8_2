def personal_sum(numbers):
    result = 0                             # Создаем переменную для посчета суммы чисел в принимаемой коллекции numbers
    incorrect_data = 0                     # Cоздаем переменную для посчета колличества не соответствий числу
    for i in numbers:                      # Проходим по каждому элементу numbers
        try:                               # Пробуем
            result += i                    # Пробуем увеличить сумму чисел коллекции numbers
        except TypeError:                  # Если ошибка, то
            incorrect_data += 1            # увеличиваем на 1 переменную количества ошибок
            print("Некорректный тип данных для подсчёта суммы - ", i)  # Выводим в консоль сообщение
    return result, incorrect_data          # Возвращаем результаты посчетов

def calculate_average(numbers):
    try:                                                     # Пробуем
        if numbers != int():                                 # Если numbers не является числом, то
            result, incorrect_data = personal_sum(numbers)   # получаем возвращаемые значения
                                                             # функции personal_sum(numbers)
            return result / (len(numbers) - incorrect_data)  # Возвращаем среднее арифметическое чисел numbers
    except TypeError:                                        # Если ошибка и numbers является числом, то
        print("В numbers записан некорректный тип данных")   # выводим в консоль сообщение
        return None                                          # Возвращаем None
    except ZeroDivisionError:                                # Если ошибка деления на 0, то
        return 0                                             # возвращаем 0





print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

