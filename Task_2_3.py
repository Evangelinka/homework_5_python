# people vs intellect_bot
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

candy_all = 200
candy_one_move = 28

def get_players():
  player_1 = input('Введите Ваше имя ИГРОК №1: ')
  player_2 = 'MetaBot'
  print('\nМеня зовут - ', player_2)
  return [player_1, player_2]

players = get_players()
print()

def find_first_move(players):
  first_move = int(input(f'{players[0]}, кто будем ходит первым? Если Вы: нажмите 1, если бот: нажмите любую другую цифру :)\n'))
  if first_move !=1:
    first_move = 0
  return [candy_all, candy_one_move, int(first_move)]

first_player = find_first_move(players)
print()

def play_game(first_player, players, message):
  count = first_player[2]
  while first_player[0] > 0:
    if not count % 2:
      move = first_player[0] % first_player[1] + 1
      print(f'Я возьму {move}')
    else:
      print(f'{players[0]}, {random.choice(message)}')
      move = int(input())
      if move > first_player[0] or move > first_player[1]:
        print(f'Вы взяли слишком много конфет! Попробуйте взять не больше, чем {first_player[1]}, всего конфет на столе есть: {first_player[0]}')
        fatal_error = 3
        while fatal_error > 0:
          if first_player[0] >= move <= first_player[1]:
            break
          print(f'Попробуйте еще раз!, Попыток осталось: {fatal_error}')
          move = int(input())
          fatal_error -= 1
        else: 
          return print('Вы проиграли! :( Попыток больше нет!, Game over!')
    first_player[0] -= move
    if first_player[0] > 0:
      print(f'Конфет осталось: {first_player[0]}')
    else:
      print('Конфет больше нет!')
    count += 1
  return players[count % 2]

instructions = '\n'.join(instruction)
print(instructions)
print()

winer = play_game(first_player, players, message)
if not winer:
  print('Ничья! Победила дружба!')
else:
  print(f'Ура, Победитель - {winer}! Все конфеты достаются ему! :)')