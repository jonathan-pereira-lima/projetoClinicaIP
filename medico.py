#======================================================================
#>>>Projeto de I.P
#>>>Professor: Zildomar
#>>>Aluno:Jośe Jonathan Pereira Lima
#>>> 1 período
#======================================================================
from clinica import *

base_medico = []

def validar_medico(crm=None):
    for f in base_medico:
        if crm != None and crm == f["crm"]:
            return False

    return True

def buscar_medico_base (crm=None):
    for f in base_medico:
        if crm != None and crm == f["crm"]:
            return f

def novo_medico():
    crm = input("CRM: ")
    if not validar_medico(crm=crm):
        print("CRM já cadastrado no sistema!!!! Utilizar outro CRM!")
        return
    nome = input("Nome: ")
    email = input("Email: ")
    opcao = input("Especialidade: [cardiologia ou neurologia] ")
    especialidade = opcao
    if opcao == "cardiologia":
        especialidade = "cardiologia"
    elif opcao == "neurologia":
        especialidade = "neurologia"
    else:
        print("opção invalida!!! digite: [cardiologia ou neurologia]")
        return
    cnpj = input("Digite cnpj da Clinica: ")
    if not validar_clinica(cnpj):

        clinica = buscar_clinica_base(cnpj)
        print("Clinica encontrada",clinica['nome'])
    else:
        print('Clinica não encontrada')
        clinica = 'sem vínculo'
        return

    medico = {
        "crm": crm,
        "nome": nome,
        "email": email,
        "especialidade": especialidade,
        "clinica": clinica
    }
    base_medico.append(medico)
    print("Médico salvo com sucesso!")



def listar_medicos():
    print("------------------------------------------------------------------")
    print("Registros encontrados: ", len(base_medico))
    if len(base_medico) > 0:
        print("%20s | %20s | %20s| %20s" % ("Nome", "CRM", "Email", "Clinica"))
        for i, medico in enumerate(base_medico):
            print("%20s | %20s | %20s| %20s" % (medico["nome"], medico["crm"], medico["email"], medico["clinica"]["nome"]))
    print("------------------------------------------------------------------")

def editar_medico():
    crm = input('Digite o CRM do Médico')

    for i, medico in enumerate(base_medico):
        if medico["crm"] == crm:
            print("----------------------MÉDICO A SER ATUALIZADO--------------------")
            print("%20s | %20s | %20s" % ("Nome", "CRM", "Email"))
            print("%20s | %20s | %20s" % (medico["nome"], medico["crm"], medico["email"]))

            opcao = int(input("deseja modificar o CRM do Médico [1-Sim 2-Não]"))
            if opcao == 1:
                crmmodificado = input('informe novo CRM:')
                medico["crm"] = crmmodificado

            opcao = int(input('deseja modificar o Nome do Médico? [1-Sim 2-Não]'))
            if opcao == 1:
                nome = input('informe novo Nome:')
                medico["nome"] = nome

            opcao = int(input('deseja modificar o Email? [1-Sim 2-Não]'))
            if opcao == 1:
                email = input('informe novo Email:')
                medico["email"] = email

            opcao = int(input('deseja modificar a Especialidade? [1-Sim 2-Não]'))
            if opcao == 1:
                especialidade = input('informe nova Especialidade:')
                medico["especialidade"] = especialidade

            opcao = int(input('deseja modificar a Clínica? [1-Sim 2-Não]'))
            if opcao == 1:
                clinica = input('informe nova Clínica:')
                medico["clinica"] = clinica



            base_medico[i] = medico
            print("----------------------ATUALIZADO COM SUCESSO--------------------")
            print("%20s | %20s | %20s" % ("Nome", "CRM", "Email"))
            print("%20s | %20s | %20s" % (medico["nome"], medico["crm"], medico["email"]))

            input('pressione qualquer tecla para continuar')
            return
    print('MÉDICO NÃO ENCONTRADO!!!')


def remover_medico():
    crm = input('Digite o CRM do Médico')

    for i, medico in enumerate(base_medico):
        if medico["crm"] == crm:
            print("----------------------MÉDICO A SER EXCLUIDO--------------------")
            print("%20s | %20s | %20s" % ("Nome", "CRM", "Email"))
            print("%20s | %20s | %20s" % (medico["nome"], medico["crm"], medico["email"]))

            opcao = int(input('deseja apagar o registro do Médico [1-Sim 2-Não]'))
            if opcao == 1:
                base_medico.pop(i)
                input('Registro removido com sucesso')
                input('pressione qualquer tecla para continuar')
                return
    print('Médico não encontrado!!!')


def buscar_medico():
    crm = input('Digite o CRM do Médico')

    for i, medico in enumerate(base_medico):
        if medico["crm"] == crm:
            print("========================================================")
            print("-----------MÉDICO ENCONTRADO---------")

            print("Nome: ", (medico["nome"]))
            print("CRM: ", (medico["crm"]))
            print("E-mail: ", (medico["email"]))
            print("Especialidade: ", (medico["especialidade"]))
            print("Clínica: ", (medico["clinica"]['nome']))
            print("========================================================")
        else:
            print('medico não encontrado')
            return

def pesq_especialidade():
    especialidade = input('Digite a especialidade do Médico')
    print("-----------MÉDICO(S) ENCONTRADO(S) POR ESPECIALIDADE---------")
    print("============================================================================================")

    for i, medico in enumerate(base_medico):
        if medico["especialidade"] == especialidade:

            print("Nome: ", (medico["nome"]))
            print("CRM: ", (medico["crm"]))
            print("E-mail: ", (medico["email"]))
            print("Especialidade: ", (medico["especialidade"]))
            print("Clínica: ", (medico["clinica"]['nome']))
            print("========================================================")




