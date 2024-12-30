def calcular_imc(peso, altura):
    """
    Função para calcular o IMC.
    Parâmetros:
    peso (float): Peso em kg
    altura (float): Altura em metros
    
    Retorna:
    float: O IMC calculado
    """
    return peso / (altura ** 2)


def get_valid_input():
    """
    Função para garantir que a entrada do usuário seja válida.
    
    Retorna:
    tuple: Peso e altura fornecidos pelo usuário.
    """
    while True:
        try:
            peso = float(input("Digite seu peso (em kg): "))
            altura = float(input("Digite sua altura (em metros): "))
            
            # Validação das entradas
            if peso <= 0 or altura <= 0:
                print("Por favor, insira valores positivos para peso e altura.")
            else:
                return peso, altura
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido para peso e altura.")


def exibir_resultado(imc):
    """
    Função para exibir o resultado do cálculo do IMC.
    Parâmetro:
    imc (float): O IMC calculado
    """
    print(f"O seu IMC é: {imc:.2f}")
    if imc < 18.5:
        print("Classificação: Abaixo do peso.")
    elif 18.5 <= imc < 24.9:
        print("Classificação: Peso normal.")
    elif 25 <= imc < 29.9:
        print("Classificação: Sobrepeso.")
    else:
        print("Classificação: Obesidade.")


def main():
    """
    Função principal que executa o cálculo e exibe o resultado do IMC.
    """
    print("Bem-vindo ao calculador de IMC!")
    
    # Obter peso e altura com validação
    peso, altura = get_valid_input()
    
    # Calcular IMC
    imc = calcular_imc(peso, altura)
    
    # Exibir o resultado
    exibir_resultado(imc)


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox

def calcular_imc_gui():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        # Validação dos dados
        if peso <= 0 or altura <= 0:
            messagebox.showerror("Erro", "Por favor, insira valores positivos para peso e altura.")
            return

        imc = peso / (altura ** 2)

        # Classificação do IMC
        if imc < 18.5:
            resultado = f"Seu IMC é: {imc:.2f}\nClassificação: Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            resultado = f"Seu IMC é: {imc:.2f}\nClassificação: Peso normal"
        elif 25 <= imc < 29.9:
            resultado = f"Seu IMC é: {imc:.2f}\nClassificação: Sobrepeso"
        else:
            resultado = f"Seu IMC é: {imc:.2f}\nClassificação: Obesidade"
        
        label_resultado.config(text=resultado)
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos para peso e altura.")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de IMC")

# Labels e entradas de dados
label_peso = tk.Label(root, text="Peso (kg):")
label_peso.pack()
entry_peso = tk.Entry(root)
entry_peso.pack()

label_altura = tk.Label(root, text="Altura (m):")
label_altura.pack()
entry_altura = tk.Entry(root)
entry_altura.pack()

# Botão de calcular
botao_calcular = tk.Button(root, text="Calcular IMC", command=calcular_imc_gui)
botao_calcular.pack()

# Label para exibir o resultado
label_resultado = tk.Label(root, text="", font=("Helvetica", 14))
label_resultado.pack()

# Rodando a interface gráfica
root.mainloop()
