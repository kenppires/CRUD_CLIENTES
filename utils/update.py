from bdados import banco_dados, buscar_registro, mapa_campos, formatar_registros, campos_aceitos

def atualizar_registro(filtro, valor, **kwargs):
    registros_encontrados = buscar_registro(filtro, valor)
    
    if not registros_encontrados:
        return "Nenhum registro encontrado."
    
    total_atualizacoes = 0

    for registro in registros_encontrados:
        for campo, novo_valor in kwargs.items():
            campo_normalizado = campo.strip().lower()
            
            chave_real = None
            for key in mapa_campos:
                if key.lower() == campo_normalizado:
                    chave_real = mapa_campos[key]
                    break

            if not chave_real:
                return (f"Campo inválido: '{campo}'. "
                        f"Campos aceitos: {', '.join(campos_aceitos())}")

            registro[chave_real] = novo_valor
            total_atualizacoes += 1

    registros_formatados = formatar_registros(registros_encontrados)

    return f"{total_atualizacoes} campo(s) atualizado(s) com sucesso!\n\n{registros_formatados}"