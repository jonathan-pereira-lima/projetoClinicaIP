#======================================================================
#>>>Projeto de I.P
#>>>Professor: Zildomar
#>>>Aluno:Jośe Jonathan Pereira Lima
#>>> 1 período
#======================================================================



base_paciente = []

def validar_paciente(cpf=None):
    for f in base_paciente:
        if cpf != None and cpf == f["cpf"]:
            return False

    return True

def buscar_paciente_base (cpf=None):
    for f in base_paciente:
        if cpf != None and cpf == f["cpf"]:
            return f

def novo_paciente():
    cpf = input("CPF: ")
    if not validar_paciente(cpf=cpf):
        print("CPF já cadastrado no sistema!!!! Utilizar outro CPF!")
        return
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    paciente = {
        "cpf": cpf,
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "endereco": endereco
    }
    base_paciente.append(paciente)
    print("Paciente salvo com sucesso!")

def listar_pacientes():
    print("------------------------------------------------------------------")
    print("Registros encontrados: ", len(base_paciente))
    if len(base_paciente) > 0:
        print("%20s | %20s | %20s" % ("Nome", "CPF", "Email"))
        for i, paciente in enumerate(base_paciente):
            print("%20s | %20s | %20s" % (paciente["nome"], paciente["cpf"], paciente["email"]))
    print("------------------------------------------------------------------")

def editar_Paciente():
    cpf = input('digite o CPF')

    for i, paciente in enumerate(base_paciente):
        if paciente["cpf"] == cpf:
            print("----------------------PACIENTE A SER ATUALIZADO--------------------")
            print("%20s | %20s | %20s" % ("Nome", "CPF", "Email"))
            print("%20s | %20s | %20s" % (paciente["nome"], paciente["cpf"], paciente["email"]))

            opcao = int(input("deseja modificar o CPF do Paciente[1-Sim 2-Não]"))
            if opcao == 1:
                cpfmodificado = input('informe novo CPF:')
                paciente["cpf"] = cpfmodificado

            opcao = int(input('deseja modificar o Nome do paciente? [1-Sim 2-Não]'))
            if opcao == 1:
                nome = input('informe novo Nome:')
                paciente["nome"] = nome

            opcao = int(input('deseja modificar o Email? [1-Sim 2-Não]'))
            if opcao == 1:
                email = input('informe novo Email:')
                paciente["email"] = email

            opcao = int(input('deseja modificar o telefone? [1-Sim 2-Não]'))
            if opcao == 1:
                telefone = input('informe novo telefone:')
                paciente["telefone"] = telefone

            opcao = int(input('deseja modificar o endereço? [1-Sim 2-Não]'))
            if opcao == 1:
                endereco = input('informe novo endereço:')
                paciente["endereco"] = endereco



            base_paciente[i] = paciente
            print("----------------------ATUALIZADO COM SUCESSO--------------------")
            print("%20s | %20s | %20s" % ("Nome", "CPF", "Email"))
            print("%20s | %20s | %20s" % (paciente["nome"], paciente["cpf"], paciente["email"]))

            input('pressione qualquer tecla para continuar')
            return
    print('PACIENTE NÃO ENCONTRADO!!!')

def remover_paciente():
    cpf = input('digite cpf')

    for i, paciente in enumerate(base_paciente):
        if paciente["cpf"] == cpf:
            print("----------------------PACIENTE A SER EXCLUIDO--------------------")
            print("%20s | %20s | %20s" % ("Nome", "CPF", "Email"))
            print("%20s | %20s | %20s" % (paciente["nome"], paciente["cpf"], paciente["email"]))

            opcao = int(input('deseja apagar o registro do paciente [1-Sim 2-Não]'))
            if opcao == 1:
                base_paciente.pop(i)
                input('Registro removido com sucesso')
                input('pressione qualquer tecla para continuar')
                return
    print('paciente não encontrado!!!')

def buscar_paciente():
    cpf = input('digite cpf')

    for i, paciente in enumerate(base_paciente):
        if paciente["cpf"] == cpf:
            print("========================================================")
            print("-----------PACIENTE ENCONTRADO---------")

            print("nome: ", (paciente["nome"]))
            print("cpf: ", (paciente["cpf"]))
            print("email: ", (paciente["email"]))
            print("telefone: ", (paciente["telefone"]))
            print("Endereço: ", (paciente["endereco"]))
            print("========================================================")




