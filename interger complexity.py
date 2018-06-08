#Given a number A, find the smallest possible value of B+C, if B*C = A. Here A, B, and C must all be positive integers. 
#It's okay to use brute force by checking every possible value of B and C. 
#You don't need to handle inputs larger than six digits. Post the return value for A = 345678 along with your solution.


div=0
djeljitelj=[]
lista_b=[]
lista_c=[]
zbroj=[]
broj=int(input("unesite broj: "))
for i in range(1,100):
    djeljitelj.append(i)
for i in range(len(djeljitelj)):
    if broj%djeljitelj[i]==0:
        lista_c.append(djeljitelj[i])
        div=broj/djeljitelj[i]
        lista_b.append(div)
for i in range(len(lista_b)):
    zbroj.append(lista_b[i]+lista_c[i])
print(min(zbroj))

       
        
