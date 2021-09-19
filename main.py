import random


def number_finder(number):
    # Смысл задачи заключается в сдвиге границы относительно середины в сторону числа
    # и последующей проверки нахождения самого числа
    count = 1
    mn = 1
    mm = 100
    predict = mm // 2  # Вычисляем середину
    while number != predict:
        count += 1
        if number > predict:
            mn = predict + 1  # Сдвигаем
        elif number < predict:
            mm = predict - 1  # Сдвигаем
        else:
            break
        predict = (mm + mn) / 2
    return count


number = random.randint(1, 100)  # Случайное число
print('Случайное число:', number)
print('Кол-во ходов для нахождения:', number_finder(number))
