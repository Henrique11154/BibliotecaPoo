class Execoes(Exception):
    def __init__(self):
        print('Ocorreu um erro')

    '''Caso o arquivo não seja encontrado'''
    def FileDontFound():
        print("Arquivo Não encontrado")

    def ValueErro():
        print('Não é possivel cadastrar este valor')
    
    def leitor_nao_encontrado():
        print('o leitor não foi encontrado')
    
    def livro_nao_encontrado():
        print('livro não encontrado')

    def funcionario_nao_encontrado():
        print("funcionario não encontrado")