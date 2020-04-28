class Conta:
    def __init__(self, numero, saldo, clientes):
        self.numero = numero
        self.saldo = saldo
        self.clientes = clientes

    def exibeSaldo(self):
        print('Cliente(s): ', end='')
        if type(self.clientes) == 'list':
            for cliente in self.clientes:
                print('%s | ' % cliente.nome, end='')
        else:
            print(self.clientes.nome, end='')
        print('\nConta: %d ' % self.numero)
        print('Saldo: R$ %.2f' % self.saldo)

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def deposito(self, valor):
        self.saldo += valor