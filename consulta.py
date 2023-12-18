#======================================================================
#>>>Projeto de I.P
#>>>Professor: Zildomar
#>>>Aluno:Jośe Jonathan Pereira Lima
#>>> 1 período
#======================================================================
from medico import *
from paciente import *
from datetime import datetime, timedelta

base_consulta = []


def string_como_data(string):
    return datetime.strptime(string, "%d/%m/%Y").date()


def string_como_hora(string):
    return datetime.strptime(string, "%H:%M").time()


def string_como_datetime(string):
    return datetime.strptime(string, "%d/%m/%Y %H:%M")


def filtrar_por_periodo(periodo_inicio, periodo_fim):
    filtro = []
    for consulta in base_consulta:
        periodo_consulta = datetime.combine(consulta["data"], consulta["hora"])
        if periodo_inicio <= periodo_consulta <= periodo_fim:
            filtro.append(consulta)
    return filtro

def validar_consulta(momento_consulta):
    duracao_consulta = timedelta(minutes=30)  # 30 minutos

    for consulta in base_consulta:
        momento_consulta_agendada = datetime.combine(consulta["data"], consulta["hora"])

        if momento_consulta > momento_consulta_agendada + duracao_consulta:
            return False
        elif not momento_consulta + duracao_consulta <= momento_consulta_agendada:
            return False
    return True

def nova_consulta():
    try:
        datahora = string_como_datetime(input("Data e Hora (DD/MM/YYYY HH:MM): "))
    except ValueError:
        print("Formato inválido de data")
        return
    if not validar_consulta(momento_consulta=datahora):
        print("Data/hora já está agendada no sistema!!!! por favor Utilizar outra Data/hora!")
        return

    codigo = input("Código: ")
    cpf = input("Digite CPF do Paciente: ")
    if not validar_paciente(cpf):
        paciente = buscar_paciente_base(cpf)
        print("Paciente encontrado", paciente['nome'])
    else:
        print('Paciente não encontrado')
        return

    data = datahora.date()
    hora = datahora.time()

    crm = input("Digite crm do médico: ")
    if not validar_medico(crm):
        medico = buscar_medico_base(crm)
        print("Médico encontrado", medico['nome'])
    else:
        print('Medico não encontrado')
        return

    retorno = input("É Retorno [1-Sim 2-Não]: ")
    consulta = {
        "datahora": datahora,
        "codigo": codigo,
        "paciente": paciente,
        "data": data,
        "hora": hora,
        "medico": medico,
        "retorno": retorno,
    }
    base_consulta.append(consulta)
    print("Consulta salva com sucesso!")


def listar_consultas():
    print("------------------------------------------------------------------")
    print("Registros encontrados: ", len(base_consulta))
    if len(base_consulta) > 0:
        print("%20s | %20s | %20s | %20s" % ("Código da Consulta", "Data/Hora", "Paciente", "Médico"))
        for i, consulta in enumerate(base_consulta):
            print("%20s | %20s | %20s | %20s" % (consulta["codigo"], consulta["datahora"], consulta["paciente"]['nome'], consulta["medico"]["nome"]))
    print("------------------------------------------------------------------")

def editar_consulta():
    codigo = input('Digite o Código da Consulta')

    for i, consulta in enumerate(base_consulta):
        if consulta["codigo"] == codigo:
            print("----------------------CONSULTA A SER ATUALIZADA--------------------")
            print("%20s | %20s | %20s" % ("Código", "Data/Hora", "Paciente"))
            print("%20s | %20s | %20s" % (consulta["codigo"], consulta["datahora"], consulta["paciente"]['nome']))

            opcao = int(input("deseja modificar o CRM do Médico [1-Sim 2-Não]"))
            if opcao == 1:
                datahoramodificada = input('informe nova Data e Horário [00/00, 00hs]:')
                consulta["datahora"] = datahoramodificada

            opcao = int(input('deseja modificar o Código da Consulta? [1-Sim 2-Não]'))
            if opcao == 1:
                codigo = input('informe novo código:')
                consulta["codigo"] = codigo

            opcao = int(input('deseja modificar o Paciente? [1-Sim 2-Não]'))
            if opcao == 1:
                paciente = input('informe novo Paciente:')
                consulta["paciente"] = paciente

            opcao = int(input('deseja modificar o Médico  [1-Sim 2-Não]'))
            if opcao == 1:
                medico = input('informe novo Médico:')
                consulta["medico"] = medico

            opcao = int(input('deseja modificar a opção de retorno? [1-Sim 2-Não]'))
            if opcao == 1:
                retorno = input('é retorno [1-Sim 2-Não]:')
                consulta["retorno"] = retorno



            base_consulta[i] = consulta
            print("----------------------ATUALIZADO COM SUCESSO--------------------")
            print("%20s | %20s | %20s" % ("Código", "Data/Hora", "Paciente"))
            print("%20s | %20s | %20s" % (consulta["codigo"], consulta["datahora"], consulta["paciente"]['nome']))

            input('pressione qualquer tecla para continuar')
            return
    print('CONSULTA NÃO ENCONTRADA!!!')


def remover_consulta():
    codigo = input('Digite o Código da Consulta')

    for i, consulta in enumerate(base_consulta):
        if consulta["codigo"] == codigo:
            print("----------------------CONSULTA A SER EXCLUIDA--------------------")
            print("%20s | %20s | %20s" % ("Código", "Data/Hora", "Paciente"))
            print("%20s | %20s | %20s" % (consulta["codigo"], consulta["datahora"], consulta["paciente"]['nome']))

            opcao = int(input('deseja apagar o registro da Consulta [1-Sim 2-Não]'))
            if opcao == 1:
                base_consulta.pop(i)
                input('Registro removido com sucesso')
                input('pressione qualquer tecla para continuar')
                return
    print('Consulta não encontrada!!!')


def buscar_consulta():
    paciente = input('Digite o Paciente')

    for i, consulta in enumerate(base_consulta):
        if consulta["paciente"]['nome'] == paciente:
            print("========================================================")
            print("-----------CONSULTA ENCONTRADA---------")

            print("Código: ", (consulta["codigo"]))
            print("Paciente: ", (consulta["paciente"]['nome']))
            print("Médico: ", (consulta["medico"]["nome"]))
            print("Data/Hora: ", (consulta["datahora"]))
            print("Retorno: ", (consulta["retorno"]))
            print("========================================================")

def listarConsultasRetorno():
    retorno = input('Digite retorno [1-Sim 2-Não] ')
    print("-----------CONSULTAS(S) ENCONTRADA(S) POR RETORNO---------")
    print("============================================================================================")

    for i, consulta in enumerate(base_consulta):
        if consulta["retorno"] == retorno:
            print("%20s | %20s | %20s | %20s" % ("Código da Consulta", "Data/Hora", "Paciente", "Médico"))
            print("%20s | %20s | %20s | %20s" % (consulta["codigo"], consulta["datahora"], consulta["paciente"]['nome'], consulta["medico"]["nome"]))
            print("=====================================================================================")

def listarConsultaDatas():
    try:
        inicio = string_como_datetime(input("Período inicial (DD/MM/YYYY HH:MM)"))
        fim = string_como_datetime(input("Período final (DD/MM/YYYYY HH:MM): "))
    except:
        print("Formato de data inválido")
        return
    for consulta in filtrar_por_periodo(inicio, fim):
        print("Código: %s, Paciente: %s, Médico: %s" % (consulta["codigo"], consulta["paciente"]['nome'], consulta["medico"]["nome"]))



