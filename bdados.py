# Banco de dados inicial com 10 cadastros (PF e PJ)
banco_dados = {
    1: {
        "ID": 1,
        "Nome": "Ana Silva",
        "CPF": "123.456.789-00",
        "Telefone": "(81) 98888-7777",
        "Email": "ana.silva@email.com"
    },
    2: {
        "ID": 2,
        "Razão_Social": "Tech Solutions LTDA",
        "CNPJ": "12.345.678/0001-90",
        "Telefone": "(11) 97777-6666",
        "Email": "contato@techsolutions.com"
    },
    3: {
        "ID": 3,
        "Nome": "João Pereira",
        "CPF": "987.654.321-00",
        "Telefone": "(21) 96666-5555",
        "Email": "joao.pereira@email.com"
    },
    4: {
        "ID": 4,
        "Razão_Social": "Global Trade ME",
        "CNPJ": "98.765.432/0001-11",
        "Telefone": "(41) 94444-3333",
        "Email": "contato@globaltrade.com"
    },
    5: {
        "ID": 5,
        "Nome": "Maria Oliveira",
        "CPF": "456.789.123-00",
        "Telefone": "(31) 95555-4444",
        "Email": "maria.oliveira@email.com"
    },
    6: {
        "ID": 6,
        "Razão_Social": "Construtora Alfa",
        "CNPJ": "34.567.890/0001-77",
        "Telefone": "(81) 97777-2222",
        "Email": "contato@construtoraalfa.com"
    },
    7: {
        "ID": 7,
        "Nome": "Carlos Mendes",
        "CPF": "741.852.963-00",
        "Telefone": "(51) 93333-2222",
        "Email": "carlos.mendes@email.com"
    },
    8: {
        "ID": 8,
        "Razão_Social": "Digital Services LTDA",
        "CNPJ": "23.456.789/0001-55",
        "Telefone": "(61) 92222-1111",
        "Email": "suporte@digitalservices.com"
    },
    9: {
        "ID": 9,
        "Nome": "Fernanda Rocha",
        "CPF": "852.963.741-00",
        "Telefone": "(71) 91111-0000",
        "Email": "fernanda.rocha@email.com"
    },
    10: {
        "ID": 10,
        "Razão_Social": "Loja Beta",
        "CNPJ": "45.678.901/0001-22",
        "Telefone": "(85) 98888-3333",
        "Email": "contato@lojabeta.com"
    }
}


def gerar_novo_id():
    if banco_dados:
        return max(banco_dados.keys()) + 1
    return 1


# 🔎 Mapeamento de sinônimos para campos
mapa_campos = {
    "id": "ID",
    "nome": "Nome",
    "razao": "Razão_Social",
    "razao_social": "Razão_Social",
    "empresa": "Razão_Social",
    "cpf": "CPF",
    "cnpj": "CNPJ",
    "doc": "CPF",   # genérico
    "documento": "CPF",
    "telefone": "Telefone",
    "tel": "Telefone",
    "email": "Email",
    "mail": "Email"
}


# 🔎 Busca flexível (case-insensitive, aceita sinônimos, busca parcial)
def buscar_registro(filtro, valor):
    resultados = []
    filtro = filtro.lower().strip()
    valor = str(valor).lower().strip()

    if filtro in mapa_campos:
        filtro = mapa_campos[filtro]

    for registro in banco_dados.values():
        for chave, conteudo in registro.items():
            if chave.lower() == filtro.lower():
                if valor in str(conteudo).lower():
                    resultados.append(registro)

        # Se filtro genérico "doc" → tenta CPF ou CNPJ
        if filtro == "CPF" and "CPF" in registro:
            if valor in str(registro["CPF"]).lower():
                resultados.append(registro)
        elif filtro == "CPF" and "CNPJ" in registro:
            if valor in str(registro["CNPJ"]).lower():
                resultados.append(registro)

    return resultados