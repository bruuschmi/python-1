from calculo import dividir


name = input("Qual seu nome? ")

print('\n')

print("Oi " + str(name) + ", vamos fazer alguns calculos!")

print('\n')

numero1 = input("Qual primeiro valor? ")
numero2 = input("Qual segundo valor?")

print('\n')
print(dividir(numero1, numero2))
