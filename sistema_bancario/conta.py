from decimal import Decimal, InvalidOperation

from .excecoes import SaldoInsuficienteError, ValorInvalidoError

CENTAVOS = Decimal("0.01")


def para_decimal(valor):
    """Converte int/str/Decimal em Decimal com 2 casas; rejeita zero, negativos e lixo."""
    try:
        d = Decimal(str(valor)).quantize(CENTAVOS)
    except (InvalidOperation, ValueError):
        raise ValorInvalidoError("Valor deve ser positivo")
    if d <= 0:
        raise ValorInvalidoError("Valor deve ser positivo")
    return d


class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self._saldo = Decimal("0.00")
        self._extrato = []

    @property
    def saldo(self):
        return self._saldo

    @property
    def extrato(self):
        return list(self._extrato)

    def depositar(self, valor):
        self.creditar(valor, "DEPOSITO")

    def sacar(self, valor):
        self.debitar(valor, "SAQUE")

    def creditar(self, valor, descricao):
        v = para_decimal(valor)
        self._saldo += v
        self._extrato.append(f"{descricao} +{v}")

    def debitar(self, valor, descricao):
        v = para_decimal(valor)
        if self._saldo < v:
            raise SaldoInsuficienteError("Saldo insuficiente")
        self._saldo -= v
        self._extrato.append(f"{descricao} -{v}")