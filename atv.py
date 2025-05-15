#class tarefa:
        
class Usuário:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Sistema:
    def __init__(self):
        self.lista_usuarios = []
        self.usuario_logado = None


    def cadastrar_usuario(self):
        nome = input("Digite um nome: ")
        emai = input("Digite um email: ")

        if"@" not in email:
            print("E-mail inválido! /n")
            return
        else:
            novo_usuario = Usuario (nome, email)
            self.lista_usuarios.append(novo_usuario)
            print("Usuario cadastrado com sucesso!")

    def login(self):
        email = input ("Entre com o email")
    
        for usuario in self.lista_usuarios:
            if usuario.email == email:
                self.usuario_logado = usuario
                print(f"Usuario logado: {self.usuario_logado.nome}")
            

        print("Usuario inexistente")

    def menu_principal(self):
        opcao_escolhida = ""
        while opcao_escolhida != "0":
            print("Menu - Escolha uma opção:")
            print("1. Cadastrar novo usuário")
            print("2. Fazer Login")
            print("0. Sair: /n")
            opcap_escolhida = input("Escolha: ")

            if opcao_escolhida == "1":
                self.cadastrar_usuario()
            elif opcao_escolhida == "2":
                self.login()    
            elif opcao_escolhida == "0":
                print("Saindo...")
            else:
                print("Opção invalida")


teste = Sistema()
teste.menu_principal()


