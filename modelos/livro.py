from modelos.execoes import Execoes
class _Livro():
    #Inicia o livro
    def __init__(self,ISBN:str,titulo:str,autor:str,ano_publicacao:str,disponivel:bool=True):
        try:
            self._ISBN = ISBN
            self._titulo = titulo
            self._autor = autor
            self._disponivel = disponivel
            self._ano_publicacao = ano_publicacao
        except ValueError:
            Execoes.ValueErro()
    
    # Retorna a string da classe livro
    def __str__(self):
        return '{},{},{},{},{}'.format(self.get_ISBN,self.get_titulo,self.get_autor,self.get_ano_publicacao,self.get_disponivel)
    
    @property
    def get_autor(self):
        return self._autor
    
    @property
    def get_titulo(self):
        return self._titulo
    
    @property
    def get_disponivel(self):
        return self._disponivel
    
    @property
    def get_ano_publicacao(self):
        return self._ano_publicacao
    
    @property
    def get_ISBN(self):
        return self._ISBN

    def set_disponivel(self,valor:bool):
        try:
            self._disponivel = valor
        except ValueError:
            Execoes.ValueErro()