print("Vamos calcular sua média!")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Média igual a: {media}")
if media >= 70:
    print("Aprovado!")
else:
    print("Reprovado!")