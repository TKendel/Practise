from random import randint
import sys
l=["0","1","2","3","4","5","6","7","8","9"]
l2=["nula","jedan","dva","tri","cetiri","pet","sest","sedam","osam","devet"]
dodatak="naest"
dvadeset="dvadeset"
tri="trideset"
cetiri="ceterdeset"
pet="pedeset"
sest="sezdeset"
sati=input("unesite koliko je sati :")
minute=input("unesite koliko je minuta: ")
vrijeme=sati+":"+minute
print(vrijeme)
####sati####
if sati=='00':
    print('ponoc'+":"+minute)
#sys.exit()

if int(sati)<10 and int(sati)>=1:
    counter=int(sati)%10
    if str(counter) in l:
        if sati[0]=='0':
            sati=sati.replace(sati[0],'')
            sati=sati.replace(sati[0],l2[counter])
    print(sati+":"+minute)
elif int(sati)>=10 and int(sati)<=19:
    jedinica=int(sati)%10
    if str(jedinica) in l:
        sati=sati.replace(sati[1],dodatak)
        sati=sati.replace(sati[0],l2[jedinica])
    print(sati+":"+minute)
elif int(sati)>19 and int(sati)<21:
    print(dvadeset+":"+minute)
elif int(sati)>20 and int(sati)<24:
    jedinica=int(sati)%10
    print(sati)
    if str(jedinica) in l:
        sati=sati.replace(sati[0],l2[jedinica])
        sati=sati.replace(sati[0],dvadeset)
    print(sati+":"+minute)
####minute####
if int(minute)<10 and int(minute)>=1:
    brojac=int(minute)%10
    if str(brojac) in l:
        if minute[0]=='0':
            minute=minute.replace(minute[0],'')
            minute=minute.replace(minute[0],l2[brojac])
    print(sati+":"+minute)
elif int(minute)>9 and int(minute)<20:
    brojac=int(minute)%10
    if str(brojac) in l:
        minute=minute.replace(minute[1],dodatak)
        minute=minute.replace(minute[0],l2[brojac])
    print(sati+":"+minute)
elif int(minute)>19 and int(minute)<21:
    print(sati+":"+dvadeset)
elif int(minute)>20 and int(minute)<30:
    brojac=int(minute)%10
    if str(brojac) in l:
        minute=minute.replace(minute[1],l2[brojac])
        minute=minute.replace(minute[0],dvadeset+' ')
    print(sati+":"+minute)
elif int(minute)>29 and int(minute)<31:
    print(sati+":"+tri)
elif int(minute)>30 and int(minute)<40:
    brojac=int(minute)%10
    if str(brojac) in l:
        minute=minute.replace(minute[1],l2[brojac])
        minute=minute.replace(minute[0],tri+' ')
    print(sati+":"+minute)
elif int(minute)>39 and int(minute)<41:
    print(sati+":"+cetiri)
elif int(minute)>40 and int(minute)<50:
    brojac=int(minute)%10
    if str(brojac) in l:
        minute=minute.replace(minute[1],l2[brojac])
        minute=minute.replace(minute[0],cetiri+' ')
    print(sati+":"+minute)
elif int(minute)>49 and int(minute)<51:
    print(sati+":"+pet)
elif int(minute)>50 and int(minute)<60:
    brojac=int(minute)%10
    if str(brojac) in l:
        minute=minute.replace(minute[1],l2[brojac])
        minute=minute.replace(minute[0],pet+' ')
    print(sati+":"+minute)
elif int(minute)>59 and int(minute)<61:
    print(sati+":"+sest)
else:
    print("krivi unos")
print("trenutno je",sati,"sati","i",minute,"minuta")







            
