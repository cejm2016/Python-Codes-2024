
###########  PROJETOOOOOOO , PARABENS BRUNO E OBRIGADO PELO INCENTIVO!!! ###########

import random
import string
import json
import time

#Dicionario com Lista e Tuplaaa

Projeto=()
title = ("Seja bem vindo ao Sis-Passw gerador de Senhas!").title()

print(f"\n####################   Password ****** ####################\n"
      f" Aplicativo feito para você gerar senhas aleatórias e usar em suas redes sociais! \n")
print(title)
print("\n ✌️✌️✌️✌️ 😆😆😆😆")


cliente={}
lista=[]

def gerar_senha(comprimento_minimo=6, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiais=True):
    if not (incluir_maiusculas or incluir_minusculas or incluir_numeros or incluir_especiais):
        raise ValueError("Pelo menos uma categoria de caracteres deve ser incluída.")

    caracteres_disponiveis = ""
    if incluir_maiusculas:
        caracteres_disponiveis += string.ascii_uppercase
    if incluir_minusculas:
        caracteres_disponiveis += string.ascii_lowercase
    if incluir_numeros:
        caracteres_disponiveis += string.digits
    if incluir_especiais:
        caracteres_disponiveis += string.punctuation

    senha = ''.join(random.choice(caracteres_disponiveis) for _ in range(comprimento_minimo))
    return senha

while True:
    comprimento = int(input("Comprimento da senha que deseja criar: "))
    if comprimento <=5:
        print('Tamanho minimo é 6 caracteres...')
    elif comprimento > 12:
            print('Tamanho máximo é 12')
    else:
        break
print("\n")
print("Nas condições de inclusão usei RAISE... se todas forem não, irá fechar ️😢😢😢😢...\n")

maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
numeros = input("Incluir números? (s/n): ").lower() == 's'
especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'
print("\n")
senha = gerar_senha(comprimento, maiusculas, minusculas, numeros, especiais)

print(f"Gerando senha... Aguarde. \n")
time.sleep(5)
print(f"Senha gerada: {senha}\n")


while True:
    print(f'Vamos fazer um teste da senha GERADA, simulando um LOGIN\n,'
          f' Copie a senha Anterior e use-a...\n')
    cliente['Login'] = input('Endereço e-mail ou Usuário: ')
    cliente['Senha'] = input('Digite a senha Gerada: ')
    lista.append(cliente.copy())
    if senha == cliente['Senha']:
        print('A senha digitada coincide e está pronta para ser usada em suas redes sociais...')
        sair = input('deseja sair ? s/n : ')
        if sair.lower() == 's' or sair.lower() == 'sim':
            break
    else:
        print('A senha gerada está incorreta, digite a SENHA que pediu')

fim = input(f'\nFIM ...\n')


#################### FIM #######################



