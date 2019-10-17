from tabuleiro.Tabuleiro import Tabuleiro

def f(tabuleiro: Tabuleiro):
    numAtaques = 0
    ataqueHorizontal = False
    ataqueDiagDirSup = False
    dimensaoPar = (tabuleiro.dimensao%2==0)
    #verificação horizontal
    for rainha in range(len(tabuleiro.rainhas)):
        ataqueHorizontal = False
        ataqueDiagDirSup = False
        # print('Rainha ', rainha+1)
        linhaRainha = tabuleiro.rainhas[rainha][0]
        colunaRainha = tabuleiro.rainhas[rainha][1]
        for coluna in range(tabuleiro.dimensao):
            if(coluna!= colunaRainha):
                if(tabuleiro.posicoes[linhaRainha][coluna] == 'Q' and not ataqueHorizontal):
                    # print('horizontal')
                    # print('linha ', linhaRainha, ' coluna ', coluna, ' está atacando a Rainha', rainha+1)
                    numAtaques+=1
                    ataqueHorizontal = True

        ### Falta corrigir o erro de contabilizar duas vezes o mesmo ataque ###
        #verificação diagonal direita superior
        if(linhaRainha > 0 and colunaRainha < tabuleiro.dimensao):
            if(True):
                for linha in range(linhaRainha-1, -1, -1):
                    for coluna in range(colunaRainha+1, tabuleiro.dimensao):
                        # print(linha, '; ', coluna)
                        if(tabuleiro.posicoes[linha][coluna] == 'Q' and not ataqueDiagDirSup):
                            # print('diagonal direita superior')
                            # print('linha ', linhaRainha, ' coluna ', coluna, ' está atacando a Rainha', rainha+1)
                            numAtaques+=1
                            coluna = tabuleiro.dimensao
                            ataqueDiagDirSup = True
                
    
    return numAtaques