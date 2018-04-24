lista=[]
dodatak=''
tabla=[]
encrypt=''

#input poruka i keyword
poruka=input("unesite tekst: ")
poruka=poruka.replace(' ','')
while True:
    keyword=input("unesite keyword: ")
    if len(keyword)<len(poruka):
        puta=len(poruka)//len(keyword)
        ostatak=len(poruka)%len(keyword)
        print(puta)
        print(ostatak)
        break
    else:
        print('keyword mora biti manji nego poruka')
if ostatak==0:
    keyword=keyword*puta
else:
    for i in range(ostatak):
        dodatak=dodatak+keyword[i]
    keyword=keyword*puta+dodatak
print(keyword)




#tablica cyphera
cypher=open('cypher.txt','r')
while True:
    row=cypher.readline()
    if row!='stop':
        row=row.replace('\n','')
        razdvojeno=list(row)
        lista.append(razdvojeno)
    else:
        break
cypher.close()


#kodiranje
for j in range(len(keyword)):
    slovo_k=lista[0].index(keyword[j])
    slovo_p=lista[0].index(poruka[j])
    n_slovo=lista[slovo_k][slovo_p] #ovo su brojke :)
    encrypt=encrypt+n_slovo
print(encrypt)



