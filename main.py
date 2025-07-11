from modelos.biblioteca import Biblioteca, Execoes, _Livro
from modelos.pessoa1 import Leitor, Funcionario,salvar_usuarios,carregar_funcionario,carregar_leitores
from modelos.emprestimo import Emprestimo, salvar_emprestimos, carregar_emprestimos
import time

# Carregar dados
biblioteca = Biblioteca()
biblioteca.carregar_biblioteca('dados/dados_blibioteca.json')
try:
    leitores = carregar_leitores('dados/leitores.json')
except Exception:
    Execoes()
try:
    funcionarios = carregar_funcionario('dados/funcionarios.json')
except Exception:
    Execoes()
try:
    emprestimos = carregar_emprestimos('dados/emprestimos.json')
except Exception:
    Execoes()
print('Bem-vindo a Biblioteca virtual')

while True:
    print('\nMenu:')
    print('1 - Cadastrar Livro')
    print('2 - Cadastrar Usuário')
    print('3 - Fazer Empréstimo')
    print('4 - Listar Livros')
    print('5 - Listar Empréstimos')
    print('6 - Sair')
    escolha = input('Escolha: ')
    if escolha == '1':
        try:
            isbn = input('ISBN: ')
            titulo = input('Título: ')
            autor = input('Autor: ')
            ano = input('Ano: ')
            livro = _Livro(isbn, titulo, autor, ano)
            biblioteca.cadastrar_Livro(livro)
            print('Livro cadastrado.')
        except ValueError:
            Execoes.ValueErro()

    elif escolha == '2':
        nome = input('Nome: ')
        cpf = input('CPF: ')
        tipo = input('Tipo (leitor/funcionario): ').lower()

        if tipo == 'leitor':
            leitores.append(Leitor(nome, cpf))
            salvar_usuarios(leitores, 'dados/leitores.json')
        elif tipo == 'funcionario':
           funcionarios.append(Funcionario(nome, cpf))
           salvar_usuarios(funcionarios, 'dados/funcionarios.json')
        else:
            print('Tipo inválido.')
            continue
        print("Usuário cadastrado.")

    elif escolha == '3':
        nome = input('Nome do leitor: ')
        isbn = input('ISBN do livro: ')
        dias = input('Prazo: ')

        if len(funcionarios) ==0:
            Execoes.funcionario_nao_encontrado()
        else:
            for i in biblioteca.get_livro:
                for j in leitores:
                    if i.get_ISBN == isbn and j.get_nome() == nome:
                        emprestimo = Emprestimo(nome,isbn,dias)
                        emprestimo.emprestar(i)
                        emprestimos.append(emprestimo)
                        salvar_emprestimos(emprestimos, 'dados/emprestimos.json')
                        print('Empréstimo registrado.')
                    else:
                        Execoes.livro_nao_encontrado()
                        print('ou ',end='')
                        Execoes.leitor_nao_encontrado()
    elif escolha == '4':
        biblioteca.exibir_livros()
    elif escolha == '5':
        for u in emprestimos:
            print(u.exibir_dados())
    elif escolha == '6':
        print('Encerrado ')
        break
    else:
        print('Opção inválida.')
    time.sleep(0.87)
