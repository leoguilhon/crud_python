from crud import adicionar_Tarefa, editar_Tarefa, remover_Tarefa, listar_Tarefas, marcar_Como_Concluida, carregar_Tarefas, get_proximo_id

# Principal
def main():
    tarefas = carregar_Tarefas()
    global proximo_id
    proximo_id = get_proximo_id()

    while True:
        print("\nMenu:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Editar Tarefa")
        print("0. Sair")

        escolha = input("Escolha a opção desejada: ")

        if escolha == "1":
            nova_tarefa = input("Nova tarefa: ")
            adicionar_Tarefa(tarefas, nova_tarefa)
        elif escolha == "2":
            listar_Tarefas()
        elif escolha == "3":
            listar_Tarefas()
            num_tarefa = input("Tarefa concluída: ")
            if num_tarefa.isdigit():
                marcar_Como_Concluida(tarefas, int(num_tarefa))
            else:
                print("Por favor, insira um número válido.")
        elif escolha == "4":
            listar_Tarefas()
            num_tarefa = input("Tarefa a ser removida: ")
            if num_tarefa.isdigit():
                remover_Tarefa(tarefas, int(num_tarefa))
            else:
                print("Por favor, insira um número válido.")
        elif escolha == "5":
            listar_Tarefas()
            num_tarefa = input("Digite o número da tarefa que deseja editar: ")
            if num_tarefa.isdigit():
                nova_tarefa = input("Digite o novo nome da tarefa: ")
                editar_Tarefa(tarefas, int(num_tarefa), nova_tarefa)
            else:
                print("Por favor, insira um número válido.")
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()