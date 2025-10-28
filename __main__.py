from utils.create import criar_registro
from utils.update import atualizar_registro
from utils.read import ler_registro
from utils.delete import deletar_registro
from bdados import formatar_registros, campos_aceitos, mapa_campos

campos_pf = ["Nome", "CPF", "Telefone", "Email"]
campos_pj = ["Razão Social", "CNPJ", "Telefone", "Email"]

def mostrar_campos():
    print("\nCampos aceitos: " + ", ".join(campos_aceitos()))

def menu():
    while True:
        print("\n=== GERENCIAMENTO DE CLIENTES ===")
        print("1 - Cadastrar Cliente")
        print("2 - Buscar Cliente(s)")
        print("3 - Atualizar Cliente")
        print("4 - Deletar Cliente")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            tipo = input("Digite o tipo (PF / PJ): ").strip().upper()
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
            mostrar_campos()
            filtro = input("\nCampo para busca ou Enter para listar todos: ").strip()
            if filtro:
                if filtro.lower() not in map(lambda x: x.lower(), campos_aceitos()):
                    print(f"Campo '{filtro}' inválido.\nCampos aceitos: " + ", ".join(campos_aceitos()))
                    continue
                valor = input("Digite o valor (busca parcial aceita[exceto ID]) ou Enter para listar apenas registros com este campo: ").strip()
                resultados = ler_registro(filtro, valor)
                print(formatar_registros(resultados))
            else:
                print(formatar_registros(ler_registro()))

        elif opcao == "3":
            mostrar_campos()
            filtro = input("\nCampo para localizar: ").strip()
            if filtro.lower() not in map(lambda x: x.lower(), campos_aceitos()):
                print(f"Campo '{filtro}' inválido.\nCampos aceitos: " + ", ".join(campos_aceitos()))
                continue
            valor = input("Valor para busca: ").strip()

            mostrar_campos()
            campo = input("\nQual campo deseja atualizar? ").strip()
            if campo.lower() not in map(lambda x: x.lower(), campos_aceitos()):
                print(f"Campo '{campo}' inválido.\nCampos aceitos: " + ", ".join(campos_aceitos()))
                continue
            novo_valor = input("Novo valor: ").strip()

            registros = ler_registro(filtro, valor)
            if not registros or isinstance(registros, str):
                print(registros if isinstance(registros, str) else "Nenhum registro encontrado.")
                continue

            tipo_cliente = "PF" if "CPF" in registros[0] else "PJ"
            chave = mapa_campos.get(campo.lower())
            if (tipo_cliente == "PF" and chave not in campos_pf) or (tipo_cliente == "PJ" and chave not in campos_pj):
                permitidos = ", ".join(campos_pf) if tipo_cliente == "PF" else ", ".join(campos_pj)
                print(f"Campo '{chave}' não pode ser atualizado para este tipo de cliente.\nPermitidos: {permitidos}")
                continue

            print(atualizar_registro(filtro, valor, **{campo: novo_valor}))

        elif opcao == "4":
            mostrar_campos()
            filtro = input("\nCampo para localizar: ").strip()
            if filtro.lower() not in map(lambda x: x.lower(), campos_aceitos()):
                print(f"Campo '{filtro}' inválido.\nCampos aceitos: " + ", ".join(campos_aceitos()))
                continue
            valor = input("Valor para busca: ").strip()
            print(deletar_registro(filtro, valor))

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()