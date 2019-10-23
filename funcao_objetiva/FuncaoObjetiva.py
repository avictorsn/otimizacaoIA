from tabuleiro.Tabuleiro import Tabuleiro

#Função que avalia quantos ataques tem uma configuração de entrada
def f(tabuleiro: Tabuleiro):
    numAtaques = 0
    ataqueHorizontalDireita = False
    ataqueDiagDirSup = False
    dimensaoPar = (tabuleiro.dimensao%2==0)
    
    ### verificação de ataques
    
    for rainha in tabuleiro.rainhas:
        #ataque horizontal
        for outraRainha in tabuleiro.rainhas:
            if outraRainha[0] == rainha[0] and rainha != outraRainha:
                numAtaques += 1
            #ataque diagonal esquerda superior
            if outraRainha[1] < rainha[1] and outraRainha[0] < rainha[0]:
                distanciaColuna = abs(rainha[1]-outraRainha[1])
                linhaDeAtaque = rainha[0]-distanciaColuna
                if linhaDeAtaque >= 0 and linhaDeAtaque == outraRainha[0]:
                    numAtaques += 1
            # ataque diagonal esquerda inferior
            if outraRainha[1] < rainha[1] and outraRainha[0] > rainha[0]:
                distanciaColuna = abs(rainha[1] - outraRainha[1])
                linhaDeAtaque = rainha[0] + distanciaColuna
                if linhaDeAtaque >= 0 and linhaDeAtaque == outraRainha[0]:
                    numAtaques += 1
            #ataque diagonal direita superior
            if outraRainha[1] > rainha[1] and outraRainha[0] < rainha[0]:
                distanciaColuna = abs(rainha[1]-outraRainha[1])
                linhaDeAtaque = rainha[0]-distanciaColuna
                if linhaDeAtaque >= 0 and linhaDeAtaque == outraRainha[0]:
                    numAtaques += 1
            # ataque diagonal direita inferior
            if outraRainha[1] > rainha[1] and outraRainha[0] > rainha[0]:
                distanciaColuna = abs(rainha[1] - outraRainha[1])
                linhaDeAtaque = rainha[0] + distanciaColuna
                if linhaDeAtaque >= 0 and linhaDeAtaque == outraRainha[0]:
                    numAtaques += 1

    return numAtaques/2