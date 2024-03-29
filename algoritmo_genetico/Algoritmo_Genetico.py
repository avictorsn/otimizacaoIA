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
            if cromossomo[1] == 0:
                for j, cromo in enumerate(cromossomo[0]):
                    novoTabuleiro.setRainha(cromo, j)
                print("Tabuleiro ", i)
                novoTabuleiro.printTabuleiro()
    
    def printMelhor(self):
        melhor = self.populacao[0]
        novoTabuleiro = Tabuleiro(self.tamanhoTabuleiro)
        for j, cromo in enumerate(melhor[0]):
            novoTabuleiro.setRainha(cromo, j)
        novoTabuleiro.printTabuleiro()
        print('Ataques: ', melhor[1])

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
            auxReproducao = int(self.tamanhoTabuleiro/2)
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
        else:
            auxReproducao = int((self.tamanhoTabuleiro-1)/2)
            # gerando filho1
            for i in range(auxReproducao+1):
                filho1.append(x[i])
            for j in range(auxReproducao+1, self.tamanhoTabuleiro):
                filho1.append(y[j])
            # gerando filho2
            for i in range(auxReproducao+1):
                filho2.append(y[i])
            for j in range(auxReproducao+1, self.tamanhoTabuleiro):
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
                    faixa3.append(cromo[0])
                if (umQuarto * 3) <= i < (umQuarto * 4):
                    faixa4.append(cromo[0])
        else:
            umQuarto = (self.maxPopulacao + 1) / 4
            for i, cromo in enumerate(self.populacao):
                if i < umQuarto:
                    faixa1.append(cromo[0])
                if umQuarto <= i < (umQuarto * 2):
                    faixa2.append(cromo[0])
                if (umQuarto * 2) <= i < (umQuarto * 3):
                    faixa3.append(cromo[0])
                if (umQuarto * 3) <= i < (umQuarto * 4):
                    faixa4.append(cromo[0])
                if i == umQuarto * 4 - 1:
                    faixa4.append(cromo[0])
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

    def mutacao(self, child):
        ### a taxa de mutação deve ser entrada com valor entre 0 e 1
        chanceMutacao = random.uniform(0,1)
        alterou = False
        if chanceMutacao <= self.taxaMutacao:
            while not alterou:
                geneAleatorio = random.randint(0, self.tamanhoTabuleiro-1)
                valorAleatorio = random.randint(0, self.tamanhoTabuleiro-1)
                if child[0][geneAleatorio] != valorAleatorio:
                    child[0][geneAleatorio] = valorAleatorio
                    alterou = True

    def sortSecond(self, val):
        return val[1]

    def execute(self):
        nova_populacao = []
        atualPopulacao = self.populacao
        atualPopulacao.sort(key=self.sortSecond)
        numGeracoes = 1
        while atualPopulacao[0][1] != 0:
            print("Geração ", numGeracoes)
            self.printMelhor()
            for i in range(self.maxPopulacao):
                x = self.selecao_aleatoria_ponderada()
                while 1:
                    y = self.selecao_aleatoria_ponderada()
                    if y[0] != x[0]:
                        break
                child = self.reproduzCromossomo(x, y)
                # Implementar mutação aqui
                self.mutacao(child)
                nova_populacao.append(child)
            atualPopulacao = copy.deepcopy(nova_populacao)
            atualPopulacao.sort(key=self.sortSecond)
            numGeracoes += 1
        self.printMelhoresPopulacao()

        print("yay")
        
