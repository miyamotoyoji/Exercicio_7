    # Roteiro de Testes – Sistema Bancário (Lab 6.1)

Execução: `python -m unittest discover -s tests -t . -v`

| ID | Tipo | Classe de teste | Entrada / ação | Resultado esperado | Status |
|---|---|---|---|---|---|
| CT01 | Unitário | TestConta | `depositar(100)` em conta vazia | Saldo = 100.00 | Passou |
| CT02 | Unitário | TestConta | `depositar(100)`; `sacar(40)` | Saldo = 60.00 | Passou |
| CT03 | Unitário | TestConta | Saldo 100; `sacar(200)` | `SaldoInsuficienteError`; saldo continua 100.00 | Passou |
| CT04 | Unitário | TestConta | `depositar(-50)`; `depositar(0)` | `ValorInvalidoError` | Passou |
| CT05 | Unitário | TestConta | `depositar(100)`; `sacar(30)` | Extrato: `DEPOSITO +100.00`, `SAQUE -30.00` | Passou |
| CT06 | Integração | TestBancoIntegracao | Abrir 2 contas no Banco e buscar | Números distintos; busca retorna a mesma conta | Passou |
| CT07 | Integração | TestBancoIntegracao | Transferir 150 de Ana (500) para Bruno | Ana 350.00; Bruno 150.00; extratos atualizados | Passou |
| CT08 | Integração | TestBancoIntegracao | Transferir 900 com saldo 500 | Exceção; nenhum saldo muda | Passou |
| CT09 | Integração | TestBancoIntegracao | Transferir para conta "9999" (inexistente) | `ContaNaoEncontradaError`; origem intacta | Passou |
| CT10 | Funcional | TestFluxoFuncional | Criar 2 contas, depositar 500, sacar 100, transferir 150, extratos | Mensagens corretas; saldos 250.00 e 150.00 | Passou |
| CT11 | Funcional | TestFluxoFuncional | Saque de 50 em conta vazia pelo menu | "Erro: Saldo insuficiente"; sistema continua | Passou |

Total: 11 casos, 11 aprovados, 0 falhas.