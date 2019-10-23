from tabuleiro.Tabuleiro import Tabuleiro
import funcao_objetiva.FuncaoObjetiva as func
import copy
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

    def printMelhoresPopulacao(self):
        print("MELHORES TABULEIROS")
        for i,cromossomo in enumerate(self.populacao):
            novoTabuleiro = Tabuleiro(self.tamanhoTabuleiro)
            if i == 5:
                break
            for j, cromo in enumerate(cromossomo[0]):
                novoTabuleiro.setRainha(cromo, j)
            print("Tabuleiro ", i)
            novoTabuleiro.printTabuleiro()

    def criaCromossomo(self):
        rainhas = np.arange(self.tamanhoTabuleiro)
        np.random.shuffle(rainhas)
        return rainhas

    def avaliarCromossomo(self, cromossomo):
        novoTabuleiro = Tabuleiro(self.tamanhoTabuleiro)
        for i, cromo in enumerate(cromossomo):
            novoTabuleiro.setRainha(cromo, i)
        return func.f(novoTabuleiro)

    def reproduzCromossomo(self, x, y):
        filho1 = []
        filho2 = []
        if self.tamanhoTabuleiro % 2 == 0:
            paridade = 0
        else:
            paridade = 1
        if paridade == 0:
            auxReproducao = self.tamanhoTabuleiro % 2
            # gerando filho1
            for i in range(auxReproducao):
                filho1.append(x[i])
            for j in range(auxReproducao, self.tamanhoTabuleiro):
                filho1.append(y[j])
            # gerando filho2
            for i in range(auxReproducao):
                filho2.append(y[i])
            for j in range(auxReproducao, self.tamanhoTabuleiro):
                filho2.append(x[j])
            nota1 = self.avaliarCromossomo(filho1)
            nota2 = self.avaliarCromossomo(filho2)
            if nota1 < nota2:
                return (filho1, nota1)
            else:
                return (filho2, nota2)

    def criaPopulacao(self):
        population = []
        for i in range(self.maxPopulacao):
            tabuleiro = self.criaCromossomo()
            avaliacao = self.avaliarCromossomo(tabuleiro)
            population.append((tabuleiro, avaliacao))
        return population

    def selecao_aleatoria_ponderada(self):
        faixa1 = []
        faixa2 = []
        faixa3 = []
        faixa4 = []
        if self.maxPopulacao % 2 == 0:
            paridade = 0
        else:
            paridade = 1
        if paridade == 0:
            umQuarto = self.maxPopulacao / 4
            for i, cromo in enumerate(self.populacao):
                if i < umQuarto:
                    faixa1.append(cromo[0])
                if umQuarto <= i < (umQuarto * 2):
                    faixa2.append(cromo[0])
                if (umQuarto * 2) <= i < (umQuarto * 3):
                    faixa2.append(cromo[0])
                if (umQuarto * 3) <= i < (umQuarto * 4):
                    faixa2.append(cromo[0])
        else:
            umQuarto = (self.maxPopulacao + 1) / 4
            for i, cromo in enumerate(self.populacao):
                if i < umQuarto:
                    faixa1.append(cromo[0])
                if umQuarto <= i < (umQuarto * 2):
                    faixa2.append(cromo[0])
                if (umQuarto * 2) <= i < (umQuarto * 3):
                    faixa2.append(cromo[0])
                if (umQuarto * 3) <= i < (umQuarto * 4):
                    faixa2.append(cromo[0])
                if i == umQuarto * 4 - 1:
                    faixa2.append(cromo[0])
        while 1:
            dado_100_faces = np.random.randint(1, 100)

            if dado_100_faces <= 5:
                if len(faixa4) > 0:
                    tamanho = len(faixa4)
                    indice = np.random.randint(tamanho)
                    return faixa4[indice]
            elif dado_100_faces <= 15 and dado_100_faces > 5:
                if len(faixa3) > 0:
                    tamanho = len(faixa3)
                    indice = np.random.randint(tamanho)
                    return faixa3[indice]
            elif dado_100_faces <= 45 and dado_100_faces > 15:
                if len(faixa2) > 0:
                    tamanho = len(faixa2)
                    indice = np.random.randint(tamanho)
                    return faixa2[indice]
            elif 100 >= dado_100_faces > 45:
                if len(faixa1) > 0:
                    tamanho = len(faixa1)
                    indice = np.random.randint(tamanho)
                    return faixa1[indice]

    def sortSecond(self, val):
        return val[1]

    def execute(self):
        nova_populacao = []
        atualPopulacao = self.populacao
        atualPopulacao.sort(key=self.sortSecond)
        while atualPopulacao[0][1] != 0:
            for i in range(self.maxPopulacao):
                x = self.selecao_aleatoria_ponderada()
                while 1:
                    y = self.selecao_aleatoria_ponderada()
                    if y != x:
                        break
                child = self.reproduzCromossomo(x, y)
                # Implementar mutação aqui
                nova_populacao.append(child)
            atualPopulacao = copy.deepcopy(nova_populacao)
            atualPopulacao.sort(key=self.sortSecond)
        self.printMelhoresPopulacao()

        print("yay")
