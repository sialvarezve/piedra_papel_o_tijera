import random

print('Este es un sencillo juego de piedra, papel o tijera. \n',
     'No esperes mucho :p. \n \n',
     '*'*15, '\n \n')
options = ('piedra', 'papel', 'tijera')
goal_score = int(input('Numero de triunfos necesarios: '))

while not 1 <= goal_score <=10:
  print('Terrible ese numero de rondas. \n',
       'Debe estar entre 1 y 10.')
  goal_score = int(input('Numero de triunfos necesarios: '))

user_score, computer_score = 0, 0
round = 1
while not (user_score >= goal_score or computer_score >= goal_score):

  print('*'*15)
  print(f'Ronda {round}')
  print('*'*15)
  user_option = input('piedra, papel o tijera: ')
  
  while user_option not in options:
    print("Esa opcion no es valida, bobo. Escoge entre piedra, papel y tijera")
    user_option = input('piedra, papel o tijera: ')    

  computer_option = random.choice(options)
  
  if user_option == computer_option:
    print('empate')
  elif user_option =='piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gana')
      user_score += 1
    else:
      print('papel gana a piedra')
      print('computer gana')
      computer_score += 1
  elif user_option =='papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gana')
      user_score += 1
    else:
      print('tijera gana a papel')
      print('computer gana')
      computer_score += 1
  elif user_option =='tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gana')
      user_score += 1
    else:
      print('piedra gana a tijera')
      print('computer gana')
      computer_score += 1

  round += 1
  
  print('-'*15)

print('*'*15)
ganador = 'user' if user_score > computer_score else 'computer'
print('El ganador es ' + ganador)
print('*'*15)