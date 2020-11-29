from random import shuffle


# Функция для получения числа "Быков" у числа
def get_bulls(number, guess):
    count = 0
    for i in range(len(number)):
        if number[i] == guess[i]:
            count += 1
    return count


# Функция для получения числа "Коров" у числа
def get_cows(number, guess):
    count = 0
    for i in range(len(number)):
        if guess[i] in number and guess[i] != number[i]:
            count += 1
    return count


# Функция для генерации, если длина не входит в промежуток от 1 до 10, возвращает пустую строку
def generate_number(length):
    if not length in range(1, 11):
        return ""
    seq = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while seq[0] == '0':
        shuffle(seq)
    return ''.join(seq[:length])


# Функция для проверки ввода на соответствие числовому представлению, запрашивает ввод пока он не будет являться числом
def get_int_input():
    number = input()
    while not number.isdigit():
        print("Ошибка! Ввод не является целым положительным числом")
        number = input()
    return number


# Функция для проверки уникальности цифр в числе
def check_unique_nums(number):
    return len(list(number)) == len(set(number))


# Запрашиваем ввод длины числа
print("Введите длину числа от 1 до 9")
length = int(get_int_input())
while int(length) not in range(1, 11):
    print("Ошибка! Введённое число не входит в диапазон от 1 до 9")
    length = int(get_int_input())

# Генерируем число заданной длины
number = generate_number(length)
print(f"Компьютер загадал число длины {length}. Попробуйте отгадать его.")

# Пока быков в слове меньше длины, просим игрока вводить число
while True:
    print(f"Введите число длины {length} с разными цифрами")
    guess = get_int_input()
    while len(guess) != length or not sorted(list(guess)) == sorted(list(set(guess))):
        print(f"Ошибка! Введите число ещё раз")
        guess = get_int_input()
    if get_bulls(number, guess) == length:
        break
    print(f"Быков - {get_bulls(number, guess)}, коров - {get_cows(number, guess)}")


# Выводим победное сообщение
print(f"Поздравляем, вы выиграли! Загаданным числом было {number}")
