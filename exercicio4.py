pessoas = {}

# Cadastrar informações das pessoas
while True:
    nome = input("Digite o nome (ou digite 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade: "))
    cpf = input("Digite o CPF: ")
    
    # Dados do dicionário principal
    pessoas[cpf] = {
        'nome': nome,
        'idade': idade
    }

# dicionário para os menores de 18 anos
menores_de_idade = {}

# Removendo e transferindo as pessoas menores de 18 anos para o novo dicionário
for cpf, info in pessoas.copy().items():
    if info['idade'] < 18:
        menores_de_idade[cpf] = info
        del pessoas[cpf]

# PRINT das pessoas maiores de 18 anos
print("Pessoas maiores de 18 anos:")
for cpf, info in pessoas.items():
    print(f"CPF: {cpf}, Nome: {info['nome']}, Idade: {info['idade']}")

# PRINT pessoas menores de 18 anos
print("\nPessoas menores de 18 anos:")
for cpf, info in menores_de_idade.items():
    print(f"CPF: {cpf}, Nome: {info['nome']}, Idade: {info['idade']}")
