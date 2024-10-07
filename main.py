from Task import *
from helpers import *
# task = Task("Ir ao boxe")
# task.create()
# task.list_all()
# task.list_one(9)
# task.delete(9)
# task.edit(10)
# task.to_finish(10)

executing = True
while executing:
    print('')
    task = Task("")
    task.list_all()
    print('')
    option = input('''
        ToDo           
        1 - Criar tarefa
        2 - Editar tarefa    
        3 - Finalizar tarefa    
        4 - Deletar tarefa
        5 - Lista tarefa especifica
        6 - Sair           
        Digite uma opção: ''')
    clear_terminal()
    match(option):
        case '1':
            description = input('Digite a tarefa: ')
            new = Task(description)
            new.create()
        case '2':
            task.list_all()
            id = input("Digite o código da tarefa a ser editada: ")
            task.edit(id) 
        case '3':
            task.list_all()
            id = input("Digite o código da tarefa a ser finalizada: ")
            task.to_finish(id)    
        case '4':
            task.list_all()
            id = input("Digite o código da tarefa a ser deletada: ")
            task.delete(id)   
        case '5':
            task.list_all()
            id = input("Digite o código da tarefa a ser listada: ")
            task.list_one(id)     
        case '6':
            print('obrigado por usar meu sistema')
            executing = False    
        case _:
            print(f'Opção {option} inválida')    