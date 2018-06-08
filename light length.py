#Description
#There is a light in a room which lights up only when someone is in the room (think motion detector). 
#You are given a set of intervals in entrance and exit times as single integers, and expected to find how long the light
#has been on. When the times overlap, you need to find the time between the smallest and the biggest numbers in that interval.

#unos zauzetog vremena
l_ulaz=[]
l_izlaz=[]
rez_ulaza=[]
rez_izlaza=[]
while True:
    ulaz=int(input("unesite kad ste usli:"))
    if ulaz==0:
        break
    else:
        l_ulaz.append(ulaz)
    izlaz=int(input("unesite kad ste izasli:"))
    if izlaz==0:
        break
    else:
        l_izlaz.append(izlaz)
#funkcija za analizu vremena

def duljina_svjetla(l_ulaz,l_izlaz):
    if not l_ulaz:
        a="kraj"
        return a
    koristeno1=[]
    koristeno2=[]
    najmanji=l_ulaz[0]
    najveci=l_izlaz[0]
    for i in range(len(l_ulaz)):
        if l_izlaz[i]>=najmanji and l_izlaz[i]<=najveci or l_ulaz[i]>=najmanji and l_ulaz[i]<=najveci:
            if l_ulaz[i]<najmanji:
                najmanji=l_ulaz[i]
                koristeno1.append(najmanji)
                koristeno2.append(l_izlaz[i])
            if najmanji==l_ulaz[i] and najveci==l_izlaz[i]:
                koristeno1.append(najmanji)
                koristeno2.append(najveci)
            if l_ulaz[i]>=najmanji and l_izlaz[i]<=najveci:
                koristeno1.append(l_ulaz[i])
                koristeno2.append(l_izlaz[i])
            if l_izlaz[i]>najveci:
                najveci=l_izlaz[i]
                koristeno1.append(l_ulaz[i])
                koristeno2.append(najveci)
            print(najmanji)
            print(najveci)
    print("ispis")
    print(l_ulaz)
    print(l_izlaz)
    print(60*"-")
    rez_ulaza.append(najmanji) 
    rez_izlaza.append(najveci)
    for j in range(len(koristeno1)):
        if koristeno1[j] in l_ulaz:
            l_ulaz.remove(koristeno1[j])
        if koristeno2[j] in l_izlaz:		#radi..
            l_izlaz.remove(koristeno2[j])
    print(koristeno1)
    print(koristeno2)
    print(60*"-")
    print(l_ulaz)
    print(l_izlaz)
    print(60*"-")
    print("kraj jednog ispisa")
    return duljina_svjetla(l_ulaz,l_izlaz)

print(duljina_svjetla(l_ulaz,l_izlaz))
rj=0
for i in range(len(rez_ulaza)):
	razlika=0
	razlika=rez_izlaza[i]-rez_ulaza[i]
	rj=rj+razlika




'''    #ovo radi dolje kak se spada, samo treba zbrojiti koliko je zauzeto ukupno iz rez_u i rez_i
najmanji=l_ulaz[0]
najveci=l_izlaz[0]
for i in range (len(l_ulaz)):
    if l_izlaz[i]>=najmanji and l_izlaz[i]<=najveci or l_ulaz[i]>=najmanji and l_ulaz[i]<=najveci:
        if l_ulaz[i]<najmanji:
            najmanji=l_ulaz[i]
        elif l_izlaz[i]>najveci:
            najveci=l_izlaz[i]
    else:
        dl_ulaz.append(l_ulaz[i]) #prvi prolaz
        dl_izlaz.append(l_izlaz[i])
rez_ulaza.append(najmanji) #prvi rez
rez_izlaza.append(najveci)


d_najmanji=dl_ulaz[0]
d_najveci=dl_izlaz[0]
for i in range(len(dl_ulaz)):
    if dl_izlaz[i]>=d_najmanji and dl_izlaz[i]<=d_najveci or dl_ulaz[i]>=d_najmanji and dl_ulaz[i]<=d_najveci:
        if dl_ulaz[i]<d_najmanji:
            d_najmanji=dl_ulaz[i]
        elif dl_izlaz[i]>d_najveci:
            d_najveci=dl_izlaz[i]
    else:
        tl_ulaz.append(dl_ulaz[i]) #prvi prolaz
        tl_izlaz.append(dl_izlaz[i])
rez_ulaza.append(d_najmanji) #prvi rez
rez_izlaza.append(d_najveci)


t_najmanji=tl_ulaz[0]
t_najveci=tl_izlaz[0]
for i in range(len(tl_ulaz)):
    if tl_izlaz[i]>=t_najmanji and tl_izlaz[i]<=t_najveci or tl_ulaz[i]>=t_najmanji and tl_ulaz[i]<=t_najveci:
        if tl_ulaz[i]<t_najmanji:
            t_najmanji=tl_ulaz[i]
        elif tl_izlaz[i]>t_najveci:
            t_najveci=tl_izlaz[i]
    else:
        cl_ulaz.append(tl_ulaz[i]) #prvi prolaz
        cl_izlaz.append(tl_izlaz[i])
rez_ulaza.append(t_najmanji) #prvi rez
rez_izlaza.append(t_najveci)
'''




















