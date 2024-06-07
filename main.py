import datetime

class ContaBancaria:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito de R$ {:.2f} realizado com sucesso.".format(valor))
            self.mostrar_saldo()
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print("Saque de R$ {:.2f} realizado com sucesso.".format(valor))
            self.mostrar_saldo()
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def mostrar_saldo(self):
        print("Saldo atual: R$ {:.2f}".format(self.saldo))
        print("Data da consulta:", datetime.datetime.now())

class Banco:
    def __init__(self):
        self.usuarios = {}

    def cadastrar_usuario(self, nome):
        if nome not in self.usuarios:
            self.usuarios[nome] = ContaBancaria(nome)
            print("Usuário {} cadastrado com sucesso.".format(nome))
        else:
            print("Usuário já cadastrado.")

    def deletar_usuario(self, nome):
        if nome in self.usuarios:
            del self.usuarios[nome]
            print("Usuário {} deletado com sucesso.".format(nome))
        else:
            print("Usuário não encontrado.")

    def entrar(self, nome):
        if nome in self.usuarios:
            return self.usuarios[nome]
        else:
            print("Usuário não encontrado.")
            return None

def main():
    banco = Banco()

    while True:
        print("\n=== Menu ===")
        print("1. Cadastrar usuário")
        print("2. Deletar usuário")
        print("3. Entrar no aplicativo")
        print("4. Sair do programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite seu nome: ")
            banco.cadastrar_usuario(nome)
        elif opcao == "2":
            nome = input("Digite seu nome: ")
            banco.deletar_usuario(nome)
        elif opcao == "3":
            nome = input("Digite seu nome: ")
            usuario = banco.entrar(nome)
            if usuario:
                while True:
                    print("\n=== Menu do usuário ===")
                    print("1. Consultar saldo")
                    print("2. Depositar")
                    print("3. Sacar")
                    print("4. Sair")

                    opcao_usuario = input("Escolha uma opção: ")

                    if opcao_usuario == "1":
                        usuario.mostrar_saldo()
                    elif opcao_usuario == "2":
                        valor = float(input("Digite o valor a depositar: "))
                        usuario.depositar(valor)
                    elif opcao_usuario == "3":
                        valor = float(input("Digite o valor a sacar: "))
                        usuario.sacar(valor)
                    elif opcao_usuario == "4":
                        break
                    else:
                        print("Opção inválida.")
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()


    


        
