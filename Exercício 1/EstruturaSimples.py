#Este código serve para trocar os valores das variáveis a por b, caso a seja maior que b
A = input("Informe um valor para a variável A:")
B = input("Informe um valor para a variável B:")

if(A>B):
    aux = A;
    A=B;
    B = aux;
    
print("O valor da variável A agora é: ", A)
print("O valor da variável B agora é: ", B)