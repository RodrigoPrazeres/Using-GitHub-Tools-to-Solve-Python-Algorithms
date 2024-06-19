# operacoes-matematicas.py

def operacoes_simples(num1, num2, operacao):
    """
    Realiza uma operação matemática simples entre dois números.
    
    Args:
    num1 (float): Primeiro número.
    num2 (float): Segundo número.
    operacao (str): Operação a ser realizada: "soma", "subtracao", "multiplicacao", "divisao".
    
    Returns:
    float: Resultado da operação.
    """
    if operacao == "soma":
        return num1 + num2
    elif operacao == "subtracao":
        return num1 - num2
    elif operacao == "multiplicacao":
        return num1 * num2
    elif operacao == "divisao":
        return num1 / num2
    else:
        raise ValueError("Operação inválida.")

def calcular_media(nota1, nota2, nota3):
    """
    Calcula a média de três notas.
    
    Args:
    nota1 (float): Primeira nota.
    nota2 (float): Segunda nota.
    nota3 (float): Terceira nota.
    
    Returns:
    float: Média das notas.
    """
    return (nota1 + nota2 + nota3) / 3

def verificar_par_impar(numero):
    """
    Verifica se um número é par ou ímpar.
    
    Args:
    numero (int): Número a ser verificado.
    
    Returns:
    str: "par" se o número for par, "ímpar" se o número for ímpar.
    """
    return "par" if numero % 2 == 0 else "ímpar"

if __name__ == "__main__":
    # Testes para operacoes_simples
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ")
    print("Resultado da operação:", operacoes_simples(num1, num2, operacao))
    
    # Testes para calcular_media
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    print("Média das notas:", calcular_media(nota1, nota2, nota3))
    
    # Testes para verificar_par_impar
    numero = int(input("Digite um número para verificar se é par ou ímpar: "))
    print(f"O número {numero} é {verificar_par_impar(numero)}.")
