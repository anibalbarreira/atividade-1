class Tarefa:
    def __init__(self, titulo, descricao, prioridade):
       self.titulo = titulo
       self.descricao = descricao
       self.prioridade = prioridade

    def __str__(self):
        return f"Tarefa: {self.titulo} - {self.descricao} - {self.prioridade}"

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.lista_tarefas = []

    def criar_tarefas(self, titulo, descricao, prioridade):
        nova_tarefa = Tarefa(titulo, descricao, prioridade)
        self.lista_tarefas.append(nova_tarefa)

    def listar_tarefas(self):
        for tarefa in self.tarefa:
            print (tarefa)
        
class Sistema:
    def __init__(self):
        self.lista_usuarios = []
        self.usuario_logado = None


    def cadastrar_usuario(self):
        nome = input("Digite um nome: ")
        email = input("Digite um email: ")

        if "@" not in email:
            print("E-mail inválido! /n")
            return
        else:
            novo_usuario = Usuario (nome, email)
            self.lista_usuarios.append(novo_usuario)
            print("Usuario cadastrado com sucesso!")

    def login(self):
        email = input ("Entre com o email: ")
        senha = input("Entre com a senha: ")
    
        for usuario in self.lista_usuarios:
            if (usuario.email == email) and (usuario.senha == senha):
                self.usuario_logado = usuario
                print(f"Usuario logado: {self.usuario_logado.nome}")
                self.menu_funcionalidades()
                return

        print("Usuario inexistente ou Senha inválida")

    def menu_principal(self):
        opcao_escolhida = ""
        while opcao_escolhida != "0":
            print("Menu - Escolha uma opção:")
            print("1. Cadastrar novo usuário")
            print("2. Fazer Login")
            print("0. Sair: /n")
            opcao_escolhida = input("Escolha: ")

            if opcao_escolhida == "1":
                self.cadastrar_usuario()
            elif opcao_escolhida == "2":
                self.login()    
            elif opcao_escolhida == "0":
                print("Saindo...")
            else:
                print("Opção invalida")

    def menu_funcionalidades(self):
        escolha = ""
        while escolha != "0":
            print("\n------Tarefas------")
            print("1 - Criar tarefa")
            print("2 - Listar tarefa")
            escolha = input("Selecione: ")

            if escolha == "1":
                titulo = input("Insira um titulo: ")
                descricao = input("Insira uma descrição")
                prioridade = input("Insira uma prioridade (Alta, Média ou Baixa): ")
                self.usuario_logado.criar_tarefa(titulo, descricao, prioridade)
            
            elif escolha == "2":
                self.usuario_logado.listar_tarefas()

teste = Sistema()
teste.menu_principal()


