from .banco import Banco
from .cliente import Cliente


class App:
    """Menu de console. `entrada` e `saida` podem ser trocadas nos testes funcionais."""

    def __init__(self, banco=None, entrada=input, saida=print):
        self.banco = banco or Banco()
        self.entrada = entrada
        self.saida = saida

    def menu(self):
        self.saida("1-Criar conta 2-Depositar 3-Sacar 4-Transferir 5-Extrato 0-Sair")

    def ler(self, prompt):
        try:
            return self.entrada(prompt).strip()
        except (EOFError, StopIteration):
            return "0"

    def executar(self):
        while True:
            self.menu()
            opcao = self.ler("Opção: ")
            if opcao == "0":
                self.saida("Até logo!")
                return
            try:
                if not self.tratar(opcao):
                    self.saida("Erro: opção inválida")
            except Exception as e:  # erros de negócio viram mensagem
                self.saida(f"Erro: {e}")

    def tratar(self, opcao):
        if opcao == "1":
            c = self.banco.abrir_conta(Cliente(self.ler("Nome: ")))
            self.saida(f"Conta criada: {c.numero} ({c.titular.nome})")
        elif opcao == "2":
            c = self.banco.buscar(self.ler("Conta: "))
            c.depositar(self.ler("Valor: "))
            self.saida(f"Depósito realizado. Saldo: {c.saldo}")
        elif opcao == "3":
            c = self.banco.buscar(self.ler("Conta: "))
            c.sacar(self.ler("Valor: "))
            self.saida(f"Saque realizado. Saldo: {c.saldo}")
        elif opcao == "4":
            origem, destino = self.ler("Origem: "), self.ler("Destino: ")
            self.banco.transferir(origem, destino, self.ler("Valor: "))
            self.saida("Transferência realizada.")
        elif opcao == "5":
            c = self.banco.buscar(self.ler("Conta: "))
            self.saida(f"Extrato da conta {c.numero}:")
            for linha in c.extrato:
                self.saida(linha)
            self.saida(f"Saldo: {c.saldo}")
        else:
            return False
        return True