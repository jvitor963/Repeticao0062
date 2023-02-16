# Menu com contadores while e for
op = 0 # para entrar no laço
while (op !=3):
    print("\nEscolha o tipo de contador que você deseja:")
    print("1 - Contador progressivo")
    print("2 - Contador regressivo")
    print("3 - encerrar")
    print("-" * 50)
    op = int(input("? "))
    if op == 1:
        for x in range(1,11):
            print(x, end=" ")
    elif op ==2:
        for x in range(10,0,-1):
            print(x, end=" ")
    elif op ==3:
        print ("Programa encerrado pelo usuário!")
        break
