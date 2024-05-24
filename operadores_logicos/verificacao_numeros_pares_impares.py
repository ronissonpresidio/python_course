"""
   - Crie um programa que leia dois números e verifique se ambos são pares ou ímpares.
"""
def veririficar_par_ou_impar(numero):
    return numero % 2 == 0

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

paridade1 = veririficar_par_ou_impar(numero1)
paridade2 = veririficar_par_ou_impar(numero2)

if paridade1 and paridade2:
    print('Ambos os números são pares')
elif not paridade1 and not paridade2:
    print('Ambos os números são ímpares')
else:
    print('Um número é par e o outro é ímpar')