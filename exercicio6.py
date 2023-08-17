def contar_vogais(texto):
    # Definindo as vogais a serem consideradas
    vogais = 'aeiouAEIOU'
    
    # Inicializando o dicionário para armazenar a contagem de vogais
    contagem_vogais = {}
    
    for letra in texto:
        if letra in vogais:
            # Convertendo a letra para minúscula antes de contar
            letra = letra.lower()
            if letra in contagem_vogais:
                contagem_vogais[letra] += 1
            else:
                contagem_vogais[letra] = 1
    
    return contagem_vogais

# Solicitando o texto ao usuário
texto = input("Digite o texto: ")

# Chamando a função para contar as vogais no texto
resultado = contar_vogais(texto)

# Imprimindo o resultado
for vogal, quantidade in resultado.items():
    print(f"{vogal}: {quantidade}")
