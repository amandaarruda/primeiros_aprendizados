# Este é o hub inicial, onde o jogo desejado será escolhido
import forca
import adivinhacao

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("1. Forca")
print("2. Adivinhação")

jogo = int(input("Qual será o jogo desejado?"))

if jogo == 1:
    print("Jogando Forca")
    forca.jogar()
elif jogo == 2:
    print("Jogando Adivinhação")
    adivinhacao.jogar()
