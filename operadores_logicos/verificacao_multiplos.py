"""
   - Crie um programa que leia um número do usuário e verifique se ele é múltiplo de 3 e 5 ao mesmo tempo.
"""

numero_digitado = int(input('Digite um número: '))

if numero_digitado % 3 == 0 and numero_digitado % 5 == 0:
    print('O número digitado é multiplo de 3 e 5')
else:
    print('O número não é multiplo de 3 e 5') 