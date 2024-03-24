def calcular_media_notas():
    # Solicita o nome do aluno
    nome_aluno = input("Digite o nome do aluno: ").strip()

    # Solicita as duas notas do alunoKarina
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    # Calcula a média das notas
    media = (nota1 + nota2) / 2

    # Determina a situação do aluno com base na média
    situacao = "Aprovado" if media >= 6 else "Reprovado"

    # Exibe a média e a situação do aluno
    print(f"\nAluno: {nome_aluno}\nMédia: {media:.2f}\nSituação: {situacao}")

# Chamar a função para executar o programa
calcular_media_notas()