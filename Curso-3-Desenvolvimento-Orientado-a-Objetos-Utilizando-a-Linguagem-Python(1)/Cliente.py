class Cliente:
    #a palavra pass é utilizada somente quando nenhuma estrutura será definida no corpo dessa classe.
    #o init é um metodo especial utilizado sempre que criamos um objeto da classe
    
    def __init__(self, n, fone):
        
        self.nome = n
        self.telefone = fone