from tabuleiro.Tabuleiro import Tabuleiro
import funcao_objetiva.FuncaoObjetiva as func
import math
import random

class SimulatedAnnealing:
    def __init__(self, configInicial: Tabuleiro, maxIteracoes, temperaturaInicial):
        # Inicializando os atributos com os parâmetros de entrada
        self.configInicial = configInicial
        self.maxIteracoes = maxIteracoes
        self.temperaturaInicial = temperaturaInicial

        # Atributos auxiliares
        self.configAtual = configInicial

    def printTabuleiro(self):
        print(self.configAtual)

    def execute(self):
        print('Executando o Simulated Annealing')
        for t in range(self.maxIteracoes+1):
            temperatura = self.temperaturaInicial / math.sqrt(t+1)
            #vizinho = configuração descendente de self.configAtual
            #if f(vizinho) < f(self.configAtual):
            #  self.configAtual = vizinho