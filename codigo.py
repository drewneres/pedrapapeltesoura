from random import randint
from time import sleep

# Definindo os itens
itens = ('Pedra', 'Papel', 'Tesoura')

# Jogada da máquina
maquina = randint(0, 2)
 
# Mostrar as opções
print(''' Suas opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura''')

try:
    # Jogador faz sua jogada
    jogador = int(input('Qual vai ser sua jogada? '))

    if jogador < 0 or jogador > 2:
        print('JOGADA INVÁLIDA! Escolha um número entre 0, 1 e 2.')
    else:
        print('PEDRA')
        sleep(1)
        print('PAPEEEEL')    
        sleep(1)
        print('TESOUUUUURAA')
        sleep(2)
        print('-=' * 11)

        # Mostrar cada jogada
        print(f'Máquina jogou: {itens[maquina]}')
        print(f'Você jogou: {itens[jogador]}')

        # Estrutura de condicionais
        if maquina == 0: # Máquina jogou PEDRA
            if jogador == 0:
                print('EMPATOU')

            elif jogador == 1:
                print('VOCÊ GANHOUU!!!')

            elif jogador == 2:
                print('VOCÊ PERDEU!')
            
        elif maquina == 1: # Máquina jogou PAPEL
            if jogador == 0:
                print('VOCÊ PERDEU!')
            
            elif jogador == 1:
                print('EMPATOUUU!')
            
            elif jogador == 2:
                print('VOCÊ GANHOUU!!!')
            
        elif maquina == 2: # Máquina jogou TESOURA
            if jogador == 0:
                print('VOCÊ GANHOUU!!!')
            
            elif jogador == 1:
                print('VOCÊ PERDEU!')
            
            elif jogador == 2:
                print('EMPATOUUU!')

except ValueError:
    print('Entrada inválida. Por favor, insira um número entre 0, 1 e 2.')
