### Este código implementa uma pequena aplicação de gerenciamento de clínicas médicas em Python. A aplicação permite cadastrar, listar, editar e remover clínicas.

### clone: https://github.com/jonathan-pereira-lima/projetoClinicaIP


Requisitos

Python 3.8 ou superior
Instalação

pip install -r requirements.txt
Execução

python main.py
Uso

### A aplicação apresenta os seguintes menus com as seguintes opções:


-----------MENU GERAL---------  
1 - Menu de Paciente  
2 - Menu de Marcação de Consulta  
3 - Menu de Médico  
4 - Menu de Funcionário  
5- Menu de Clínica  
6 – SAIR  
Digite opção: >>>

-----------MENU PACIENTE---------  
1 - Cadastrar Paciente  
2 - Buscar Paciente por cpf  
3 - Editar Paciente  
4 - Remover Paciente  
5 - Listar Todos os Pacientes  
6 – SAIR  

------------MENU MARCAÇÃO DE CONSULTAS---------  
1 - Marcar Consulta  
2 - Buscar Consulta por Paciente  
3 - Editar Consulta  
4 - Remover Consulta  
5 - Listar Consultas  
6 - Listar Consultas por Retorno  
7 - Listar Consultas por intervalo de datas  
8 – SAIR  

-----------MENU MÉDICO---------  
1 - Cadastrar Médico  
2 - Buscar Médico por CRM  
3 - Editar Médico  
4 - Remover Médico  
5 - Listar Todos os médicos  
6 - Listar Médico por Especialidade  
7 – SAIR  

-----------MENU FUNCIONÁRIO---------  
1 - Cadastrar Funcionário  
2 - Buscar Funcionário por Matrícula  
3 - Editar Funcionário  
4 - Remover Funcionário  
5 - Listar Todos os Funcionários  
6 – SAIR  

-----------MENU CLÍNICA---------  
1 - Cadastrar Clínica  
2 - Buscar Clínica por CNPJ  
3 - Editar Clínica  
4 - Remover Clínica  
5 - Listar Todas as Clínicas  
6 – SAIR  

### Exemplos:

Para cadastrar uma nova clínica, digite 1 e siga as instruções.
Para listar todas as clínicas, digite 2.
Para editar os dados de uma clínica, digite 3 e informe o CNPJ da clínica.
Para remover uma clínica, digite 4 e informe o CNPJ da clínica.
Para buscar uma clínica, digite 5 e informe o CNPJ da clínica.
Comentários

O código é relativamente simples e pode ser facilmente adaptado para atender a necessidades específicas. Algumas melhorias que podem ser feitas incluem:

* Validação dos dados de entrada (por exemplo, garantir que o CNPJ seja válido).  
* Tratamento de erros (por exemplo, exibir uma mensagem de erro se uma operação falhar).  
* Armazenamento dos dados em um banco de dados.  
