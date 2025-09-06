from utils.create import criar_registro
from utils.read import ler_registro
from utils.update import atualizar_registro
from utils.delete import deletar_registro

def menu():
    while True:
        print("\n=== GERENCIAMENTO DE CLIENTES ===")
        print("1 - Registrar Cliente")
        print("2 - Buscar Cliente(s)")
        print("3 - Atualizar Cliente")
        print("4 - Deletar Cliente")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tipo = input("Digite o tipo (PF para Pessoa Física / PJ para Pessoa Jurídica): ").strip().upper()
            
            if tipo == "PF":
                nome = input("Nome: ")
                cpf = input("CPF: ")
                telefone = input("Telefone: ")
                email = input("Email: ")
                print(criar_registro("PF", cpf, telefone, email, nome=nome))

            elif tipo == "PJ":
                razao_social = input("Razão Social: ")
                cnpj = input("CNPJ: ")
                telefone = input("Telefone: ")
                email = input("Email: ")
                print(criar_registro("PJ", cnpj, telefone, email, razao_social=razao_social))

            else:
                print("Tipo inválido, escolha PF ou PJ.")

        elif opcao == "2":
            filtro = input("Digite o campo para busca (ID / Nome / Razão_Social / CPF / CNPJ / Telefone / Email) ou Enter para listar todos: ")
            if filtro:
                valor = input("Digite o valor (busca parcial aceita): ")
                resultados = ler_registro(filtro, valor)
                if resultados:
                    for r in resultados:
                        print(r)
                else:
                    print("Nenhum registro encontrado.")
            else:
                for r in ler_registro():
                    print(r)

        elif opcao == "3":
            filtro = input("Campo para localizar (ID / Nome / Razão_Social / CPF / CNPJ / Telefone / Email): ")
            valor = input("Valor para busca (parcial aceito): ")
            campo = input("Qual campo deseja atualizar? ")
            novo_valor = input("Novo valor: ")
            print(atualizar_registro(filtro, valor, **{campo: novo_valor}))

        elif opcao == "4":
            filtro = input("Campo para localizar (ID / Nome / Razão_Social / CPF / CNPJ / Telefone / Email): ")
            valor = input("Valor para busca (parcial aceito): ")
            print(deletar_registro(filtro, valor))

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()