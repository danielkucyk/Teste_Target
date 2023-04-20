# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...).
# Escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 

def Fibonacci(numero):
    Fib1 = 0
    Fib2 = 1

    while numero > Fib2:
        FibNext = Fib1 + Fib2
        Fib1 = Fib2
        Fib2 = FibNext

    if numero == Fib2:
        print("Pertence a sequencia de Fibonacci!")
    else:
        print("Não pertence a sequencia de Fibonaaci!")


numero = float(input("Digite um numero: "))

Fibonacci(numero)

