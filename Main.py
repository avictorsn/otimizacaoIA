from simulated_annealing.SimulatedAnnealing import SimulatedAnnealing
from tabuleiro.Tabuleiro import Tabuleiro
import funcao_objetiva.FuncaoObjetiva as func
import os

dimensao = int(input('Digite a dimensão do tabuleiro (exemplo: 2 -> 2x2):'))

newTabuleiro = Tabuleiro(dimensao)

numRainhas = 0
while numRainhas < dimensao:
    os.system('cls' if os.name == 'nt' else 'clear')
    newTabuleiro.printTabuleiro()
    print('Rainha ', numRainhas+1)
    posX = int(input('Digite a linha da rainha : '))
    posY = numRainhas
    newTabuleiro.setRainha(posX-1, posY)
    numRainhas+=1

os.system('cls' if os.name == 'nt' else 'clear')
newTabuleiro.printTabuleiro()
print(func.f(newTabuleiro))