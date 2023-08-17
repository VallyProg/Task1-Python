# def fibonacci(n: int):
#     a, b = 0, 1
#     for _ in range(n + 1):
#         yield a
#         a, b = b, a + b

# print(*fibonacci(18))


# def generate_dict(names: str, salaries: int, bonuses: str) -> dict[str: float]:
#     yield {name: sal* (1 + float (bon.strip('%')) / 100) for name, sal, bon in zip(names, salaries, bonuses)}



# names = ["Миша", "Саша", "Кирилл"]
# salaries = [100000, 75000, 50000]
# bonuses = ["10.5%", "15.01%", "17.9%"]
# print(next(generate_dict(names, salaries, bonuses)))


# import os 

# def parse_path(path):
#     filepath, file_extension = os.path.splitext(path)
#     dirname, filename, = os.path.split(filepath)
#     return (dirname, filename, file_extension)

# path = r"C:\Users\chupa\OneDrive\Рабочий стол\Hometask5.py"
# dirname, filename, file_extension = parse_path(path)
# print('Directory:', dirname)
# print('Name:', filename)
# print('Extension:', file_extension)