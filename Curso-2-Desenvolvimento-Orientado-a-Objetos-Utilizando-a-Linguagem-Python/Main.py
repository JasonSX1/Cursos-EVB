class Main:
    pass


from Cliente import Cliente

from Conta import Conta

c1 = Cliente("Geison", "77999999999")
conta=Conta(c1.nome, 6565, 0)


print(conta.titular, ", Número de conta: ", conta.numero, " Seu Saldo: ", conta.saldo)