from controlador import *

def controlador_menu_principal():
    while True:
        menuProjeto.menuPrincipal()
        entrada = input(">>> ")
        if entrada == "1":
            controlador_menu_paciente()
        elif entrada == "2":
            controlador_menu_consultas()
        elif entrada == "3":
            controlador_menu_medicos()
        elif entrada == "4":
            controlador_menu_funcionario()
        elif entrada == "5":
            controlador_menu_clinica()
        elif entrada == "6":
            break

controlador_menu_principal()