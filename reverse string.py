try:
    s=input("unesi nesto: ")
    a=-len(s)
    b=-1
    ls=[]
    ns=""
    while b>a-1:
        ls.append(s[b])
        b-=1
    rj=ns.join(ls) #koristis da spojis postojeci string ili listu o ovom slucaju sa
    print(rj)   #drugim postojecim stringom 
except:
    print("doslo je do pogreske!")
