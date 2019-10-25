from simulated_annealing.SimulatedAnnealing import SimulatedAnnealing
from algoritmo_genetico.Algoritmo_Genetico import AlgoritmoGenetico
from tabuleiro.Tabuleiro import Tabuleiro
import funcao_objetiva.FuncaoObjetiva as func
import os



dimensao = int(input('Digite a dimensão do tabuleiro (exemplo: 4 -> 4x4): '))

newTabuleiro = Tabuleiro(dimensao)

numRainhas = 0
while numRainhas < dimensao:
    os.system('cls' if os.name == 'nt' else 'clear')
    newTabuleiro.printTabuleiro()
    print('Rainha ', numRainhas + 1)
    posX = int(input('Digite a linha da rainha : '))
    posY = numRainhas
    newTabuleiro.setRainha(posX - 1, posY)
    numRainhas += 1

os.system('cls' if os.name == 'nt' else 'clear')
metodo = int(input("Digite 1 para 'Simulated Annealing' ou 2 para 'Algoritmo Genético': "))

### Simulated Annealing
if metodo == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    temperaturaInicial = int(input("Digite o valor da temperatura inicial(0 para teste): "))
    if temperaturaInicial < 0:
        print('Temperatura inválida')
    elif temperaturaInicial == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        newTabuleiro.printTabuleiro()
        s = SimulatedAnnealing(newTabuleiro, 50, 100)
        s.execute(func.f)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        newTabuleiro.printTabuleiro()
        s = SimulatedAnnealing(newTabuleiro, 50, temperaturaInicial)
        s.execute(func.f)

### Algoritmo Genético
elif metodo == 2:
    os.system('cls' if os.name == 'nt' else 'clear')
    teste = int(input("Digite '1' para teste, ou '0' para atribuir valores de entrada: "))
    if teste == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        newTabuleiro.printTabuleiro()
        a = AlgoritmoGenetico(newTabuleiro, 200, 100, 0.5, dimensao)
        a.execute()
    elif teste == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        maxPopulacao = int(input("Digite o tamanho máximo da população(mínimo = 2): "))
        taxaMutacao = float(input("Digite a taxa de mutação(valor entre 0 e 1): "))
        if maxPopulacao < 1 or (taxaMutacao>1.0 or taxaMutacao<0.0):
            print("Dados inválidos")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            newTabuleiro.printTabuleiro()
            a = AlgoritmoGenetico(newTabuleiro, 200, maxPopulacao, taxaMutacao, dimensao)
            a.execute()
    else:
        print("Entrada inválida")
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Escolha inválida')

