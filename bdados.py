# bdados.py

banco_dados = {1: {'ID': 1, 'Nome': 'Ana Silva', 'CPF': '123.456.789-00', 'Telefone': '(81) 98888-7777', 'Email': 'ana.silva@email.com'}, 2: {'ID': 2, 'Razão Social': 'Tech Solutions LTDA', 'CNPJ': '12.345.678/0001-90', 'Telefone': '(11) 97777-6666', 'Email': 'contato@techsolutions.com'}, 3: {'ID': 3, 'Nome': 'João Pereira', 'CPF': '987.654.321-00', 'Telefone': '(21) 96666-5555', 'Email': 'joao.pereira@email.com'}, 4: {'ID': 4, 'Razão Social': 'Global Trade ME', 'CNPJ': '98.765.432/0001-11', 'Telefone': '(41) 94444-3333', 'Email': 'contato@globaltrade.com'}, 5: {'ID': 5, 'Nome': 'Maria Oliveira', 'CPF': '456.789.123-00', 'Telefone': '(31) 95555-4444', 'Email': 'maria.oliveira@email.com'}, 6: {'ID': 6, 'Razão Social': 'Construtora Alfa', 'CNPJ': '34.567.890/0001-77', 'Telefone': '(81) 97777-2222', 'Email': 'contato@construtoraalfa.com'}, 7: {'ID': 7, 'Nome': 'Carlos Mendes', 'CPF': '741.852.963-00', 'Telefone': '(51) 93333-2222', 'Email': 'carlos.mendes@email.com'}, 8: {'ID': 8, 'Razão Social': 'Digital Services LTDA', 'CNPJ': '23.456.789/0001-55', 'Telefone': '(61) 92222-1111', 'Email': 'suporte@digitalservices.com'}, 9: {'ID': 9, 'Nome': 'Fernanda Rocha', 'CPF': '852.963.741-00', 'Telefone': '(71) 91111-0000', 'Email': 'fernanda.rocha@email.com'}, 10: {'ID': 10, 'Razão Social': 'Loja Beta', 'CNPJ': '45.678.901/0001-22', 'Telefone': '(85) 98888-3333', 'Email': 'contato@lojabeta.com'}, 11: {'ID': 11, 'Nome': 'PetDoC', 'CPF': '9938119382', 'Telefone': '8199283921', 'Email': 'petris@gmail.com'}}

def gerar_novo_id():
    if banco_dados:
        return max(banco_dados.keys()) + 1
    return 1

mapa_campos = {
    "id": "ID", "nome": "Nome",
    "razao": "Razão Social", "razão": "Razão Social", "razao social": "Razão Social", "razão social": "Razão Social",
    "empresa": "Razão Social",
    "cpf": "CPF", "cnpj": "CNPJ",
    "doc": "CPF", "documento": "CPF",
    "telefone": "Telefone", "tel": "Telefone",
    "email": "Email", "mail": "Email"
}

campos_principais = ["ID", "Nome", "Razão Social", "CPF", "CNPJ", "Telefone", "Email"]

def campos_aceitos():
    return campos_principais

def buscar_registro(filtro, valor):
    resultados = []
    filtro = filtro.lower().strip()
    valor = str(valor).lower().strip()

    if filtro not in mapa_campos:
        return f"Campo '{filtro}' inválido.\nCampos aceitos: " + ", ".join(campos_principais)
    filtro = mapa_campos[filtro]

    for registro in banco_dados.values():
        if filtro == "ID":
            if str(registro.get("ID", "")) == valor:
                resultados.append(registro)
        elif filtro in ["CPF", "CNPJ"]:
            if filtro in registro:
                if not valor:
                    resultados.append(registro)
                elif valor in str(registro[filtro]).lower():
                    resultados.append(registro)
        else:
            if filtro in registro:
                if not valor or valor in str(registro[filtro]).lower():
                    resultados.append(registro)

    return resultados

def formatar_registros(registros):
    if not registros:
        return "Nenhum registro encontrado."
    if isinstance(registros, str):
        return registros

    saida = []
    saida.append("-" * 50)
    for reg in sorted(registros, key=lambda x: x["ID"]):
        for chave, valor in reg.items():
            saida.append(f"{chave}: {valor}")
        saida.append("-" * 50)
    return "\n".join(saida)