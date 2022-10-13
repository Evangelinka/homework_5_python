# people vs people
import random
instruction = ('Привет! :) Это игра с конфетами на логику! ', 
               ' ',
               'Правила игры: ', 
               'На столе лежит 2021 конфета ,', 
               'за 1 ход можно взять не больше 28 конфет ',
               'ходить нужно по очереди ,',
               'выигрывает тот, кто заберет последнюю конфету!!!',
               ' ', 
               'Желаю удачи! Поехали! :)',
               ' ')

message = ['Ваш ход!', 'сколько конфет будете брать?', 'Ваша очередь!', 'смелее!']

candy_all = 2021
candy_one_move = 28
def play_game(candy_all, candy_one_move, instruction, message):
  count = 0
  while candy_all > 0:
    print(f'{players[count % 2]}, {random.choice(message)}')
    move = int(input())
    if move > candy_all or move > candy_one_move:
      print(f'Вы взяли слишком много конфет! Попробуйте взять не больше, чем {candy_one_move}, всего конфет на столе есть: {candy_all}')
      fatal_error = 3
      while fatal_error > 0:
        if candy_all >= move <= candy_one_move:
          break
        print(f'Попробуйте еще раз!, Попыток осталось: {fatal_error}')
        move = int(input())
        fatal_error -= 1
      else: 
        return print('Вы проиграли! :( Попыток больше нет!, Game over!')
    candy_all -= move
    if candy_all > 0:
      print(f'Конфет осталось: {candy_all}')
    else:
      print('Конфет больше нет!')
    count += 1
  return players[not count % 2]

instructions = '\n'.join(instruction)
print(instructions)
player_1 = input('Введите Ваше имя ИГРОК №1: ')
player_2 = input('Введите Ваше имя ИГРОК №2: ')
print()
players = [player_1, player_2]
winer = play_game(candy_all, candy_one_move, instruction, message)
if not winer:
  print('Ничья! Победила дружба!')
else:
  print(f'Ура, Победитель - {winer}! Все конфеты достаются ему! :)')