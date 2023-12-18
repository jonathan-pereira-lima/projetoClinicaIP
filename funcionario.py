# ======================================================================
# >>>Projeto de I.P
# >>>Professor: Zildomar
# >>>Aluno:Jośe Jonathan Pereira Lima
# >>> 1 período
# ======================================================================

from clinica import *

base_funcionarios = []


def validar_funcionario(cpf=None, matricula=None):
    for f in base_funcionarios:
        if cpf != None and cpf == f["cpf"]:
            return False

        if matricula != None and matricula == f["matricula"]:
            return False

    return True


def novo_funcionario():
    matricula = input("Matricula")
    if not validar_funcionario(matricula=matricula):
        print("Funcionário com mesma matricula encontrado! utilizar outra matricula!!")
        return

    cpf = input("CPF: ")
    if not validar_funcionario(cpf=cpf):
        print("Funcionário com mesmo CPF encontrado! utilizar outro CPF!!")
        return

    nome = input("Nome: ")
    email = input("Email: ")
    cnpj = input("Digite cnpj da Clinica: ")
    if not validar_clinica(cnpj):

        clinica = buscar_clinica_base(cnpj)
        print("Clinica encontrada", clinica['nome'])
    else:
        print('Clinica não encontrada')
        clinica = 'sem vínculo'
        return
    funcionario = {
        "matricula": matricula,
        "cpf": cpf,
        "nome": nome,
        "email": email,
        "clinica": clinica,
    }
    base_funcionarios.append(funcionario)
    print("Funcionario salvo com sucesso!")


def listar_funcionarios():
    print("------------------------------------------------------------------")
    print("Registros encontrados: ", len(base_funcionarios))

    if len(base_funcionarios) > 0:
        print("%20s | %20s | %20s" % ("Nome", "CPF", "Matricula"))
        for i, funcionario in enumerate(base_funcionarios):
            print("%20s | %20s | %20s" % (funcionario["nome"], funcionario["cpf"], funcionario["matricula"]))
    print("------------------------------------------------------------------")


def editar_funcionarios():
    matricula = input('digite a matricula do Funcionario')

    for i, funcionario in enumerate(base_funcionarios):
        if funcionario["matricula"] == matricula:
            print("----------------------FUNCIONÁRIO A SER ATUALIZADO--------------------")
            print("%20s | %20s | %20s" % ("Nome", "CPF", "Matricula"))
            print("%20s | %20s | %20s" % (funcionario["nome"], funcionario["cpf"], funcionario["matricula"]))

            opcao = int(input("deseja modificar a Matricula Funcionario [1-Sim 2-Não]"))
            if opcao == 1:
                matriculamodificada = input('informe nova Matricula:')
                funcionario["matricula"] = matriculamodificada

            opcao = int(input('deseja modificar o CPF do Funcionário? [1-Sim 2-Não]'))
            if opcao == 1:
                cpf = input('informe novo CPF:')
                funcionario["cpf"] = cpf

            opcao = int(input('deseja modificar o Nome do Funcionário? [1-Sim 2-Não]'))
            if opcao == 1:
                nome = input('informe novo Nome:')
                funcionario["nome"] = nome

            opcao = int(input('deseja modificar o E-mail do funcionário? [1-Sim 2-Não]'))
            if opcao == 1:
                email = input('informe novo E-mail:')
                funcionario["email"] = email

            opcao = int(input('deseja modificar a Clinica? [1-Sim 2-Não]'))
            if opcao == 1:
                clinica = input('informe nova Clinica:')
                funcionario["clinica"] = clinica

            base_funcionarios[i] = funcionario
            print("----------------------ATUALIZADO COM SUCESSO--------------------")
            print("%20s | %20s | %20s" % ("Nome", "Matricula", "CPF"))
            print("%20s | %20s | %20s" % (funcionario["nome"], funcionario["matricula"], funcionario["cpf"]))

            input('pressione qualquer tecla para continuar')
            return
    print('FUNCIONÁRIO NÃO ENCONTRADO!!!')


def remover_funcionario():
    matricula = input('digite a Matricula do Funcionário')

    for i, funcionario in enumerate(base_funcionarios):
        if funcionario["matricula"] == matricula:
            print("----------------------FUNCIONÁRIO A SER EXCLUIDO--------------------")
            print("%20s | %20s | %20s" % ("Nome", "Matricula", "CPF"))
            print("%20s | %20s | %20s" % (funcionario["nome"], funcionario["matricula"], funcionario["cpf"]))

            opcao = int(input('deseja apagar o registro do funcionário [1-Sim 2-Não]'))
            if opcao == 1:
                base_funcionarios.pop(i)
                input('Registro removido com sucesso')
                input('pressione qualquer tecla para continuar')
                return
    print('funcionário não encontrado!!!')


def buscar_funcionario():
    matricula = input('Digite a Matricula do Funcionário')

    for i, funcionario in enumerate(base_funcionarios):
        if funcionario["matricula"] == matricula:
            print("========================================================")
            print("-----------FUNCIONÁRIO ENCONTRADO---------")

            print("nome: ", (funcionario["nome"]))
            print("cpf: ", (funcionario["cpf"]))
            print("Matricula: ", (funcionario["matricula"]))
            print("E-mail: ", (funcionario["email"]))
            print("Clínica: ", (funcionario["clinica"]['nome']))
            print("========================================================")


