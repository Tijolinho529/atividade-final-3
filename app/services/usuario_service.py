from models.usuario_model import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            cadastrado = self.repository.pesquisar_usuario_por_email(email=usuario.email)

            if cadastrado:
                print("Usuário já cadastrado!")
                return

            self.repository.salvar_usario(usuario=usuario)
            print("Usuário cadastrado com sucesso!")
        except TypeError as erro:
            print("Erro ao salvar o usuário: {erro}")
        except Exception as erro: 
            print("Ocorreu um erro inesperado: {erro}")

    def mostrar_usuario_por_email(self, email: str):
        usuario = self.repository.pesquisar_usuario_por_email(email)

        if usuario:
            print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")
        else:
            print("Usuário não encontrado!")

    def excluir_todos_usuarios(self):
        try:
            self.repository.excluir_todos_usuarios()
            print("Todos os usuários foram removidos com sucesso!")
        except Exception as erro:
            print(f"Ocorreu um erro ao remover os usuários: {erro}")


    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()