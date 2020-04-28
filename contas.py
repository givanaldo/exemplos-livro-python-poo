class Conta:
    def __init__(self, numero, saldo, cliente):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente

    def exibirSaldo(self):
        print('Conta: %d || ' % self.numero, end='')
        print('Cliente: %s' % self.cliente.nome)
        print('Saldo: R$ %.2f \n' % self.saldo)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor