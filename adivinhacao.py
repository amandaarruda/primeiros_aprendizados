# Este jogo é um exercício do curso de Introdução à Python

import random


def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = round(random.random() * 100)
    total_de_tentativas = 0
    pontos = 1000

    print("Níveis de dificuldade:")
    print("1. Fácil")
    print("2. Médio")
    print("3. Difícil")

    nivel = int(input("Selecione o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            # para fazer o número ser digitado novamente:
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        # agora, é necessário comparar o chute e o número secreto.
        # Quando usamos apenas um =, estamos atribuindo um valor à variável. Para compararmos valores ou variáveis, usamos o ==.
        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            # para sair do laço:
            break
        # os dois pontos são necessários sempre depois de uma condição
        # é necessário colocar 4 espaços ou dar um tab
        else:
            if maior:
                print("Você errou... Seu chute foi maior que o número secreto.")
            elif menor:
                print('Você errou... Seu chute foi menor que o número secreto.')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        # O uso de parênteses depois do if, elif, etc é opcional
        # Comentário que li no stackoverflow sobre isso: Não há nenhum ganho ou perda no uso de parênteses extras em expressões como if e while. Eles não são obrigatórios na linguagem justamente para simplificar a leitura das expressões. o : no final dos comandos faz a separação da expressão para o bloco contido no comando - portanto não existe a ambiguidade potencial que existe em C e as linguagens que copiaram a sua sintaxe exigindo o parênteses no if. Note que isso não impede que você use parênteses para melhorar a legibilidade do código, sobretudo em expressões complexas de um if que podem ter que ser quebradas em mais de uma linha. Nesses casos, inclusive, os parênteses são preferíveis ao indicador de continuação de linha \. Parenteses extras são automaticamente elimnados no estágio de compilação do programa (lembrando que a compilação em Python é automática).

        # Diferença: Um if é o primeiro if, o else é quando você quer fazer ele completar alguma ação se o if for falso, e elif é quando você tem um if dentro de um else. A instrução else não aceita receber uma condição.

        # atenção: é preciso que as classes sejam equivalentes para que o resultado possa ser correto.
        # como eu defini a variável numero_secreto como uma int (e a intenção é que apenas int sejam digitadas. caso contrário, poderia ter definido como a str "13"), é necessário mudar o input de str do chute.
        rodada = rodada + 1

    print('Fim do jogo :)')


if __name__ == "__main__":
    jogar()
