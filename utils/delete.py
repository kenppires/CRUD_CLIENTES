from bdados import banco_dados, buscar_registro, formatar_registros

def deletar_registro(filtro, valor):
    registros = buscar_registro(filtro, valor)
    if not registros or isinstance(registros, str):
        return registros if isinstance(registros, str) else "Nenhum registro encontrado."

    num_registros = len(registros)
    print(f"\n{num_registros} registro(s) encontrado(s):")
  
    print(formatar_registros(registros))
    confirm = input("Tem certeza que deseja deletar esses registros? (s/n): ").strip().lower()

    if confirm == "s":
        for reg in registros:
            del banco_dados[reg["ID"]]
        return f"{len(registros)} registro(s) deletado(s)."
    return "Operação cancelada."