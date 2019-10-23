from tabuleiro.Tabuleiro import Tabuleiro
import funcao_objetiva.FuncaoObjetiva as func
import math
import random
import numpy as np


# genótipo = colunas, exemplo [3,1,2] - rainha 1 na linha 3, rainha 2 na linha 1 e rainha 3 na linha 2
class AlgoritmoGenetico:
    def __init__(self, configInicial: Tabuleiro, maxIteracoes, maxPopulacao, taxaMutacao, tamanhoTabuleiro):
        self.configInicial = configInicial
        self.maxIteracoes = maxIteracoes
        self.maxPopulacao = maxPopulacao
        self.taxaMutacao = taxaMutacao
        self.configAtual = configInicial
        self.tamanhoTabuleiro = tamanhoTabuleiro
        self.populacao = self.criaPopulacao()

    def printTabuleiro(self):
        print(self.configAtual)

    def criaCromossomo(self):
        rainhas = np.arange(self.tamanhoTabuleiro)
        np.random.shuffle(rainhas)
        return rainhas

    def avaliarCromossomo(self, cromossomo):
        novoTabuleiro = Tabuleiro(self.tamanhoTabuleiro)
        for i, cromo in enumerate(cromossomo):
            novoTabuleiro.setRainha(cromo, i)
        return func.f(novoTabuleiro)

    def criaPopulacao(self):
        population = []
        for i in range(self.maxPopulacao):
            tabuleiro = self.criaCromossomo()
            avaliacao = self.avaliarCromossomo(tabuleiro)
            population.append([tabuleiro, avaliacao])
        return population
