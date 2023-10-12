import colorama
from colorama import Fore 


def inicio():
    return inicio
while True :
 print( Fore.WHITE+ '-'*70)
 print('Òla eu sou o computador seu adversario,qual seu nick?')
 print('-'*70)
 name = input('->  ')
 tamnho = len(name)

 if tamnho > 3:
  print( f'Seja bem vindo(a) {Fore.GREEN} {name}')
  break
 else:
  print(Fore.RED + 'Digite um nick valido')



from random import randint
from time import sleep
def jogo(jokenpô):
 return jogo
rodadas = 0

while True:
 itens = ['pedra', 'tesoura', 'papel']
 computador = randint(0,2)
 print('-'*28)
 print(Fore.LIGHTBLUE_EX + 'Vamos nessa!!!')
 sleep(1.2)
 print( Fore.BLUE + '''
      Faça sua escolha
      [0] PEDRA
      [1] TESOURA 
      [2] PAPEL
      ''')
 player = int(input(Fore.WHITE+ '-> '))
 print(Fore.GREEN + 'JO')
 sleep(1)
 print(Fore.YELLOW+'kEN')
 sleep(1)
 print(Fore.MAGENTA+'PO!!!')
 print(Fore.WHITE+'-=-='*11)
 print('O jogador jogou {}'.format(itens[player]))
 print('O computador jogou {}'.format(itens[computador]))
 print('-=-='*11)

 if player == computador:
  print( Fore.YELLOW +  'EMPATE!!!')
 
 elif player == 1:
  if computador != 0:
    print(Fore.GREEN + 'Você venceu')
  else:
    print( Fore.RED + 'O computador ganhou')
 elif player == 0:
  if computador != 2:
   print(Fore.GREEN + 'Você venceu')
   
  else:
    print( Fore.RED + 'O computador ganhou')
 elif player == 1:
    if computador != 2:
       print(Fore.GREEN + 'Você venceu')
       
    else:
     print( Fore.RED + 'O computador ganhou')
 elif player == 2:
  if computador != 1:
    print(Fore.GREEN + 'Você venceu')
   
  else:
    print( Fore.RED + 'O computador ganhou')
  print(Fore.LIGHTBLUE_EX + 'Deseja continuar? S/N')
 opçao = input('->').upper()
 if opçao == 'N':
  print(Fore.LIGHTGREEN_EX + 'Jogo encerrado,TCHAU!!! ')
  break
 elif opçao == 'S':
  print( f'Rodada {rodadas + 2}')

  rodadas =+1

    
      
     