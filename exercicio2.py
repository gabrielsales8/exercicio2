nome  = input('Digite o nome:')
idade  = input('Digite a idade:')
telefone  = input('Digite o telefone:')
endereco  = input('Digite o endereço:')

d = {'nome': nome, 'idade': idade, 'telefone': telefone, 'endereco': endereco,}
for chave, valor in sorted(d.items()):
    print(f"{chave}: {valor}")
