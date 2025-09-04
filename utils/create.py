def add_cliente(bdados):
    nome_cliente = input("informe o nome do cliente: ")

    novo_id = bdados[-1][id]+1 #verificar

    novo_cliente = {
        {"id":len(bdados)+1,
         "nome": nome_cliente}
    }

    bdados.append(novo_cliente)