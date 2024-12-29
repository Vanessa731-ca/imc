# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso adequado"
    elif 25 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30 <= imc <= 34.9:
        return "Obesidade grau I"
    elif 35 <= imc <= 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

# Entrada do usuário
print("Bem-vindo ao cálculo de IMC!")
altura = float(input("Digite sua altura em metros (ex: 1.75): "))
peso = float(input("Digite seu peso em kg (ex: 70): "))

# Cálculo e exibição do resultado
imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
