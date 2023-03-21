from random import randint
from math import log2, ceil

# Приветствие
print('Добро пожаловать в игру "Угадай число"!', \
      'Предлагаем вам самим указать в каком диапазоне вы будете отгадывать число!', '',\
      sep = '\n')

new_game = 'д'
count_games = 0
sum_guesses = 0
while new_game == 'д':
    # Проверка валидности левой границы
    def left_is_valid(left):
        while not left.isdigit():
            left = input('Нужно указать число (без пробелов, спец. символов и букв) - ')
        return left

    # Унзнаем у пользователя левую грацину
    left = input('Укажите минимальное число - ')
    valid_left = int(left_is_valid(left))

    # Проверка валидности правой границы
    def right_is_valid(right):
        while not right.isdigit():
            right = input('Нужно указать число (без пробелов, спец. символов и букв) - ')
        return right

    # Унзнаем у пользователя правую грацину для диапазона
    right = input('Укажите максимально число - ')
    valid_right = int(right_is_valid(right))

    # Проверяем, чтобы левая граница была меньше.
    while valid_left + 1 > valid_right: # Примечание к, valid_left + 1 почему-то при одинаковых значения l = 10 & r = 10 цикл выводил false
        right = input('Максимальное значение должно быть больше минимального. Укажите число - ')
        valid_right = int(right_is_valid(right))

    # Показываем клиенту указанный диапазон и примерное кол-во попыток для отгадывания
    print(f'\nВы указали диапазон от {valid_left} до {valid_right}.\n' 
          f'Среднее число попыток на отгадывания числа в указанном диапазоне приблизительно равняется - {ceil(log2(valid_right - valid_left))}!\n'
          f'Уверены у вас получится быстрее! Приступим!\n')

    # Генерируем случайное число из указанного диапазона
    rand_num = randint(valid_left, valid_right)

    # Проверка валидности указанного числа и попадание в указанный диапазон
    def guess_is_valid(q):
        global guess
        if not guess.isdigit():
            while not guess.isdigit():
                guess = input('Нужно указать число (без пробелов, спец. символов и букв) - ')
                if not valid_left <= int(guess) <= valid_right:
                    while not valid_left <= int(guess) <= valid_right:
                        guess = input(f'Число должно находится в указанном вами диапазоне от {valid_left} до {valid_right} - ')
                    return int(guess)
        else:
            return int(guess)

    # Узнаем у пользователя первое значение
    guess = input('Укажите число - ')
    guess_is_valid(guess)

    # Добавляем счётчик попыток
    counter = 1

    # Запускаем цикл с подсказками для пользователя
    while guess_is_valid(guess) != rand_num:
        if guess_is_valid(guess) > rand_num:
            counter += 1
            guess = input('Загаданое число меньше, укажите новое - ')
        elif guess_is_valid(guess) < rand_num:
            counter += 1
            guess = input('Загаданое число больше, укажите новое - ')

    # Завершение текущей игры
    print(f'\nПоздравляем! Вы угадали\n'
          f'Кол-во ваших попыток: {counter}\n')

    # Считаем тотал для общей статистики
    count_games += 1
    sum_guesses += counter
    avg = sum_guesses / count_games

    # Хочет ли пользователь сыграть ещё
    new_game = input('Хотите сыграть ещё? Напишие "д", если хотите сыграть ещё раз или "н", если не хотите: ').lower()

if count_games > 1:
    print(f'\nСтатистика вашей игры.\n'
          f'Кол-во игры: {count_games}\n'
          f'Сумма попыток: {sum_guesses}\n'
          f'Среднее кол-во попыток на игру: {avg}\n'
          f'Всего доброго!')
else:
    print('\nВсего доброго!')