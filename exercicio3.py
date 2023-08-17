agenda = {}

# Loop para ler os dados da agenda
while True:
    cpf = input("Digite o CPF (ou digite 'sair' para encerrar): ")
    if cpf.lower() == 'sair':
        break
    
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    telefone = input("Digite o telefone: ")
    
    # Dados do dicionário
    agenda[cpf] = {
        'nome': nome,
        'idade': idade,
        'telefone': telefone
    }

# Print da agenda no formato "chave: nome-idade-telefone"
for cpf, dados in agenda.items():
    print(f"{cpf}: {dados['nome']}-{dados['idade']}-{dados['telefone']}")
