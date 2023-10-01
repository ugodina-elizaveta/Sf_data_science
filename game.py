import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_num = 1
    max_num = 101
    while True:
        np.random.seed(1)   # фиксируем сид для воспроизводимости
        predict = np.random.randint(min_num, max_num)
        count += 1  # количество попыток
        if predict == number:
            break
        elif predict < number:
            min_num = predict
        elif predict > number:
            max_num = predict
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []   # список для сохранения количества попыток
    np.random.seed(1)   # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))   # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))   # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


