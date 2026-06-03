# Função que exibe o menu principal e retorna a opção escolhida pelo usuário
def funcao_menu():
    print("\n------BEM-VINDO AO SISTEMA DE CADASTRO DE ALUNOS------")
    print("\n1 - Para Adicionar aluno ")
    print("2 - Para Listar todos os alunos")
    print("3 - Para Buscar aluno pelo nome ")
    print("4 - Para Remover aluno ")
    print("5 - Para Mostar media geral das notas")
    print("6 - Para Sair")
    print("----------------------------//------------------------------")

    opcao = int(input("\nDigite o numero que corresponde com a acao que deseja fazer no sistema --> "))
    return opcao


# Lista responsável por armazenar os dados dos alunos
lista_alunos_cad = []


# Função para cadastrar um novo aluno
def add_aluno():

    nome = str(input("Digite o nome do aluno --> "))
    idade = int(input("Digite a idade do aluno --> "))

    # Validação da nota (somente valores entre 0 e 10)
    while True:
        nota = float(input("Digite a nota do aluno (de 0 a 10) --> "))
        if 0 <= nota <= 10:
            break
        else:
            print("Nota Invalida !")

    # Dicionário contendo as informações do aluno
    info_alunos = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }

    # Adiciona o aluno na lista principal
    lista_alunos_cad.append(info_alunos)


# Função para listar todos os alunos cadastrados
def listar_alunos():
    if len(lista_alunos_cad) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in lista_alunos_cad:
            print("-----Cadastro------")
            print(f"\nNome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Nota: {aluno['nota']}")


# Função para buscar um aluno pelo nome
def busca_por_nome():
    if len(lista_alunos_cad) == 0:
        print("Nenhum aluno cadastrado.")

    for aluno in lista_alunos_cad:
        if aluno["nome"].strip().title() == nome.strip().title():

            # Exibe os dados do aluno encontrado
            print(f"\nO aluno {aluno['nome']} está na lista! :)")
            print(f"Idade desse aluno: {aluno['idade']}")
            print(f"Nota desse aluno: {aluno['nota']}")
            break
    else:
        print("\nO aluno não está na lista :( !")


# Função para remover um aluno pelo nome
def remover_aluno():
    if len(lista_alunos_cad) == 0:
        print("Nenhum aluno cadastrado.")

    for aluno in lista_alunos_cad:
        if aluno["nome"].strip().title() == nome.strip().title():

            # Remove o aluno da lista
            print(f"\nO aluno {aluno['nome']} esta na lista e ele foi removido do sistema :( ")
            lista_alunos_cad.remove(aluno)

            print("-----Lista atualizada sem esse aluno------\n")
            print(lista_alunos_cad)
            break

    print(lista_alunos_cad)


# Função para calcular a média geral das notas
def media_total_notas():

    # Verifica se existem alunos cadastrados
    if len(lista_alunos_cad) == 0:
        print("Nenhum aluno cadastrado. Logo, nao se tem notas para serem operadas!")
        return

    soma_total = 0

    # Soma todas as notas cadastradas
    for aluno in lista_alunos_cad:
        soma_total += aluno['nota']

    # Calcula a média das notas
    media = soma_total / len(aluno)

    print(f"Media das notas dos alunos --> {media}")


# Loop principal do sistema
while True:

    # Recebe a opção escolhida no menu
    opcao = funcao_menu()

    # Adiciona um novo aluno
    if opcao == 1:
        add_aluno()

    # Lista todos os alunos cadastrados
    if opcao == 2:
        listar_alunos()

    # Busca um aluno pelo nome
    if opcao == 3:
        nome = str(input("Digite o nome do aluno que voce deseja procurar no sistema --> ").lower())
        busca_por_nome()

    # Remove um aluno pelo nome
    if opcao == 4:
        nome = str(input("Digite o nome do aluno que voce deseja remover do sistema --> "))
        remover_aluno()

    # Exibe a média geral das notas
    if opcao == 5:
        media_total_notas()

    # Encerra o sistema
    if opcao == 6:
        print("Saindo do Sistema...")
        break

      
print("-----------Esse foi o meu primeiro projeto em Python !!----------------")

    




