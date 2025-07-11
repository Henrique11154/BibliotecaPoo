from modelos.execoes import Execoes
from json import dumps,loads
from modelos.livro import _Livro

class Biblioteca():
    def __init__(self):
        self.__livro = []     #Inicia a Blibioteca
        
    '''CADASTRO DO LIVRO'''
    def cadastrar_Livro(self,livro:_Livro):
        for i in self.__livro:
            if livro.__str__() == i.__str__():
                print("Este livro ja existe")
                return None
        self.__livro.append(livro)
        self.salvar_dados()

    '''Transforma em dicionario pra salvar em Json'''
    def to_dict(self):
        dicio = {}
        for i in range(len(self.__livro)):
            livro = self.__livro[i]
            dicio[f'ISBN livro {i+1}:'] = livro.get_ISBN
            dicio[f'titulo livro {i+1}:'] = livro.get_titulo
            dicio[f'ano_publicacao livro {i+1}:'] = livro.get_ano_publicacao
            dicio[f'autor livro {i+1}:'] = livro.get_autor
            dicio[f'disponivel livro {i+1}:'] = str(livro.get_disponivel)
        return dicio
            
    def salvar_dados(self):
        try:
            with open('dados/dados_blibioteca.json','w',encoding='utf-8') as arquivo:
                arquivo.write(dumps(self.to_dict()))
        except FileNotFoundError:
            Execoes.FileDontFound()
        except Exception:
            Execoes()

    # Ja inicia a biblioteca
    def carregar_biblioteca(self,arquivo):
        try:
            with open(arquivo,'r',encoding='utf-8') as arq:
                leitura = loads(arq.read())
                for i in range(len(leitura)//5):
                    self.cadastrar_Livro(_Livro(leitura[f'ISBN livro {i+1}:'],leitura[f'titulo livro {i+1}:'],leitura[f'ano_publicacao livro {i+1}:'],leitura[f'disponivel livro {i+1}:']))
        except FileNotFoundError:
            Execoes.FileDontFound()
        except Exception:
            Execoes()

    
    def exibir_livros(self):
        livros = self.to_dict()
        for k,i in livros.items():
            print(k+" "+i)
            print("")
    
    @property
    def get_livro(self):
        return self.__livro