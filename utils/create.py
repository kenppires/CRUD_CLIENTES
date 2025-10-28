import ast
from bdados import banco_dados, gerar_novo_id

class ClienteBase:
    def __init__(self, id, telefone, email):
        self.id = id
        self.telefone = telefone
        self.email = email

    def to_dict(self):
        #Converte o objeto em um dicionário compatível com o banco_dados.
        raise NotImplementedError("O método to_dict deve ser implementado na subclasse.")

class ClientePF(ClienteBase):
    def __init__(self, id, nome, cpf, telefone, email):
        super().__init__(id, telefone, email)
        self.nome = nome
        self.cpf = cpf

    def to_dict(self):
        return {
            "ID": self.id,
            "Nome": self.nome,
            "CPF": self.cpf,
            "Telefone": self.telefone,
            "Email": self.email
        }

class ClientePJ(ClienteBase):
    def __init__(self, id, razao_social, cnpj, telefone, email):
        super().__init__(id, telefone, email)
        self.razao_social = razao_social
        self.cnpj = cnpj

    def to_dict(self):
        return {
            "ID": self.id,
            "Razão Social": self.razao_social,
            "CNPJ": self.cnpj,
            "Telefone": self.telefone,
            "Email": self.email
        }

def criar_registro(tipo, identificador, telefone, email, nome=None, razao_social=None):
    # Cria um objeto Cliente, converte para dicionário e persiste.
    
    novo_id = gerar_novo_id()
    registro = None 
    
    if tipo.upper() == "PF":
        if not nome:
            return "Erro: Nome é obrigatório para Pessoa Física."
        
        novo_cliente_obj = ClientePF(novo_id, nome, identificador, telefone, email)
        registro = novo_cliente_obj.to_dict()
        

    elif tipo.upper() == "PJ":
        if not razao_social:
            return "Erro: Razão Social é obrigatória para Pessoa Jurídica."
        
        novo_cliente_obj = ClientePJ(novo_id, razao_social, identificador, telefone, email)
        registro = novo_cliente_obj.to_dict()

    else:
        return "Tipo inválido. Use 'PF' ou 'PJ'."
    
    if registro is None:
        return "Erro ao criar registro."
    
    banco_dados[novo_id] = registro
    
    with open("bdados.py", "r", encoding="utf-8") as f:
        conteudo = f.read()

    inicio = conteudo.find("banco_dados = {")
    if inicio == -1:
        return "Erro: banco_dados não encontrado no arquivo bdados.py"

    dicionario_str = conteudo[inicio + len("banco_dados = "):].split("\n\n", 1)[0].strip()

    dados_existentes = ast.literal_eval(dicionario_str)

    dados_existentes[novo_id] = registro

    novo_conteudo = conteudo.replace(dicionario_str, str(dados_existentes))

    with open("bdados.py", "w", encoding="utf-8") as f:
        f.write(novo_conteudo)

    return f"Registro {novo_id} criado com sucesso!"