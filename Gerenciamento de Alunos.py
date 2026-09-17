# Função que exibe o menu principal e retorna a opção escolhida pelo usuário

import tkinter as tk
from tkinter import messagebox


# Lista responsável por armazenar os dados dos alunos
lista_alunos_cad = []


# ---------------- FUNÇÕES DO SISTEMA ---------------- #

# Função para cadastrar um novo aluno
def add_aluno():

    nome = entrada_nome.get()
    idade = entrada_idade.get()
    nota = entrada_nota.get()

    # Verifica se os campos estão preenchidos
    if nome == "" or idade == "" or nota == "":
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    # Validação da idade
    try:
        idade = int(idade)
    except ValueError:
        messagebox.showerror("Erro", "A idade deve ser um número!")
        return

    # Validação da nota
    try:
        nota = float(nota)
    except ValueError:
        messagebox.showerror("Erro", "A nota deve ser um número!")
        return

    if nota < 0 or nota > 10:
        messagebox.showerror("Erro", "A nota deve estar entre 0 e 10!")
        return

    # Dicionário contendo as informações do aluno
    info_aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }

    # Adiciona o aluno na lista
    lista_alunos_cad.append(info_aluno)

    # Limpa os campos
    entrada_nome.delete(0, tk.END)
    entrada_idade.delete(0, tk.END)
    entrada_nota.delete(0, tk.END)

    messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")


# Função para listar todos os alunos
def listar_alunos():

    if len(lista_alunos_cad) == 0:
        messagebox.showinfo("Alunos", "Nenhum aluno cadastrado.")
        return

    texto = ""

    for aluno in lista_alunos_cad:
        texto += (
            f"Nome: {aluno['nome']}\n"
            f"Idade: {aluno['idade']}\n"
            f"Nota: {aluno['nota']}\n"
            "----------------------\n"
        )

    messagebox.showinfo("Alunos cadastrados", texto)


# Função para buscar um aluno pelo nome
def busca_por_nome():

    nome = entrada_busca.get()

    if nome == "":
        messagebox.showwarning("Atenção", "Digite um nome para buscar.")
        return

    for aluno in lista_alunos_cad:

        if aluno["nome"].strip().lower() == nome.strip().lower():

            messagebox.showinfo(
                "Aluno encontrado",
                f"Nome: {aluno['nome']}\n"
                f"Idade: {aluno['idade']}\n"
                f"Nota: {aluno['nota']}"
            )

            return

    messagebox.showinfo(
        "Resultado",
        "O aluno não está cadastrado."
    )


# Função para remover um aluno
def remover_aluno():

    nome = entrada_busca.get()

    if nome == "":
        messagebox.showwarning("Atenção", "Digite um nome para remover.")
        return

    for aluno in lista_alunos_cad:

        if aluno["nome"].strip().lower() == nome.strip().lower():

            lista_alunos_cad.remove(aluno)

            messagebox.showinfo(
                "Aluno removido",
                f"O aluno {aluno['nome']} foi removido."
            )

            entrada_busca.delete(0, tk.END)

            return

    messagebox.showinfo(
        "Resultado",
        "O aluno não foi encontrado."
    )


# Função para calcular a média geral
def media_total_notas():

    if len(lista_alunos_cad) == 0:
        messagebox.showinfo(
            "Média",
            "Nenhum aluno cadastrado."
        )
        return

    soma_total = 0

    for aluno in lista_alunos_cad:
        soma_total += aluno["nota"]

    media = soma_total / len(lista_alunos_cad)

    messagebox.showinfo(
        "Média geral",
        f"A média geral das notas é: {media:.2f}"
    )


# ---------------- INTERFACE ---------------- #

# Cria a janela principal
janela = tk.Tk()

janela.title("Sistema de Cadastro de Alunos")
janela.geometry("500x500")


# Título
titulo = tk.Label(
    janela,
    text="SISTEMA DE CADASTRO DE ALUNOS",
    font=("Arial", 16)
)

titulo.pack(pady=20)


# -------- CADASTRO -------- #

label_nome = tk.Label(janela, text="Nome do aluno:")
label_nome.pack()

entrada_nome = tk.Entry(janela)
entrada_nome.pack()


label_idade = tk.Label(janela, text="Idade:")
label_idade.pack()

entrada_idade = tk.Entry(janela)
entrada_idade.pack()


label_nota = tk.Label(janela, text="Nota:")
label_nota.pack()

entrada_nota = tk.Entry(janela)
entrada_nota.pack()


botao_adicionar = tk.Button(
    janela,
    text="Adicionar aluno",
    command=add_aluno
)

botao_adicionar.pack(pady=10)


# -------- LISTAGEM -------- #

botao_listar = tk.Button(
    janela,
    text="Listar alunos",
    command=listar_alunos
)

botao_listar.pack(pady=5)


# -------- BUSCA / REMOÇÃO -------- #

label_busca = tk.Label(
    janela,
    text="Nome para buscar/remover:"
)

label_busca.pack(pady=(20, 0))

entrada_busca = tk.Entry(janela)
entrada_busca.pack()


botao_buscar = tk.Button(
    janela,
    text="Buscar aluno",
    command=busca_por_nome
)

botao_buscar.pack(pady=5)


botao_remover = tk.Button(
    janela,
    text="Remover aluno",
    command=remover_aluno
)

botao_remover.pack(pady=5)


# -------- MÉDIA -------- #

botao_media = tk.Button(
    janela,
    text="Mostrar média geral",
    command=media_total_notas
)

botao_media.pack(pady=15)


# Inicia o programa
janela.mainloop()
