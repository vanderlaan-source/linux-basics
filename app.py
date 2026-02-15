def adicionar():
  nome = input("Nome:")

  if nome == "":
    print("Não digitou nada")
    return
  with open("dados/users.txt", "a") as f:
    f.write(nome + "\n")
  print("Guardado")

def listar():
 with open("dados/users.txt", "r") as f:
  for linha in f:
    print("-", linha.strip())

while True:
    print("\n1 - Adicionar")
    print("2 - Listar")
    print("3 - Sair")

    op = input("Escolha: ")


    if op == "1":
        adicionar()
 
    elif op == "2":
        listar()

    elif op == "3":
        print("Adeus")
        break

    else:
        print("Opção inválida")
