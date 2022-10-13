# Создайте программу для игры в "Крестики-нолики".

matrix_for_play = [['-' for i in range(0, 3)] for i in range(0, 3)]

def get_play_matrix():
  for i in matrix_for_play:
    print(*i)

get_play_matrix() 
print('Для игры вводите данные на EN расскладке \nЕсли хотите прекратить игру: введите "STOP". Приятной игры!')

step = 0 
while step != 'STOP':
  i = int(input('Номер строки: '))
  j = int(input('Номер столбца: '))
  step = input('Введите X или О: ')
  if 0 < i <= 3 and step != 'STOP' and 0 < j <= 3 and (step=='X' or step=='O'):
    matrix_for_play[i - 1][j - 1] = step
  else:
    print('Вы ввели недопустимый диапазон! GAME OVER \nПопробуйте сыграть еще раз!')
    break
  get_play_matrix()