# repete-texto.py

def repetir_texto(texto, vezes):
    """
    Repete uma string um número específico de vezes.
    
    Args:
    texto (str): Texto a ser repetido.
    vezes (int): Número de vezes que o texto deve ser repetido.
    
    Returns:
    str: Texto repetido.
    """
    return texto * vezes

if __name__ == "__main__":
    # Teste para repetir_texto
    texto = input("Digite o texto a ser repetido: ")
    vezes = int(input("Digite o número de vezes que o texto deve ser repetido: "))
    print("Texto repetido:", repetir_texto(texto, vezes))
