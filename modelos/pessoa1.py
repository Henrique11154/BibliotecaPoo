import json
from abc import ABC, abstractmethod
from typing import overload
from modelos.execoes import Execoes

class Pessoa(ABC):
    ''' Classe base que representa uma pessoa '''
    def __init__(self, nome:str, cpf:str):
        self.__nome = nome
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome:str):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self.__nome = novo_nome.strip()

    def get_cpf(self):
        return self.__cpf

    @abstractmethod
    def exibir_dados(self):
        pass

    def to_dict(self):
        return {
            'nome': self.__nome,
            'cpf': self.__cpf,
            'tipo': self.__class__.__name__
        }

class Leitor(Pessoa):
    ''' Classe que representa os dados do leitor '''
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
    def exibir_dados(self):
        return f'Leitor: {self.get_nome()}, CPF: {self.get_cpf()}'
    def get_cpf(self):
        return super().get_cpf()
    def get_nome(self):
        return super().get_nome()

class Funcionario(Pessoa):
    ''' Classe que representa os dados do funcionario '''
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
    
    def exibir_dados(self):
        return f'Funcionário: {self.get_nome()}, CPF: {self.get_cpf()}'
    def get_nome(self):
        return super().get_nome()
    def get_cpf(self):
        return super().get_cpf()

def salvar_usuarios(usuarios:list, arquivo_json):
    dados = []
    for i in usuarios:
        dados.append(i.to_dict())
    try:
        with open(arquivo_json, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        Execoes.FileDontFound()
    except Exception:
        Execoes()

def carregar_leitores(arquivo_json):
    leitores = []
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as f:
            lista = json.load(f)
            for item in lista:
                nome = item.get('nome')
                cpf = item.get('cpf')
                leitores.append(Leitor(nome,cpf))
    except FileNotFoundError:
        Execoes.FileDontFound()
    return leitores

def carregar_funcionario(arquivo_json):
    funcionarios = []
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as f:
            lista = json.load(f)
            for item in lista:
                nome = item.get('nome')
                cpf = item.get('cpf')
                funcionarios.append(Funcionario(nome,cpf))
    except FileNotFoundError:
        Execoes.FileDontFound()
    return funcionarios

if __name__ == '__main__':
     Funcionario.salvar_usuarios([
        Leitor('Eduardo', '12345678901'),
        Funcionario('Cassiano', '10987654321')
     ], 'TrabalhoFinal/modelos/usuarios.json')

     for i in carregar_usuarios('TrabalhoFinal/modelos/usuarios.json'):
        print(i.exibir_dados())
