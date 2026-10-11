from .cliente import Cliente
from .conta import Conta
from .excecoes import ContaNaoEncontradaError


class Banco:
    def __init__(self):
        self._contas = {}
        self._sequencia = 1

    def _proximo_numero(self):
        numero = f"{self._sequencia:04d}"
        self._sequencia += 1
        return numero

    def abrir_conta(self, cliente: Cliente):
        conta = Conta(self._proximo_numero(), cliente)
        self._contas[conta.numero] = conta
        return conta

    def buscar(self, numero):
        if numero not in self._contas:
            raise ContaNaoEncontradaError(numero)
        return self._contas[numero]

    def transferir(self, origem, destino, valor):
        o = self.buscar(origem)
        d = self.buscar(destino)
        o.debitar(valor, "TRANSF. ENVIADA")
        d.creditar(valor, "TRANSF. RECEBIDA")