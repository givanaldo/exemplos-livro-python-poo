class Conta:
    def __init__(self, numero, saldo, clientes):
        self.numero = numero
        self.saldo = saldo
        self.clientes = clientes

    def exibirSaldo(self):
        print('\nConta: %d ' % self.numero)
        print('Cliente(s): ', end='')
        if type(self.clientes) is list:
            for cliente in self.clientes:
                print('%s | ' % cliente.nome, end='')
        else:
            print(self.clientes.nome, end=' | ')
        print('Saldo: R$ %.2f' % self.saldo)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

