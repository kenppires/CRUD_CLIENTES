from bdados import clientes

def busca(bdados):
    chave_busca = input("Buscar cliente por qual filtro?:\n" \
                    "1 - ID"\
                    "2 - Nome/Razão Social"\
                    "3 - CPF/CNPJ"\
                    "4 - Telefone"\
                    "5 - Email"
                    "0 - Voltar")
match chave_busca:
    case "1":
        nome_busca = input("Informe a ID do Cliente: ")
        for nome in clientes:
            if nome["nome"] == nome_busca:
                print(nome)

    case "2":
        nome_busca = input("Informe o Nome ou Razão Social do Cliente: ")
        for nome in clientes:
            if nome["nome"] == nome_busca:
                print(nome)