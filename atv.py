# Cadastrar tarefas
class Tarefa:
    incrementa_id = 1
    def __init__(self, titulo, descricao, prioridade):
       self.titulo = titulo
       self.descricao = descricao
       self.prioridade = prioridade
       self.status = "Pendente"
       self.id = Tarefa.incrementa_id 
       Tarefa.incrementa_id += 1
# Visualizar tarefas por status e/ou Marcar tarefas como concluídas
    def concluir_tarefa(self):
            self.status = "Concluida"
            print(f"Tarefa: {self.titulo} concluida!")

    def editar_tarefa(self, novo_tiulo, nova_descricao, nova_prioridade):
            self.titulo = novo_titulo
            self.descricao = nova_descricao
            self.prioridade = nova_prioridade
# Marcar tarefas como concluídas
    def __str__(self):
        return f"Tarefa: {self.id} - {self.titulo} - {self.descricao} - {self.prioridade} - {self,status}"
# Cadastrar Usuários
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
            if status is None or tarefa.status == status:
                print(tarefa)
    
    def procura_tarefa(self, id_tarefa):
        for tarefa in self.lista_tarefas:
            if tarefa.id == id_tarefa:
                return tarefa
        return None

    def remover_tarefa(self, id_tarefa):
        tarefa_buscada = self.procura_tarefa(id_tarefa)
        if tarefa_buscada:
            self.lista_tarefas.remove(tarefa_buscada)
        else:
            print("Tarefa não encontrada")

    def limpar_concluidas(self):
        tarefas_ativas = []
        for tarefa in self.lista_tarefas:
            if tarefa.status != "Concluida":
                tarefas_ativas.append(tarefa)
            self.lista_tarefas = tarefas_ativas
# Sistema
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
            print("1 - Criar Tarefa")
            print("2 - Listar Tarefa")
            print("3 - Listar Tarefas pendentes")
            print("4 - Listar Tarefas concluidas")
            print("5 - Editar Tarefas")
            print("6 - Editar Tarefas não encontrada")
            escolha = input("Selecione: ")

            if escolha == "1":
                titulo = input("Insira um titulo: ")
                descricao = input("Insira uma descrição")
                prioridade = input("Insira uma prioridade (Alta, Média ou Baixa): ")
                self.usuario_logado.criar_tarefa(titulo, descricao, prioridade)
            
            elif escolha == "2":
                self.usuario_logado.listar_tarefas()

            elif escolha == "3":
                self.usuario_logado.listar_tarefas("Pendente")

            elif escolha == "4":
                self.usuario_logado.listar_tarefas("Cocnluida")

            elif escolha == "5":
                id = input("Insira o ID da Tarefa: ")
                if id.isdigit():
                    tarefa_buscada = self.usuario_logado.procura_tarefa(int(id))
                    if tarefa_buscada:
                        tarefa.buscada.concluir_tarefa()
                    else:
                        print("Tarefa não encontrada")

            elif escolha == "6":
                id = input("Insira o ID da Tarefa: ")
                if id.isdigit():
                    tarefa_buscada = self.usuario_logado.procura_tarefa(int(id))
                    if tarefa_buscada:
                        novo_titulo = input("Insira novo titulo: ")
                        nova_descricao = input("Insira nova descricao: ")
                        nova_prioridade = input("Insira nova prioridade? ")
                        tarefa_buscada.editar_tarefa(novo_titulo, nova_descricao, nova_prioridade)

                    else:
                        print("Tarefa não encontrada")
                    
            elif escolha == "7":
                id = input("Insira o ID da Tarefa: ")
                if id.isdigit():
                    tarefa_buscada = self.usuario_logado.remover_tarefa(int(id))

            elif escolha == "8":
                self.usuario_logado.limpar_concluida()

teste = Sistema()
teste.menu_principal()


