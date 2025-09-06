from bdados import banco_dados, buscar_registro

def ler_registro(filtro=None, valor=None):
    if filtro and valor:
        return buscar_registro(filtro, valor)
    return list(banco_dados.values())  # Retorna todos