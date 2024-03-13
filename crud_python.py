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
    option = input("Escolha uma opção: (1) Criar tarefa (2) Listar tarefas (3) Deletar tarefa (4) Editar Tarefa (5) Sair\n")
    if option == '1':
        task_name = input('Insira o nome da tarefa a ser criada: ')
        tasks.append(task_name)
        print(f'Tarefa {task_name} criada com sucesso.')
    elif option == '2':
        if tasks:
            print('Tarefas:')
            for i, task in enumerate(tasks):
                print(i+1, task)
        else:
            print('Não há tarefas registradas.')
    elif option == '3':
        task_found = False
        task_id_delete = int(input('Insira o id da tarefa a ser deletada: '))
        for i, task in enumerate(tasks):
            if i + 1 == task_id_delete:
                del tasks[i]
                task_found = True
                print(f'Tarefa "{task_id_delete}" deletada com sucesso.')
                break
        if not task_found:
            print(f'Tarefa "{task_id_delete}" não encontrada na lista.')
    elif option == '4':
        print('Tarefas:')
        for i, task in enumerate(tasks):
            print(i+1, task)
        task_to_edit = input('Insira o id da tarefa a ser editada: ')
        if task_to_edit:
            new_name = input('Insira o novo nome da tarefa: ')
            tasks[i-1] = new_name;
            print('Tarefa editada com sucesso.')
        else:
            print('Tarefa não existe.')
    elif option == '5':
        print('Saindo do programa...')
        exit_choice = True
    else:
        print('Opção inválida.')
