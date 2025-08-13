import random
import string
import time

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

    senha = "".join(random.choice(caracteres_disponiveis) for _ in range(comprimento_minimo))
    return senha

def inicio():
    cliente = {}
    lista = []

    print("\n####################   Sys-Passw *** ####################\n")
    print("Um Aplicativo feito para você gerar Senhas ou Tokens, e usar onde quiser!\n")
    print("✌️✌️✌️✌️ 😆😆😆😆")

    # Pergunta o tamanho da senha
    while True:
        try:
            comprimento = int(input("Comprimento da senha/código que deseja criar: "))
            if comprimento < 6:
                print('Tamanho mínimo é 6 caracteres...')
            elif comprimento > 12:
                print('Tamanho máximo é 12 caracteres.')
            else:
                break
        except ValueError:
            print("Erro: Digite um número válido!")

    # Pergunta quais tipos de caracteres incluir
    while True:
        maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower()
        minusculas = input("Incluir letras minúsculas? (s/n): ").strip().lower()
        numeros = input("Incluir números? (s/n): ").strip().lower()
        especiais = input("Incluir caracteres especiais? (s/n): ").strip().lower()

        if maiusculas not in ['s','sim','n','nao'] or minusculas not in ['s','sim','n','nao'] \
        or numeros not in ['s','sim','n','nao'] or especiais not in ['s','sim','n','nao']:
            print("Respostas inválidas! Use apenas s/n ou sim/não.")
            continue

        if maiusculas == 'n' and minusculas == 'n' and numeros == 'n' and especiais == 'n':
            print("Nenhuma opção selecionada. Encerrando... 😢😢")
            time.sleep(2.5)
            return  # Sai da função, encerrando

        break

    incluir_maiusculas = maiusculas in ['s', 'sim']
    incluir_minusculas = minusculas in ['s', 'sim']
    incluir_numeros = numeros in ['s', 'sim']
    incluir_especiais = especiais in ['s', 'sim']

    # Gera a senha
    senha = gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais)

    print("\nGerando senha... Aguarde.\n")
    time.sleep(3.0)
    print(f"Senha gerada: {senha}\n")

    # Testa a senha no "login"
    while True:
        print("Vamos fazer um teste da senha gerada, simulando um LOGIN.\n")
        cliente['Login'] = input('Endereço e-mail ou Usuário: ')
        cliente['Senha'] = input('Digite a senha Gerada: ')
        lista.append(cliente.copy())

        if senha == cliente['Senha']:
            print('Senha correta! Está pronta para uso. ✅')
            sair = input('Deseja sair? (s/n): ').strip().lower()
            if sair in ['s', 'sim']:
                return  # Sai da função → encerra o programa
            elif sair in ['n', 'nao']:
                print("\nredirecionando para o inicio do programa...\n")
                time.sleep(3.0)
                return inicio()  # Chama a função de novo → reinicia
        else:
            print('A senha gerada está incorreta, digite exatamente como foi mostrada.')

fim = print("Fim!!!")

# Programa inicia aqui
inicio()
