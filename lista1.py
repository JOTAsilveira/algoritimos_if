import random

#1
a = []
cont = 2
for i in range (40):
    a.append (cont)
    cont += 2
print (a)


#2
for i in range (5):
    indice = int ( input ( "informe o valor do indice: "))
    valor = int ( input ( "informe o valor do valor: "))
    a[indice] = valor
print (a)



#3
#a
for i in range (5):
    ind = random.randint (0, 39)
    val = random.randint (2, 80)
    a[ind] = val
print ("lista alterada: ")
print (a)

#b
soma = 0
for i in a:
    soma += i
print (soma)

#c
for i in range(1, 40):
    if a[i] < a[i-1]:
        print ("o indice é:", i)

#4
n = int ( input ( "informe o número de membros da família"))
lista = []
for i in range (n):
    idade = int ( input ("informe a idade do membro:"))
    lista.append(idade)
print ("idades da família", lista)

s = 0
for i in lista:
    s += i
print ("a soma das idades da família é:", s)

#5
criança = 0
adulto = 0
idoso = 0

c = []
a = []
ido = []

for i in lista:
    if i <= 17:
        criança += 1
        c.append(i)
    if i >= 18:
        adulto += 1
        a.append(i)
    if i >= 60:
        idoso += 1
        ido.append(i)


print ("criança:", criança, "adulto:", adulto, "idoso:", idoso)
print ("criança:", c)
print ("adulto:", a)
print ("idoso:", ido)


#extra

a = []
cont = 1
pos = 0
for i in range (40):
    a.append (cont)
    cont += 1

print ("casas coringa:")
for i in range (5):
    coringa = random.randint(1, 40)
    print(coringa)

print ("tabuleiro:", a)
print ("você está na casa 1")


dado = random.randint(1, 6)
print ("o valor do dado 1 foi:", dado)
pos += dado
if pos == coringa:
    print ("você voltou pra casa 0")
    pos == 0
else:
    print ("você está na casa", pos)
dado = random.randint(1, 6)



dado = random.randint(1, 6)
pos += dado
print ("o valor do dado 2 foi:", dado)
if pos== coringa:
    print ("você voltou pra casa 0")
    pos == 0
else:
    print ("você está na casa", pos)
dado = random.randint(1, 6)




dado = random.randint(1, 6)
pos += dado
print ("o valor do dado 2 foi:", dado)
if pos == coringa:
    print ("você voltou pra casa 0")
    pos == 0
else:
    print ("você está na casa", pos)
dado = random.randint(1, 6)
