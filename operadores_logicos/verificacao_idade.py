"""
Escreva um programa que pergunte a idade do usuário e verifique se ele tem idade suficiente para votar (18 anos ou mais).
"""

idade_usuario = int(input('Digite sua idade: '))

if idade_usuario >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')