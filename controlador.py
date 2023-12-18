#======================================================================
#>>>Projeto de I.P
#>>>Professor: Zildomar
#>>>Aluno:Jośe Jonathan Pereira Lima
#>>> 1 período
#======================================================================



import clinica
import funcionario
import medico
import consulta
import paciente
import menuProjeto



def controlador_menu_paciente():
    while True:
        menuProjeto.menu_paciente()
        entrada = input(">>> ")
        if entrada == "1":
            paciente.novo_paciente()
        elif entrada == "2":
            paciente.buscar_paciente()
        elif entrada == "3":
            paciente.editar_Paciente()
        elif entrada == "4":
            paciente.remover_paciente()
        elif entrada == "5":
            paciente.listar_pacientes()
        elif entrada == "6":
            break


def controlador_menu_consultas():
    while True:
        menuProjeto.menu_consulta()
        entrada = input(">>> ")
        if entrada == "1":
            consulta.nova_consulta()
        elif entrada == "2":
            consulta.buscar_consulta()
        elif entrada == "3":
            consulta.editar_consulta()
        elif entrada == "4":
            consulta.remover_consulta()
        elif entrada == "5":
            consulta.listar_consultas()
        elif entrada == "6":
            consulta.listarConsultasRetorno()
        elif entrada == "7":
            consulta.listarConsultaDatas()
        elif entrada == "8":
            break

def controlador_menu_medicos():
    while True:
        menuProjeto.menu_medico()
        entrada = input(">>>")
        if entrada == "1":
            medico.novo_medico()
        elif entrada == "2":
            medico.buscar_medico()
        elif entrada == "3":
            medico.editar_medico()
        elif entrada == "4":
            medico.remover_medico()
        elif entrada == "5":
            medico.listar_medicos()
        elif entrada == "6":
            medico.pesq_especialidade()
        elif entrada == "7":
            break


def controlador_menu_funcionario():
    while True:
        menuProjeto.menu_funcionario()
        entrada = input (">>>")
        if entrada == "1":
            funcionario.novo_funcionario()
        elif entrada == "2":
            funcionario.buscar_funcionario()
        elif entrada == "3":
            funcionario.editar_funcionarios()
        elif entrada == "4":
            funcionario.remover_funcionario()
        elif entrada == "5":
            funcionario.listar_funcionarios()
        elif entrada == "6":
            break

def controlador_menu_clinica():
    while True:
        menuProjeto.menu_clinica()
        entrada = input(">>>")
        if entrada == "1":
            clinica.nova_clinica()
        elif entrada == "2":
            clinica.buscar_clinica()
        elif entrada == "3":
            clinica.editar_clinica()
        elif entrada == "4":
            clinica.remover_clinica()
        elif entrada == "5":
            clinica.listar_clinicas()
        elif entrada == "6":
            break



