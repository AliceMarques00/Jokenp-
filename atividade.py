import random

class Jokenpo:
    def __init__(self):

        self.opcoes = ['Pedra', 'Papel', 'Tesoura']

    def escolher_opcao(self):
        print('Bem vindo ao Jokenpô!')
        nome=input('Qual o seu nome jogador? ')
        escolha_usuario = input(f'{nome} escolha Pedra, Papel ou Tesoura: ').capitalize()
        if escolha_usuario not in self.opcoes:
            print('Escolha inválida, tente novamente.')
            return self.escolher_opcao()
        return escolha_usuario

    def escolha_computador(self):

        return random.choice(self.opcoes)

    def determinar_vencedor(self, jogador, computador):

        if jogador == computador:
            return 'Empate'
        elif (jogador == 'Pedra' and computador == 'Tesoura') or \
             (jogador == 'Papel' and computador == 'Pedra') or \
             (jogador == 'Tesoura' and computador == 'Papel'):
            return 'Parabens mini queride, você venceu! :)'
        else:
            return 'O oponente venceu'

    def jogar(self):

        jogador = self.escolher_opcao()
        computador = self.escolha_computador()
        print(f' Você escolheu {jogador}')
        print(f'Computador escolheu: {computador}')
        resultado = self.determinar_vencedor(jogador, computador)
        print(resultado)

jogar = Jokenpo()
jogar.jogar()

