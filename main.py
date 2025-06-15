
from abc import ABC, abstractmethod
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log_biblioteca.txt'

class LogFileMixin:
    def log(self,msg):
        msg_formatada = f'{msg}'
        with open(LOG_FILE, 'a') as arquivo:
            print('Salvando no log...')
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class OperacoesBiblioteca(ABC):

    @abstractmethod
    def pegar_livro(self, livro):
        pass

    @abstractmethod
    def devolver_livro(self, livro):
        pass

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self._status = True

    @property
    def disponivel(self):
        return self._status
    
    @disponivel.setter
    def disponivel(self,valor: bool):
        self._status = valor

class Usuario(OperacoesBiblioteca,LogFileMixin):
    def __init__(self,nome):
        self.nome = nome
        self._livros_emprestados = []

    def pegar_livro(self,livro):
        if livro.disponivel:
            self._livros_emprestados.append(livro)
            livro.disponivel = False
            self.log(f'{self.nome} pegou o livro {livro.titulo}')
        else:
            self.log(f'O livro {livro.titulo} nao esta disponivel para pegar emprestado')

    def devolver_livro(self, livro):
        if livro in self._livros_emprestados:
            self._livros_emprestados.remove(livro)
            livro.disponivel = True
            self.log(f'{self.nome} devolveu o livro {livro.titulo}')
        else:
            self.log(f'{livro.titulo} ainda nao está em sua lista de emprestados.')


class Funcionario(LogFileMixin):
    def __init__(self, nome, id_funcionario):
        self.nome = nome
        self.id_funcionario = id_funcionario
        self._livros_cadastrados = []

    def cadastrar_livro(self,titulo,autor,ano):
        novolivro = Livro(titulo,autor,ano)
        self._livros_cadastrados.append(novolivro)
        self.log(f'Funcionario {self.nome}, adicionou o livro {titulo}')
        return novolivro
    
    def remover_livro(self,titulo,autor,ano):
        for livro in self._livros_cadastrados:
            if livro.titulo == titulo:
                self._livros_cadastrados.remove(livro)
            print(f'Funcionário {self.nome} removeu o livro {titulo}')
            return
        print(f'Livro {titulo} não encontrado para remoção.')


if __name__ == '__main__':
    func = Funcionario('Joao','1234')
    livro1 = func.cadastrar_livro('Princesa e o sapo','Emanuel',2025)    

    usuario = Usuario('Ana')
    usuario.pegar_livro(livro1)
    usuario.devolver_livro(livro1)




    


