def generator_kodu(a, b):
    a2 = a.split("-")
    b2 = b.split("-")
    c = []
    d = []
    for i in range(0, len(a2)):
        a2[i] = int(a2[i])
    for i in range(0, len(b2)):
        b2[i] = int(b2[i])
    if a2[0] < b2[0]:
        if a2[1] < 1000:
            y = a2[1]
            while y < 999:
                y = y + 1
                c.append("{:03d}".format(y))
                d.append(a2[0])
        a2[0] = a2[0] + 1
        a2[1] = 0
    if a2[0] == b2[0]:
        if a2[1] < 1000:
            y = a2[1]
            while y < 999 and y < b2[1]-1:
                y = y + 1
                c.append("{:03d}".format(y))
                d.append(a2[0])
    print("Generator kodów pocztowych:")
    for i in range(0, len(d)):
        print(d[i], "-", c[i])

def elementy_listy(porownanie,n):
    lista = []
    licznik = 1
    for i in range(0, n):
        lista.append(licznik)
        licznik = licznik + 1
    print("wejscie",porownanie, n)
    lista2 = lista
    for i in range(0, len(porownanie)):
        lista2.remove(porownanie[i])
    print("wyjscie",lista2)

def generacja_liczb(x,y):
    lista = []
    x = float(x)
    while x <= y:
        lista.append(x)
        x = x +0.5
    print("Wygenerowana lista",lista)

a = "79-900"
b = "80-155"
generator_kodu(a, b)

lista_p =[2,3,7,4,9]
n = 10

elementy_listy(lista_p, n)
x = 2
y = 5.5
generacja_liczb(x, y)



