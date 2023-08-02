# import math

# d = float(input('Введите диаметр круга: '))

# if d > 1000:
#     print('Неправильно введено число, введите меньше 1000')
#     exit()

# l = 2 * math.pi * (d / 2) # Длина круга
# s = math.pi * math.pow((d / 2), 2) # Плдощадь круга

# print(f'Длина круга = {l:.42f}')
# print(f'Площадь круга = {s:.42f}')




# def print_hex(a_input):
        
#     dict_hex = "0123456789abcdef"
#     a_str = ""
#     while (a_input) > 0:
#         a_str = dict_hex[a_input % 16] + a_str    
#         a_input = a_input // 16
#     return a_str

# a_input = int(input('Введите целое число: '))
# a_str = print_hex(a_input)

# print(f'Число {a_input} в шестнатиричной системе = {a_str}') 



# def process_fractions(fr1_str, fr2_str):

#     a_ch, a_zn = map(int, fr1_str.split("/"))
#     b_ch, b_zn = map(int, fr2_str.split("/"))

#     if a_zn == b_zn:
#         sum_frac_ch = a_ch + b_ch 
#         sum_frac_zn = a_zn * 1
    
    
#     if a_zn != b_zn:
#         sum_frac_ch = a_ch * a_zn + b_ch * b_zn
#         sum_frac_zn = b_ch * b_zn
#     sum_frac = (sum_frac_ch, sum_frac_zn)

#     proizv_frac_ch = a_ch * b_ch
#     proizv_frac_zn = a_zn * b_zn
#     proizv_frac = (proizv_frac_ch, proizv_frac_zn)

#     return sum_frac, proizv_frac


# fr1_str = input('Введите первую дробь в виде a/b: ')
# fr2_str = input('Введите вторую дробь в виде a/b: ')

# sum_frac, proizv_frac = process_fractions(fr1_str, fr2_str)

# print(f"Сумма дробей {fr1_str} и {fr2_str} - {sum_frac[0]}/{sum_frac[1]}")
# print(f"Произведение дробей {fr1_str} и {fr2_str} - {proizv_frac[0]}/{proizv_frac[1]}")
