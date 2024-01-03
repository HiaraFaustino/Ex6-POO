class TitulacaoInvalida(Exception):
    pass

class ProfessorIdadeInvalida(Exception):
    pass

class CursoInvalido(Exception):
    pass

class AlunoIdadeInvalida(Exception):
    pass

class CPFDuplicado(Exception):
    pass

class Pessoa():
    def __init__(self, nome, endereco, idade, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf = cpf
        
    @property
    def nome(self):
      return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def cpf(self):
        return self.__cpf
    
    def printDescricao(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
    
class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, titulacao):
        super().__init__(nome, endereco, idade, cpf)
        self.__titulacao = titulacao

    @property
    def titulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        super().printDescricao()
        print(f"Titulação: {self.titulacao}")
    
class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, curso):
        super().__init__(nome, endereco, idade, cpf)
        self.__curso = curso

    @property
    def curso(self):
        return self.__curso
    
    def printDescricao(self):
        super().printDescricao()
        print(f"Curso: {self.curso}")
    
if __name__ == "__main__":
    prof1 = Professor("Paulo", "Rua das Palmeiras, 221", 45, 12345678912, "Doutor")
    prof2 = Professor("Marcos", "Rua das Flores, 67", 29, 67854323400, "Doutor")
    prof3 = Professor("Maria", "Rua das Margaridas, 101", 37, 12345678912, "Doutor")
    prof4 = Professor("Fábio", "Rua Mário Braz, 451", 48, 47851263987, "Mestre")

    aluno1 = Aluno("Marcelo", "Rua Pedro Sancho, 45", 22, 14587963287, "SIN")
    aluno2 = Aluno("Melina", "Rua João Vilela, 98", 17, 25896415732, "CCO")
    aluno3 = Aluno("Sara", "Rua Osório Machado, 32", 21, 78954863211, "ECO")
    aluno4 = Aluno("Carla", "Rua da Pedra, 11", 25, 25896415732, "SIN")

    ListaPessoas = [prof1, prof2, prof3, prof4, aluno1, aluno2, aluno3, aluno4]

cadastro = {}

pessoasValidas = []

for pessoa in ListaPessoas:
    try:
        cpf = pessoa.cpf
        if cpf in cadastro:
            raise CPFDuplicado("CPF %s já existe!" % cpf)
        cadastro[cpf] = pessoa
        
        if isinstance(pessoa, Professor):
            if pessoa.titulacao != "Doutor":
                raise TitulacaoInvalida("Titulação %s não aceita!" % pessoa.titulacao)
            if pessoa.idade < 30:
                raise ProfessorIdadeInvalida("Idade do professor inválida: %d!" % pessoa.idade)
        elif isinstance(pessoa, Aluno):
            if pessoa.curso != 'SIN' and pessoa.curso != 'CCO':
                raise CursoInvalido("Curso inválido: %s!" % pessoa.curso)
            if pessoa.idade < 18:
                raise AlunoIdadeInvalida("Idade do aluno inválida: %s!" % pessoa.idade)
            
        pessoasValidas.append(pessoa)

    except TitulacaoInvalida as e:
        print(e)
    except ProfessorIdadeInvalida as e:
        print(e)
    except CursoInvalido as e:
        print(e)
    except AlunoIdadeInvalida as e:
        print(e)
    except CPFDuplicado as e:
        print(e)

print()
for pessoa in pessoasValidas:
    pessoa.printDescricao()
    print('-----------------')
        
