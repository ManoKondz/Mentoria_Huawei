# Entrada e Validação de entrada
# Nota da Prova 1
while True:
    nt1 = input("Entre com sua primeira nota da N1:\n")
    try:
        nt1 = float(nt1)
    except ValueError:
        print("Não é um número válido, Digite somente números válidos.")
    if type(nt1) == float:
        break
# Nota da Prova 2
while True:
    nt2 = input("Entre com sua segunda nota da N1:\n")
    try:
        nt2 = float(nt2)
    except ValueError:
        print("Não é um número válido, Digite somente números válidos.")
    if type(nt2) == float:
        break
# Nota da Prova 3
while True:
    nt3 = input("Entre com sua primeira nota da N2:\n")
    try:
        nt3 = float(nt3)
    except ValueError:
        print("Não é um número válido, Digite somente números válidos.")
    if type(nt3) == float:
        break
# Nota da Prova 4
while True:
    nt4 = input("Entre com sua segunda nota da N2:\n")
    try:
        nt4 = float(nt4)
    except ValueError:
        print("Não é um número válido, Digite somente números válidos.")
    if type(nt4) == float:
        break
# Calculo da média da N1
n1 = (nt1 + nt2) / 2 
print("Sua nota da n1 é:", n1)
# Calculo da média da N2
n2 = (nt3 + nt4) / 2 
print("Sua nota da n2 é:", n2)
# Calculo da Média Geral
MF = (2 * n1 + 3 * n2) / 5 
print("Média Final:", MF)
#Aprovação
if( MF >= 6):
  print("Parabéns, sua média é %s, logo, você está aprovado por média, agora verifique suas faltas." % (MF))
# Avaliação Final
elif MF <= 5.9 and MF > 2.9:
  print("sua média é %s, portanto, você está de AF" % (MF))
  af = input("Entre com sua nota da AF:\n")
  while True:
    try:
        af = float(af)
    except ValueError:
        print("Não é um número válido, Digite somente números válidos.")
    if type(af) == float:
        break
  maf = (MF + af) / 2
  if maf >= 5:
    print("Parabéns! Sua média final é %s, logo, você passou na AF." % (maf))
  else:
    print("Infelizmente sua média é %s, portanto, você está reprovado." % (maf))
# Reprovação
elif MF <= 2.9:
   print( "Sua média é %s, logo, você está reprovado." % (MF))