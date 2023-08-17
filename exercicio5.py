def realizar_backup(dicionario, backup):
    # Copiar os dados do dicionário principal para o dicionário de backup
    backup.update(dicionario)
    # Limpar o dicionário principal
    dicionario.clear()

# Dicionário principal para armazenar os dados
dicionario_principal = {}

# Dicionário de backup
dicionario_backup = {}

while True:
    nome = input("Digite o nome (ou digite 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade: "))
    cpf = input("Digite o CPF: ")
    
    # Adicionando os dados ao dicionário principal
    dicionario_principal[cpf] = {
        'nome': nome,
        'idade': idade
    }
    
    # Realizar backup e limpar o dicionário principal se atingir tamanho 5
    if len(dicionario_principal) >= 5:
        print("Fazendo backup e limpando dicionário principal...")
        realizar_backup(dicionario_principal, dicionario_backup)

# Imprimindo o dicionário de backup no final
        print("Dicionário de backup:")
        for cpf, info in dicionario_backup.items():
            print(f"CPF: {cpf}, Nome: {info['nome']}, Idade: {info['idade']}")

#print("Dicionário principal:")
#for cpf, info in dicionario_principal.items():
#    print(f"CPF: {cpf}, Nome: {info['nome']}, Idade: {info['idade']}")