from bdados import banco_dados, gerar_novo_id

def criar_registro(tipo, identificador, telefone, email, nome=None, razao_social=None):
    novo_id = gerar_novo_id()
    if tipo.upper() == "PF":
        if not nome:
            return "Erro: Nome é obrigatório para Pessoa Física."
        
        registro = {
            "ID": novo_id,
            "Nome": nome,
            "CPF": identificador,
            "Telefone": telefone,
            "Email": email
        }

    elif tipo.upper() == "PJ":
        if not razao_social:
            return "Erro: Razão Social é obrigatória para Pessoa Jurídica."
        
        registro = {
            "ID": novo_id,
            "Razão Social": razao_social,
            "CNPJ": identificador,
            "Telefone": telefone,
            "Email": email
        }

    else:
        return "Tipo inválido. Use 'PF' ou 'PJ'."
    
    banco_dados[novo_id] = registro
