def calcular_media_tempos(tempos):
    media = sum(tempos) / len(tempos)
    return media

corredores = {
    "Corredor 1": [], "Corredor 2": [], "Corredor 3": [], "Corredor 4": [], "Corredor 5": [], "Corredor 6": []
}

for volta in range(1, 11):
    print(f"Volta {volta}:")
    for corredor in corredores:
        tempo = float(input(f"Digite o tempo do {corredor} (em segundos): "))
        corredores[corredor].append(tempo)

melhor_volta = float("inf")
melhor_corredor = None
melhor_volta_numero = None

classificacao = []

for corredor, tempos in corredores.items():
    media_corredor = calcular_media_tempos(tempos)
    classificacao.append((corredor, media_corredor))
    
    if min(tempos) < melhor_volta:
        melhor_volta = min(tempos)
        melhor_corredor = corredor
        melhor_volta_numero = tempos.index(melhor_volta) + 1

classificacao = sorted(classificacao, key=lambda x: x[1])

print("\nMelhor volta da prova:")
print(f"Corredor: {melhor_corredor}")
print(f"Volta: {melhor_volta_numero}")
print("\nClassificação final:")
for posicao, (corredor, media) in enumerate(classificacao, start=1):
    print(f"{posicao}º lugar: {corredor} - Média de tempos: {media:.2f} segundos")
