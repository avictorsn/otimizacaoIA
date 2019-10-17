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

    def resfriamento(self, T):
        return T*0.8

    def configuracaoSucessoraAleatoria(self, tabuleiro=Tabuleiro, listaRainhas=list):
        posicoesRainhasRestantes = []
        posicaoRainhaAlterada = random.randint(0,len(listaRainhas)-1)
        print('posição a ser alterada é da rainha de coluna ', (posicaoRainhaAlterada+1))
        for i in range(tabuleiro.dimensao):
            if listaRainhas[i][1] != posicaoRainhaAlterada:
                tabuleiro.setRainha(listaRainhas[i][0], listaRainhas[i][1])
            else:
                tabuleiro.setRainha(posicaoRainhaAlterada, i)
        return tabuleiro

    def prob(self, valorVizinho, valorAtual, temperatura):
        delta = valorVizinho - valorAtual
        func = delta/temperatura
        result = math.exp(func)
        return result

    def execute(self, f):
        print('Executando o Simulated Annealing')
        for t in range(1, self.maxIteracoes):
            temperatura = self.temperaturaInicial / self.resfriamento(t)
            atual = self.configAtual
            vizinho = Tabuleiro(self.configAtual.dimensao)
            vizinho = self.configuracaoSucessoraAleatoria(vizinho, atual.rainhas)
            vizinho.printTabuleiro()
            if f(vizinho) < f(self.configAtual):
                self.configAtual = vizinho
            else:
                p = random.uniform(0,1)
                if self.prob(f(vizinho), f(atual), temperatura) > p:
                    self.configAtual = vizinho