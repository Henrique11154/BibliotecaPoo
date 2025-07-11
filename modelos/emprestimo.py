import json
from datetime import date
from modelos.livro import _Livro 
from modelos.execoes import Execoes

class Emprestimo:
    ''' Representa o empréstimo de livros '''
    def __init__(self,nome_leitor:str,ISBN:str,dias:str):
        self.__nome_leitor = nome_leitor
        self.__codigo = ISBN
        self.__data_emprestimo = date.today().strftime('%d/%m/%Y')
        self.__prazo = dias
        self.__devolvido = False


    def emprestar(self, livro:_Livro):
        if livro.get_disponivel:
            print('Empréstimo realizado com sucesso!')
            print('{} pegou o livro em {}, e deve delvolver em: {} dias'.format(self.get_nome,self.get_data,self.get_dias))
            livro.set_disponivel(False)
        else:
            print('Livro indisponível.')

    def foi_devolvido(self):
        return self.__devolvido

    def exibir_dados(self):
        status = 'Devolvido' if self.__devolvido else 'Pendente'
        return f'Leitor: {self.get_nome}, Livro: {self.get_codigo}, Data: {self.__data_emprestimo}, Prazo: {self.get_dias} dias, Status: {status}'

    def to_dict(self):
        return {
            'nome_leitor': self.__nome_leitor,
            'ISBN': self.__codigo,
            'data_emprestimo': self.__data_emprestimo,
            'prazo': self.__prazo,
            'devolvido': self.__devolvido
        }
    
    @property
    def get_data(self):
        return self.__data_emprestimo
    @property
    def get_devolvido(self):
        return self.__devolvido
    @property
    def get_nome(self):
        return self.__nome_leitor
    @property
    def get_codigo(self):
        return self.__codigo
    @property
    def get_dias(self):
        return self.__prazo
    
def salvar_emprestimos(lista_emprestimos, caminho_arquivo):
    dados = [i.to_dict() for i in lista_emprestimos]
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        Execoes.FileDontFound()
    except Exception:
        Execoes()

def carregar_emprestimos(caminho_arquivo):
    emprestimos = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            lista = json.load(f)
            for item in lista:
                i = Emprestimo(item['nome_leitor'], item['ISBN'], item['prazo'])
                i.__data_emprestimo = item['data_emprestimo']
                if item['devolvido']:
                    i.__devolvido = True
                emprestimos.append(i)
    except FileNotFoundError:
        Execoes.FileDontFound()
    return emprestimos

# Teste
if __name__ == '__main__':

    l1 = _Livro('Python Básico', 'Machado De Assis', 'LIV001', 2020)
    l2 = _Livro('POO com Python', 'Gustavo Guanabara', 'LIV002', 2022)

    e1 = Emprestimo('Eduardo', 'LIV001', 7)
    e2 = Emprestimo('Henrique', 'LIV002', 10)

    e1.emprestar(l1)
    e2.emprestar(l2)

    salvar_emprestimos([e1, e2], 'TrabalhoFinal/modelos/emprestimos.json')
    print('Empréstimos salvos.')

    lista = carregar_emprestimos('TrabalhoFinal/modelos/emprestimos.json')
    for i in lista:
        print(i.exibir_dados())

