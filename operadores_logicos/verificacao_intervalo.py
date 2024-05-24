"""
Escreva um programa que leia um número e verifique se ele está no intervalo de 10 a 20, inclusive.
"""

numero_digitado = int(input())

print(f'{numero_digitado in range(10,20 + 1)}')