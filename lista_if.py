#1
for i in range (1, 51, 1):
    print (i)

#2
for i in range (100, 0, -1):
    print (i)

#3
n = int ( input ( ))
for i in range (1, n, 1):
    if i % 2 == 0:
        print (i) 

#4
it = 0
n = int ( input( ))
for i in range (0, n+1):
    it += i
print (it)

#5
it = 0
np = int ( input ())
for i in range (0, np, 1):
    idade = int ( input ("informe a idade: "))
    it = it + idade
m = it / np
print (m)

#6
s = 0
m = 0
for i in range (1, 6, 1):
    n = int ( input ( ))
    if n > 10 and n < 20:
        s += 1
    if n < 10 or n > 20:
        m += 1
print (s, "números estão no intervalo")
print (m, "números não estão no intervalo")

#7
print ("OPERAÇÃO - SUBTRAÇÃO!")
for i in range (1, 4, 1):
    print ("============================")
    print ("conta", i, "!")
    n1 = int ( input ( "Digite o primeiro número: "))
    n2 = int ( input ( "Digite o outro número: "))
    s = n1 - n2
    print (n1, "-", n2, "=", s)
    i += 1

#8
print ("TABUADAS!")
a = 0
while a == 0:
    resposta = input ( "deseja ver uma tabuada?")
    if resposta == "S":
        n = int ( input ( "Tabuada de: "))
        for i in range (1, 11, 1):
            resultado = n * i
            print (n, "x", i, "=", resultado)
    if resposta == "N":
        break
'''
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
for i in range (10):
    voto = input ( )
    if voto == "1":
        a += 1
    elif voto == "2":
        b += 1
    elif voto == "3": 
        c += 1
    elif voto == "4":
        d += 1
    elif voto == "5":
        e += 1
    elif voto == "6":
        f += 1
print ("o candidato 1 teve", a, "votos")
print ("o candidato 2 teve", b, "votos")
print ("o candidato 3 teve", c, "votos")
print ("o candidato 4 teve", d, "votos")
print ("Total de votos nulos: ", e)
print ("Total de em branco: ", f)
