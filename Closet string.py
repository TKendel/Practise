lista=[]
pocetak=[]
zbroj_promjena=[]
zbroj=[]
broj_dna=0

#kreiranje liste sa svim zadanim stringovima
file=open("DNA.txt","r")
while True:
    dna=file.readline()
    if dna!='stop\n':
        dna=dna.replace('\n','')
        lista.append(dna)
        broj_dna=broj_dna+1
    else:
        break
file.close()
print(lista)

#lista za pomoc u zbrajanu svih zasebnih promjena
for x in range(broj_dna):
    pocetak.append(x)

#usporedivanje stringova
for glavni in range(0,broj_dna):
    prvi=lista[glavni]
    print(30*'-')
    for sekundarni in range(0,broj_dna):
        brojac=0
        drugi=lista[sekundarni]
        for slovo in range(len(prvi)):
            if prvi[slovo]!=drugi[slovo]:
                brojac=brojac+1
        print(brojac)
        zbroj_promjena.append(brojac)

#zbrajanje svih zasebnih promjena
for pocetni in range(len(pocetak)):
    pocetni_broj=pocetni
    suma=0
    for i in range(pocetni_broj,len(zbroj_promjena),broj_dna):
        suma=zbroj_promjena[i]+suma
    zbroj.append(suma)

#biranje najslicnjieg stringa
print(30*'-')
najmanji=min(zbroj)
pokazatelj=zbroj.index(najmanji)
print("najslicniji string njima svima je: ",lista[pokazatelj])





    

