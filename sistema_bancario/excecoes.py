class ValorInvalidoError(Exception):
    """Valor de operação inválido (zero, negativo ou não numérico)."""


class SaldoInsuficienteError(Exception):
    """Saldo insuficiente para a operação."""


class ContaNaoEncontradaError(Exception):
    """Número de conta inexistente no banco."""

    def __init__(self, numero):
        super().__init__(f"Conta não encontrada: {numero}")