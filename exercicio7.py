def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

alunos = {}
while True:
    nome = input("Digite o nome do aluno (ou deixe vazio para sair): ")
    if nome == "":
        break
    
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    
    alunos[nome] = [nota1, nota2]

for aluno, notas in alunos.items():
    media_aluno = calcular_media(notas)
    print(f"Média do(a) {aluno}: {media_aluno:.2f}")
