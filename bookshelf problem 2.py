#Description
#You have an enormous book collection and want to buy some shelfs. 
#You go to a bookshelfstore and they sell all kinds of shelfs. 
#The wierd part is, some shelfs are different in length but they all cost the same.
#You now want to puzzle your collection so that you can fit as many books on the least number of shelfs


sve_knjiga=[]
v_knjige=[]
x=0
a=0
suma=0
p=0

#izvlacanje svih ponudenih velicina polica
file=open('bs2.txt','r')
shelf=file.readline()
shelf=shelf.replace('\n','')
shelf=shelf.split(' ')
shelf=list(map(int,shelf))



#izvlacenje knjiga
while True:
    knjiga=file.readline()
    knjiga=knjiga.replace('\n','')
    if knjiga!='stop':
        
        sve_knjiga.append(knjiga.split(' '))
    else:
        break


#izvlacenje samo velicina knjiga
for i in range(len(sve_knjiga)):
    v_knjige.append(sve_knjiga[i][0])
    v_knjige=list(map(int,v_knjige))  #pvo u map() zadam func koja djeluje na sve podatke u ovom slucaju
    v_knjige.sort()
    v_knjige.reverse()
file.close()                #v_knjige koji je inicjalno bio str. list je sam te podatke opet stavlja u listu
 


def potraga(shelf,v_knjige):
    koristene_knjige=[]
    razlika1=0
    police=shelf
    knjige=v_knjige
    if not knjige:
        a="kraj"
        return a
    naj_p=max(police)
    print("max v p",naj_p)
    police.remove(naj_p)
    naj_k=max(knjige)
    koristene_knjige.append(naj_k)
    knjige.remove(naj_k)
    print("max v k",naj_k)
    while naj_k<naj_p:
        print("prvi puta")
        razlika1=naj_p-naj_k
        print("razlika1:",razlika1)
        for j in range (1):
            if not knjige:
                print("prazna lista")
                print("to je sve za policu",naj_p,"\nKnjige koristene su", koristene_knjige)
                naj_k=naj_k+razlika1
                break
            elif knjige[j]<=razlika1:
                dodatak1=knjige[j]
                koristene_knjige.append(dodatak1) #realno bi mogo pop korstiti da mi izebrise
                print("dodatak1",dodatak1) #iz tablice i zapise sto je obirsao u isto vrijeme
                knjige.remove(dodatak1) #da druga funk ne uzem opet isti broj
                knjige.sort()
                knjige.reverse()
                print(knjige)
                nova_v_knjige=naj_k+dodatak1
                print("nova_v_knjige",nova_v_knjige)
                print(50*"-")
                naj_k=naj_k+dodatak1
            else:
                print(60*"*")
                print("to je sve za policu",naj_p,"\nKnjige koristene su", koristene_knjige)
                naj_k=naj_k+razlika1
                print(naj_k)
                print(60*"*")
                print(60*"-")
                break
    return potraga(police,knjige)


print(potraga(shelf,v_knjige))
