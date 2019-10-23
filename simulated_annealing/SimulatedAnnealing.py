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

    # Printar configuração atual
    def printTabuleiro(self):
        print(self.configAtual)

    #Função de resfriamento
    def resfriamento(self, T):
        return math.sqrt(T)

    # Gerar uma configuração aleatória descendente de uma dada configuração
    def configuracaoSucessoraAleatoria(self, tabuleiro=Tabuleiro, listaRainhas=list):
        colunaRainhaAlterada = random.randint(0,len(listaRainhas)-1)
        print('posição a ser alterada é da rainha de coluna ', (colunaRainhaAlterada+1))
        for i in range(tabuleiro.dimensao):
            if listaRainhas[i][1] != colunaRainhaAlterada:
                tabuleiro.setRainha(listaRainhas[i][0], listaRainhas[i][1])
            else:
                novaLinha = random.randint(0,tabuleiro.dimensao-1)
                while novaLinha == listaRainhas[i][0]:
                    novaLinha = random.randint(0,tabuleiro.dimensao-1)
                tabuleiro.setRainha(novaLinha, colunaRainhaAlterada)
        return tabuleiro

    # Probabilidade de seguir na direção menos vantajosa
    def prob(self, valorVizinho, valorAtual, temperatura):
        delta = valorVizinho - valorAtual
        func = delta/temperatura
        result = math.exp(func)
        return result

    # Execução do algoritmo Simulated Annealing
    def execute(self, f):
        print('Executando o Simulated Annealing')
        t = 1
        while f(self.configAtual) > 0:
        # for t in range(1, self.maxIteracoes):
            temperatura = self.temperaturaInicial / self.resfriamento(t)
            atual = self.configAtual
            vizinho = Tabuleiro(self.configAtual.dimensao)
            vizinho = self.configuracaoSucessoraAleatoria(vizinho, atual.rainhas)
            vizinho.printTabuleiro()
            if f(vizinho) < f(self.configAtual):
                self.configAtual = vizinho
                print(f(self.configAtual))
            else:
                p = random.uniform(0,1)
                if self.prob(f(vizinho), f(atual), temperatura) > p:
                    self.configAtual = vizinho
                print(f(self.configAtual))
            t += 1