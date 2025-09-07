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
    
    with open("bdados.py", "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Converte o texto em estrutura Python para editar
    inicio = conteudo.find("banco_dados = {")
    if inicio == -1:
        return "Erro: banco_dados não encontrado no arquivo bdados.py"

    # Retira apenas o dicionário original
    dicionario_str = conteudo[inicio + len("banco_dados = "):].split("\n\n", 1)[0].strip()

    # Converte o texto para dicionário real
    dados_existentes = ast.literal_eval(dicionario_str)

    # Atualiza os dados
    dados_existentes[novo_id] = registro

    # Substitui o conteúdo do dicionário no arquivo
    novo_conteudo = conteudo.replace(dicionario_str, str(dados_existentes))

    # Salva de volta no bdados.py
    with open("bdados.py", "w", encoding="utf-8") as f:
        f.write(novo_conteudo)

    return f"Registro {novo_id} criado com sucesso!"