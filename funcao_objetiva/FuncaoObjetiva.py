from tabuleiro.Tabuleiro import Tabuleiro

#Função que avalia quantos ataques tem uma configuração de entrada
def f(tabuleiro: Tabuleiro):
    numAtaques = 0
    ataqueHorizontalDireita = False
    ataqueDiagDirSup = False
    dimensaoPar = (tabuleiro.dimensao%2==0)
    
    ### verificação de ataques
    
    for rainha in range(len(tabuleiro.rainhas)):
        ataqueHorizontalDireita = False
        ataqueDiagEsqSup = False
        ataqueDiagDirSup = False
        linhaRainha = tabuleiro.rainhas[rainha][0]
        colunaRainha = tabuleiro.rainhas[rainha][1]
        #horizontal pela direita
        for coluna in range(tabuleiro.dimensao):
            if(coluna!= colunaRainha):
                if(tabuleiro.posicoes[linhaRainha][coluna] == 'Q' and not ataqueHorizontalDireita):
                    numAtaques+=1
                    ataqueHorizontalDireita = True

        ### Falta corrigir o erro de contabilizar duas vezes o mesmo ataque ###
        #verificação diagonal direita superior
        if(linhaRainha > 0 and colunaRainha < tabuleiro.dimensao):
            for linha in range(linhaRainha-1, -1, -1):
                for coluna in range(colunaRainha+1, tabuleiro.dimensao):
                    if(tabuleiro.posicoes[linha][coluna] == 'Q' and not ataqueDiagDirSup):
                        numAtaques+=1
                        coluna = tabuleiro.dimensao
                        ataqueDiagDirSup = True

        #verificação diagonal esquerda superior
        if(linhaRainha > 0 and colunaRainha < tabuleiro.dimensao):
            for linha in range(linhaRainha-1, -1, -1):
                for coluna in range(colunaRainha-1, -1, -1):
                    if(tabuleiro.posicoes[linha][coluna] == 'Q' and not ataqueDiagEsqSup):
                        numAtaques+=1
                        coluna = tabuleiro.dimensao
                        ataqueDiagEsqSup = True
                
    
    return numAtaques