from models.usuario_model import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session

    def salvar_usario(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()

    def pesquisar_usuario_por_email(self, email: str):
        # Retorna todos os campos, exceto a senha
        return self.session.query(
            Usuario.id,
            Usuario.nome,
            Usuario.email
        ).filter_by(email=email).first()
    
    def pesquisar_usuario_por_nome_senha(self, nome: str, senha: str):
        return self.session.query(Usuario).filter_by(nome=nome, senha=senha).first()

    def excluir_usuario(self, usuario: Usuario):
        self.session.delete(usuario)
        self.session.commit()

    def excluir_todos_usuarios(self):
        try:
            # Exclui todos os registros na tabela de usuários
            self.session.query(Usuario).delete()
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Erro ao excluir todos os usuários: {e}")

    def listar_usuarios(self):
        return self.session.query(Usuario).all()