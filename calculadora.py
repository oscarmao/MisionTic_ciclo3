

print("calculadora ejemplo")
print()
print("1). SUMAR")

def sumar(n1,n2):
    return n1+n2

op=int(input("digite una opcion: "))
n1=int(input("digite el numero: "))
n2=int(input("Digite el numero 2: "))
res=None
if op==1:
    res=sumar(n1,n2)
    
print("el resultado  de la suma es: ", res)