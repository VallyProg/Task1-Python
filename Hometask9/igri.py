# import random

# def game_control(func):
# def wrapper(num, amount):
# # result = 'Введите корректные значения игры'
# if not ((1 <= num <= 100) and amount in range(1, 11)):
# num = random.randint(1, 100)
# amount = random.randint(1, 10)
# result = func(num, amount)
# return result

# return wrapper

# @game_control
# def inner(num, amount):
# for attempt in range(1, amount + 1):
# print(f"Попытка № {attempt}")
# ask = int(input('Угадайте число от 1 до 100: '))
# if ask == num:
# print('Вы угадали!!!')
# break
# elif ask < num:
# print('Ваше число больше загаданного')
# else:
# print('Ваше число меньше загаданного')

# if ask != num:
#     print('Вы проиграли!')

# inner(500, 500)



# def request_number(num, amount):
# def inner():
# for attempt in range(1, amount + 1):
# print(f"Попытка № {attempt}")
# ask = int(input('Угадайте число от 1 до 100: '))
# if ask == num:
# print('Вы угадали!!!')
# break
# elif ask < num:
# print('Ваше число больше загаданного')
# else:
# print('Ваше число меньше загаданного')

#     if ask != num:
#         print('Вы проиграли!')

# return inner








# import time
# from typing import Callable
# from random import randint
# def how_long(func: Callable):
# start = time.time()
# func()
# print(f"время выполнения составило {time.time() - start}")
# def create_list(n=5_000_000):
# return [randint(-1000, 1000) for _ in range(n)]
# how_long(create_list)
# def calc_pow(pow: int):
# def calc_root(root: int):
# return root ** pow
# return calc_root
# # print(calc_pow(4)(10))
# squares = calc_pow(2)
# cubs = calc_pow(3)
# print(squares(6))
# print(cubs(6))

# import time
# from typing import Callable

# def main(func: Callable):
# def wrapper(*args, **kwargs):
# print(f'Запуск функции {func.name} в {time.time()}')
# result = func(*args, **kwargs)
# print(f'Результат функции {func.name}: {result}')
# print(f'Завершение функции {func.name} в {time.time()}')
# return result

# return wrapper

# @main
# def factorial(n: int) -> int:
# f = 1
# for i in range(2, n + 1):
# f *= i
# return f

# print(f'{factorial(10) = }')
# control = main(factorial)
# print(f'{control.name = }')
# print(f'{control(10) = }')



# import json
# from pathlib import Path
# from typing import Callable

# def my_logger(func: Callable):
# file = Path(f'{func.name}.json')
# if file.is_file():
# with open(file, 'r', encoding='utf-8') as f:
# data = json.load(f)
# else:
# data = []

# def wrapper(*args, **kwargs):
#     json_dict = {'args': args, **kwargs}
#     result = func(*args, **kwargs)
#     json_dict['result'] = result
#     data.append(json_dict)
#     with open(file, 'w', encoding='utf-8') as f:
#         json.dump(data, f)
#     return result

# return wrapper

# @my_logger
# def get_all(num: int, *args, **kwargs) -> int:
# return num

# if name == 'main':
# get_all(42, 6, z=1, y='1', x=True)
