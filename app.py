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
 
 nome = input("Nome: ")

  if nome == "":
     print("Erro")
     return

  with open("dados/users.txt" , "a") as f:
     f.write(nome +"\n")
       
  print("Guardado")

def listar():
 
  with open("dados/users.txt" , "r") as f:
     funcionarios  = f.readlines() 
    
  if len(funcionarios) == 0:
     print("Sem funcionários")
     return

  for i, funcionario in enumerate (funcionarios, 1):
     print(i, "-", funcionario.strip())
       
def apagar():
  
  with open("dados/users.txt" , "r") as f:
     funcionarios  = f.readlines()
  
  if len(funcionarios) == 0:
     print("Sem funcionários")
     return
  
  for i, funcionario in enumerate (funcionarios, 1):
     print(i, "-", funcionario.strip())

  escolha = input("Nome do funcionário: ")
  
  if not escolha.isdigit():
      print("Número inválido")
      return
  
  indice = int(escolha) - 1

  if indice < 0 or indice >= len(funcionarios):
        print("Fora da lista")
        return
  

  funcionarios.pop(indice)
 
  with open("dados/user.txt", "w") as f:
        for c in funcionarios:
            f.write(c)

  print("funcionário removido")

def sair():
  print("Adeus")

while True:
  print("\n1 - Adicionar funcionário")
  print("2 - Listar funcionários")
  print("3 - Apagar funcionário")
  print("4 - Sair")
  
  op = input("Escolha:")

  if op == "1": 
    adicionar()
  
  elif op == "2":
    listar()

  elif op == "3":
    apagar()

  elif op == "4":
    sair()
    break

  else:
    print("Opção inválida:")
  


