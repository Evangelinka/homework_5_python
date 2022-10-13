# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('Task_4_decod.txt', 'r') as data:
    my_text = data.read()

def encode_rle(my_text):
    str_code = ''
    prev_char = ''
    count = 1
    for i in my_text:
        if i != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = i
        else:
            count += 1
    return str_code + str(count) + prev_char[-1]


str_code = encode_rle(my_text)
print('Исходник: ', my_text)
print('Получилось: ', str_code)

with open('Task_4_encod.txt', 'r') as data:
    text_2 = data.read()

def decoding_rle(text_2):
    count = ''
    str_decode = ''
    for i in text_2:
        if i.isdigit():
            count += i
        else:
            str_decode += i * int(count)
            count = ''
    return str_decode

str_decode = decoding_rle(text_2)
print('Исходник: ', text_2)
print('Получилось: ', str_decode)