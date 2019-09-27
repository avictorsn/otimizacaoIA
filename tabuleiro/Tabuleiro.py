class Tabuleiro:
    def __init__(self, dimensao):
        self.dimensao = dimensao
        self.posicoes = []
        self.rainhas = []
        self.inicializarTabuleiro()

    def inicializarTabuleiro(self):
        for linha in range(self.dimensao):
            novaLinha = []
            for coluna in range(self.dimensao):
                novaLinha.append(' ')
            self.posicoes.append(novaLinha)

    def printTabuleiro(self):
        for linha in range(self.dimensao):
            print("|", end="")
            for coluna in range(self.dimensao):
                print(self.posicoes[linha][coluna], end="|")
            print()

    def getPeca(self, posicaoX, posicaoY):
        return self.posicoes[posicaoX][posicaoY]

    def setPeca(self, posicaoX, posicaoY, peca):
        self.posicoes[posicaoX][posicaoY] = peca
    
    def setRainha(self, posicaoX, posicaoY):
        self.setPeca(posicaoX,posicaoY, 'Q')
        self.rainhas.append([posicaoX, posicaoY])
    
    def getRainha(self, indexRainha):
        return self.rainhas[indexRainha]
    