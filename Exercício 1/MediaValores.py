#o usuário digita vários valores reais positivos.Todos estes números devem ser somados e, 
# quando for digitado algum número negativo, o laço de repetição deverá encerrar e, na sequência, 
# exibir a média dos valores digitados.

qtd =0
soma =0
media =0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    #entrada de valores
    valor = float(input("Digite um valor: "))
    
#caso digite um valor negaivo o laço encerra
media = soma/qtd
print("\n Total da soma: ", soma)
print("\n Quantidade de valores digitados: ", qtd)
print("\n Média dos valores: ", media)