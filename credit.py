#Função que faz o algoritmo de Luhn
def Validacao(n):
  nlist = [int(a) for a in str(n)]
  rlist = nlist
  rlist.reverse()
  soma_par = 0
  for i in list(rlist)[1::2]:
      if i * 2 > 9:
        soma_par += i * 2 - 9
      else:
        soma_par += i * 2
  soma_total = soma_par
  for i in list(rlist)[::2]:
    soma_total += i
  if soma_total % 10 == 0:
    return True
  else:
    return False

#Função para definir a bandeira do cartão, ou se ele é invalido
def Bandeira(n):
  nlist = [int(a) for a in str(n)]
  if Validacao(n) == True:
    if (nlist[0] == 4) and (len(nlist) in [13,16]):
      print('VISA\n')
    elif (nlist[0] == 3) and (nlist[1] == 4 or 7) and (len(nlist) == 15):
      print("AMEX\n")
    elif (nlist[0] == 5) and (nlist[1] == 1 or 2 or 3 or 4 or 5) and (len(nlist) == 16):
      print('MASTERCARD\n')
    else:
      print('INVALIDO\n')
  else:
    print('INVALIDO\n')

#Programa principal + tratamento de erro
while True:
  numero = input('Digite o numero do cartao, com apenas numeros (sem espaço, e/ou outros caracteres):\n')
  if numero.isdigit() == False:
    print('Numero invalido\n')
  else:
    n = int(numero)
    Validacao(n)
    Bandeira(n)
    break
