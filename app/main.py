from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    while True:  # Loop infinito para mostrar o menu repetidamente

        print(
            f"--- MENU SENAI ---\n"
            f"Código | Descrição\n"
            f"  1    | Cadastrar um novo usuário\n"
            f"  2    | Pesquisar um usuário\n"
            f"  3    | Atualizar dados de um usuário\n"
            f"  4    | Excluir um usuário\n"
            f"  5    | Excluir todos os usuários cadastrados\n"
            f"  0    | Sair\n"
        )

        codigo = input("Digite o código que deseja: ")

        if codigo == "1":
            os.system("cls || clear")

            # Lógica para cadastrar usuário
            print("\nAdicionando usuário: ")
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            senha = input("Digite a senha do usuário: ")

            service.criar_usuario(nome=nome, email=email, senha=senha)

        elif codigo == "2":
            os.system("cls || clear")

            # Lógica para pesquisar usuário
            print("Pesquisando usuário por e-mail:")
            email = input("Digite o e-mail do usuário que deseja buscar: ")

            usuario = repository.pesquisar_usuario_por_email(email=email)

            if usuario:
                print(f"\n--- Dados do Usuário ---")
                print(f"ID: {usuario.id}")
                print(f"Nome: {usuario.nome}")
                print(f"E-mail: {usuario.email}\n")
            else:
                print("\nUsuário não encontrado!")

        elif codigo == "3":
            os.system("cls || clear")

            # Lógica para atualizar dados do usuário
            print("Atualizando Dados de um usuário")
            nome = input("Digite o nome do usuário: ")
            senha = input("Digite a senha do usuário: ")

            usuario = repository.pesquisar_usuario_por_nome_senha(nome=nome, senha=senha)

            if usuario:
                print(f"\n--- Dados do Usuário ---")
                print(f"ID: {usuario.id}")
                print(f"Nome: {usuario.nome}")
                print(f"E-mail: {usuario.email}")
                print(f"Senha: {usuario.senha}\n")

                print(
                    f"\n--- O Que Deseja Alterar ---\n"
                    f"1 | Nome\n"
                    f"2 | E-mail\n"
                    f"3 | Senha\n"
                    f"0 | Sair\n"
                )

                escolha = input("Digite o código da alteração que deseja fazer: ")

                if escolha == "1":
                    novo_nome = input("Digite o novo nome: ")
                    usuario.nome = novo_nome
                    print(f"\nNome atualizado com sucesso para: {usuario.nome}")

                elif escolha == "2":
                    novo_email = input("Digite o novo e-mail: ")
                    usuario.email = novo_email
                    print(f"\nE-mail atualizado com sucesso para: {usuario.email}")

                elif escolha == "3":
                    nova_senha = input("Digite a nova senha: ")
                    usuario.senha = nova_senha
                    print("\nSenha atualizada com sucesso!")

                elif escolha == "0":
                    print("\nOperação cancelada. Nenhuma alteração foi feita.")

                else:
                    print("\nCódigo inválido! Nenhuma alteração foi feita.")
                
                # Salva as alterações no banco de dados
                repository.salvar_usario(usuario)

            else:
                print("\nUsuário não encontrado ou senha incorreta!")

        elif codigo == "4":
            os.system("cls || clear")

            # Lógica para excluir um usuário
            print("\nExcluindo um Usuário")
            nome = input("Digite o nome do usuário que deseja excluir: ")
            senha = input("Digite a senha do usuário: ")

            usuario = repository.pesquisar_usuario_por_nome_senha(nome=nome, senha=senha)

            if usuario:
                print(f"\n--- Dados do Usuário ---")
                print(f"ID: {usuario.id}")
                print(f"Nome: {usuario.nome}")
                print(f"E-mail: {usuario.email}")
                print(f"Senha: {usuario.senha}\n")

                confirmacao = input("Tem certeza que deseja excluir este usuário? (S/N): ").strip().upper()

                if confirmacao == "S":
                    repository.excluir_usuario(usuario=usuario)
                    print("\nUsuário excluído com sucesso!")
                else:
                    print("\nOperação cancelada. Nenhum usuário foi excluído.")
            else:
                print("\nUsuário não encontrado ou senha incorreta!")

        elif codigo == "5":
            os.system("cls || clear")

            # Lógica para excluir todos os usuários
            print("\nRemover todos os usuários cadastrados:")
            confirmacao = input("Tem certeza que deseja remover TODOS os usuários? (S/N): ").strip().upper()

            if confirmacao == "S":
                service.excluir_todos_usuarios()
            else:
                print("Operação cancelada. Nenhum usuário foi removido.")

        elif codigo == "0":
            os.system("cls || clear")

            # Lógica para sair do sistema
            print("\nSaindo do sistema...")
            break

        else:
            print("\nCódigo inválido! Tente novamente...\n")
            continue  # Retorna ao início do loop (menu)

if __name__ == "__main__":
    os.system("cls || clear")
    main()