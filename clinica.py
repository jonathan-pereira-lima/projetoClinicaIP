#======================================================================
#>>>Projeto de I.P
#>>>Professor: Zildomar
#>>>Aluno:Jośe Jonathan Pereira Lima
#>>> 1 período
#======================================================================



base_clinica = []

def validar_clinica(cnpj=None):
    for f in base_clinica:
        if cnpj != None and cnpj == f["cnpj"]:
            return False

    return True

def buscar_clinica_base (cnpj=None):
    for f in base_clinica:
        if cnpj != None and cnpj == f["cnpj"]:
            return f

    return None

def nova_clinica():
    cnpj = input("CNPJ: ")
    if not validar_clinica(cnpj=cnpj):
        print("CNPJ já cadastrado no sistema!!!! Utilizar outro CNPJ!")
        return
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    clinica = {
        "cnpj": cnpj,
        "nome": nome,
        "endereco": endereco
    }
    base_clinica.append(clinica)
    print("Clínica salva com sucesso!")




def listar_clinicas():
    print("------------------------------------------------------------------")
    print("Registros encontrados: ", len(base_clinica))
    if len(base_clinica) > 0:
        print("%20s | %20s | %20s" % ("Nome", "CNPJ", "Endereço"))
        for i, clinica in enumerate(base_clinica):
            print("%20s | %20s | %20s" % (clinica["nome"], clinica["cnpj"], clinica["endereco"]))
    print("------------------------------------------------------------------")

def editar_clinica():
    cnpj = input('digite o CNPJ')

    for i, clinica in enumerate(base_clinica):
        if clinica["cnpj"] == cnpj:
            print("----------------------CLINICA A SER ATUALIZADA--------------------")
            print("%20s | %20s | %20s" % ("Nome", "CNPJ", "Endereço"))
            print("%20s | %20s | %20s" % (clinica["nome"], clinica["cnpj"], clinica["endereco"]))

            opcao = int(input("deseja modificar o CNPJ da Clínica? [1-Sim 2-Não]"))
            if opcao == 1:
                cnpjmodificado = input('informe novo CNPJ:')
                clinica["cnpj"] = cnpjmodificado

            opcao = int(input('deseja modificar o Nome da Clínica? [1-Sim 2-Não]'))
            if opcao == 1:
                nome = input('informe novo Nome:')
                clinica["nome"] = nome

            opcao = int(input('deseja modificar o endereço? [1-Sim 2-Não]'))
            if opcao == 1:
                endereco = input('informe novo endereço:')
                clinica["endereco"] = endereco



            base_clinica[i] = clinica
            print("----------------------ATUALIZADO COM SUCESSO--------------------")
            print("%20s | %20s | %20s" % ("Nome", "CNPJ", "Endereço"))
            print("%20s | %20s | %20s" % (clinica["nome"], clinica["cnpj"], clinica["endereco"]))

            input('pressione qualquer tecla para continuar')
            return
    print('CLÍNICA NÃO ENCONTRADA!!!')


def remover_clinica():
    cnpj = input('digite o CNPJ da clinica que deseja excluir: ')

    for i, clinica in enumerate(base_clinica):
        if clinica["cnpj"] == cnpj:
            print("----------------------CLÍNICA A SER EXCLUIDA--------------------")
            print("%20s | %20s | %20s" % ("Nome", "CNPJ", "Endereço"))
            print("%20s | %20s | %20s" % (clinica["nome"], clinica["cnpj"], clinica["endereco"]))

            opcao = int(input('deseja apagar o registro da Clínica [1-Sim 2-Não]'))
            if opcao == 1:
                base_clinica.pop(i)
                input('Registro removido com sucesso')
                input('pressione qualquer tecla para continuar')
                return
    print('Clínica não encontrada!!!')


def buscar_clinica():
    cnpj = input('digite cnpj')

    for i, clinica in enumerate(base_clinica):
        if clinica["cnpj"] == cnpj:
            print("========================================================")
            print("-----------CLÍNICA ENCONTRADA---------")

            print("Nome: ", (clinica["nome"]))
            print("CNPJ: ", (clinica["cnpj"]))
            print("Endereço: ", (clinica["endereco"]))
            print("========================================================")




