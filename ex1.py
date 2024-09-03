'''1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores 
anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um 
número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou 
não a sequência.
IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser 
previamente definido no código;

Um número é Fibonacci se apenas se uma ou ambas as expressões 
5*n2 + 4 ou 5*n2 – 4 retornarem um quadrado perfeito.'''

from math import sqrt

#Verificar se é um quadrado perfeito Ex: Se x = 16, raiz = 4, e 4 * 4 = 16, então x é um quadrado perfeito.
def quadradoPerfeito(x):
    raiz = int(sqrt(x))
    return raiz*raiz == x

#Verifica se é fibonacci se ao menos 1 condição for atendida
def eFibonacci(n):
    return quadradoPerfeito(5*n*n+4) or quadradoPerfeito(5*n*n-4)

def main():
    n = int(input('Digite 1 numero positivo para verificar se pertence a sequencia de fibonacci: '))

    if(eFibonacci(n)):
        print(f'{n} pertence a sequencia de Fibonacci.')
    else:
        print(f'{n} Não pertence a sequencia de Fibonacci')


if __name__ == '__main__':
    main()