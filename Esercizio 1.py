def fattoriale (num):
    for i in range(1, num+1):
        num =  num * i
    return num

numero = int(input("Inserisci un numero:"))
print("Il fattoriale del numero", numero, "e", fattoriale(numero))