#crie um jogo de adivinha numero com uma matriz e os jogadores disponiveis
import random

print("BEM-VINDO AO JOGO DO CHUTE")

matriz=[["joão"],
["carmem"],
["pedro"],
["maria"]]

escolha=float(input("Nos diga qual jogador você é? 0,1,2,3(0=João, 1=Carmem, 2=Pedro, 3=Maria)"))
if (escolha==0):
    escolha=matriz[0]
    print(matriz[0])
elif (escolha==1):
    escolha=matriz[1]
    print(matriz[1])
elif (escolha==2):
    escolha=matriz[2]
    print(matriz[2])
elif (escolha==3):
    escolha=matriz[3]
    print(matriz[3])
    
respota=float(input("digite o seu valor de chute: "))
if respota==random.randint(0,9):
    print("o vencedor(a) é:", escolha)
    print("com o numero:",respota)
else: print("você não venceu, tente outra vez")

