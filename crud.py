# Variáveis Globais
proximo_id = 1

# Função para obter o próximo ID a partir do arquivo de tarefas
def get_proximo_id():
    try:
        with open('tarefas.txt', 'r') as arquivo_txt:
            linhas = arquivo_txt.readlines()
            if linhas:
                ultima_linha = linhas[-1].strip()
                partes = ultima_linha.split(', ')
                return int(partes[0]) + 1
            else:
                return 1  # Caso o arquivo esteja vazio
    except FileNotFoundError:
        return 1  # Caso o arquivo não exista

def adicionar_Tarefa(lista_tarefas, nova_tarefa):
    """Adiciona uma nova tarefa à lista e ao arquivo, mantendo a ordem crescente por ID."""
    global proximo_id
    id_tarefa = proximo_id
    proximo_id += 1
    lista_tarefas.append({"id": id_tarefa, "descricao": nova_tarefa, "status": "Pendente"})
    lista_tarefas.sort(key=lambda x: x['id'])  # Ordena a lista de tarefas por ID
    with open('tarefas.txt', 'w') as arquivo_txt:  # Reescreve o arquivo inteiro
        for tarefa in lista_tarefas:
            arquivo_txt.write(f"{tarefa['id']}, {tarefa['descricao']}, {tarefa['status']};\n")
    print("Tarefa adicionada com sucesso!")

def editar_Tarefa(lista_tarefas, num_tarefa, nova_tarefa):
    """Edita uma tarefa existente e atualiza o arquivo."""
    for tarefa in lista_tarefas:
        if tarefa["id"] == num_tarefa:
            tarefa["descricao"] = nova_tarefa
            atualizar_Arquivo(lista_tarefas)
            print("Tarefa editada com sucesso!")
            return
    print("Tarefa inválida")

def remover_Tarefa(lista_tarefas, num_tarefa):
    """Remove uma tarefa e atualiza o arquivo."""
    for tarefa in lista_tarefas:
        if tarefa["id"] == num_tarefa:
            lista_tarefas.remove(tarefa)
            atualizar_Arquivo(lista_tarefas)
            print("Tarefa removida com sucesso!")
            return
    print("Tarefa inválida")

def listar_Tarefas():
    """Lista todas as tarefas do arquivo."""
    try:
        with open('tarefas.txt', 'r') as arquivo_txt:
            linhas = arquivo_txt.readlines()
            if not linhas:
                print("\nNenhuma tarefa pendente.")
            else:
                print("\nTarefas:")
                for linha in linhas:
                    partes = linha.strip().split(', ')
                    if len(partes) >= 3:  # Considera apenas as linhas com pelo menos três valores
                        id_tarefa, descricao, status = partes
                        print(f"{id_tarefa}. {descricao} - {status}")
                    else:
                        print(f"A linha '{linha.strip()}' não pôde ser processada corretamente.")
                print("\n")
    except FileNotFoundError:
        print("Arquivo 'tarefas.txt' não encontrado.")


def marcar_Como_Concluida(lista_tarefas, num_tarefa):
    """Marca uma tarefa como concluída e atualiza o arquivo."""
    for tarefa in lista_tarefas:
        if tarefa["id"] == num_tarefa:
            tarefa["status"] = "Concluída"
            atualizar_Arquivo(lista_tarefas)
            print("Tarefa marcada como concluída com sucesso!")
            return
    print("Tarefa inválida")

def atualizar_Arquivo(lista_tarefas):
    """Atualiza o arquivo 'tarefas.txt' com base na lista de tarefas."""
    with open('tarefas.txt', 'w') as arquivo_txt:
        for tarefa in lista_tarefas:
            arquivo_txt.write(f"{tarefa['id']}, {tarefa['descricao']}, {tarefa['status']};\n")
            
def carregar_Tarefas():
    tarefas = []
    try:
        with open('tarefas.txt', 'r') as arquivo_txt:
            linhas = arquivo_txt.readlines()
            for linha in linhas:
                partes = linha.strip().split(', ')
                if len(partes) >= 3:  # Considera apenas as linhas com pelo menos três valores
                    id_tarefa, descricao, status = partes
                    tarefas.append({"id": int(id_tarefa), "descricao": descricao, "status": status})
                else:
                    print(f"A linha '{linha.strip()}' não pôde ser processada corretamente.")
    except FileNotFoundError:
        print("Arquivo 'tarefas.txt' não encontrado.")
    return tarefas