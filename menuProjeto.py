#======================================================================
#>>>Projeto de I.P
#>>>Professor: Zildomar
#>>>Aluno:Jośe Jonathan Pereira Lima
#>>> 1 período
#======================================================================



def menu_paciente():
    print("-----------MENU PACIENTE---------")
    print("1 - Cadastrar Paciente")
    print("2 - Buscar Paciente por cpf")
    print("3 - Editar Paciente")
    print("4 - Remover Paciente")
    print("5 - Listar Todos os Pacientes")
    print("6 – SAIR")

def menu_consulta():
    print("------------MENU MARCAÇÃO DE CONSULTAS---------")
    print("1 - Marcar Consulta")
    print("2 - Buscar Consulta por Paciente")
    print("3 - Editar Consulta")
    print("4 - Remover Consulta")
    print("5 - Listar Consultas")
    print("6 - Listar Consultas por Retorno")
    print('7 - Listar Consultas por intervalo de datas')
    print("8 – SAIR")

def menu_medico():
    print("-----------MENU MÉDICO---------")
    print("1 - Cadastrar Médico")
    print("2 - Buscar Médico por CRM")
    print("3 - Editar Médico")
    print("4 - Remover Médico")
    print("5 - Listar Todos os médicos")
    print("6 - Listar Médico por Especialidade")
    print("7 – SAIR")


def menu_funcionario():
    print("-----------MENU FUNCIONÁRIO---------")
    print("1 - Cadastrar Funcionário")
    print("2 - Buscar Funcionário por Matrícula")
    print("3 - Editar Funcionário")
    print("4 - Remover Funcionário")
    print("5 - Listar Todos os Funcionários")
    print("6 – SAIR")

def menu_clinica():
    print("-----------MENU CLÍNICA---------")
    print("1 - Cadastrar Clínica")
    print("2 - Buscar Clínica por CNPJ")
    print("3 - Editar Clínica")
    print("4 - Remover Clínica")
    print("5 - Listar Todas as Clínicas")
    print("6 – SAIR")


def menuPrincipal():
    print('\n')
    print('-----------MENU---------')
    print('1 - Menu de Paciente')
    print('2 - Menu de Marcação de Consulta')
    print('3 - Menu de Médico')
    print('4 - Menu de Funcionário')
    print('5- Menu de Clínica')
    print('6 – SAIR')
    opcao = int(input('Digite opção: >>>'))
    #print('\n')
    return opcao