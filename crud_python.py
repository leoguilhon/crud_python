menu_status = True
tasks = []
exit_choice = False

def is_not_numeric(value):
    try:
        float(value)
        return False 
    except ValueError:
        return True

while exit_choice is False:
    option = input("Escolha uma opção: (1) Criar tarefa (2) Listar tarefas (3) Deletar tarefa (4) Sair\n")
    if option == '1':
        task_name = input('Insira o nome da tarefa a ser criada: ')
        tasks.append(task_name)
        print(f'Tarefa {task_name} criada com sucesso.')
    elif option == '2':
        print('Tarefas:')
        for task in tasks:
            print(task) 
    elif option == '3':
        task_found = False
        task_name_delete = input('Insira o nome da tarefa a ser deletada: ')
        for task in tasks:
            if task == task_name_delete:
                tasks.remove(task_name_delete)
                task_found = True
                print(f'Tarefa {task_name_delete} deletada com sucesso.')
                break
        if not task_found:
            print(f'Tarefa "{task_name_delete}" não encontrada na lista.')
    elif option == '4':
        print('Saindo do programa...')
        exit_choice = True
    else:
        print('Opção inválida.')
