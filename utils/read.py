from bdados import banco_dados, mapa_campos

def ler_registro(filtro=None, valor=None):
    if filtro:
        campo = mapa_campos.get(filtro.lower().strip())
        if not campo:
            return f"Campo '{filtro}' inválido."

        if not valor:
            registros = [r for r in banco_dados.values() if campo in r and r[campo]]
            return registros
        else:
            resultados = []
            for r in banco_dados.values():
                if campo == "ID":
                    if str(r.get("ID", "")) == valor:  # ID exato
                        resultados.append(r)
                elif campo in ["CPF", "CNPJ"]:
                    if campo in r and valor.lower() in str(r[campo]).lower():
                        resultados.append(r)
                elif campo in r and valor.lower() in str(r[campo]).lower():
                    resultados.append(r)
            return resultados
    return list(banco_dados.values())