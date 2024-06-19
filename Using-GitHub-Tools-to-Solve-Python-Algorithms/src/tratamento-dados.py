# tratamento-dados.py

def concatenar_dados(dado1, dado2):
    """
    Concatena dois dados fornecidos pelo usuário em uma única string.
    
    Args:
    dado1 (str): Primeiro dado de entrada.
    dado2 (str): Segundo dado de entrada.
    
    Returns:
    str: Os dados concatenados.
    """
    return dado1 + dado2

def verificar_palindromo(palavra):
    """
    Verifica se a palavra fornecida é um palíndromo.
    
    Args:
    palavra (str): Palavra a ser verificada.
    
    Returns:
    bool: True se a palavra for um palíndromo, False caso contrário.
    """
    return palavra == palavra[::-1]

if __name__ == "__main__":
    # Testes para concatenar_dados
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    print("Dados concatenados:", concatenar_dados(dado1, dado2))
    
    # Testes para verificar_palindromo
    palavra = input("Digite uma palavra para verificar se é um palíndromo: ")
    if verificar_palindromo(palavra):
        print(f"{palavra} é um palíndromo!")
    else:
        print(f"{palavra} não é um palíndromo.")
