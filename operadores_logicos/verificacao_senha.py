"""
- Escreva um programa que peça ao usuário para digitar uma senha e verifique se ela contém pelo menos 8 caracteres e tem pelo menos um número.
"""

def verificar_senha(senha):
    if len(senha) < 8:
        return False
    
    tem_numero = any(char.isdigit() for char in senha)
    
    return tem_numero

senha = input('Digite sua senha: ')

if verificar_senha(senha):
    print('Senha válida.')
else:
    print('Senha inválida. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.')
