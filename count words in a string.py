dad=open("words.txt","r")
a=dad.read()
print(a)
a=a.replace("\n"," ")
a=a.replace("."," ")
print("-"*60)
b=a.split(" ")
b=list(filter(None,b)) #filter napravi bolean filter gdje u ovom slucaju ako je 
print(b)                #nesto none u listi b izbrisi
print("postoje",len(b),"rijeci")
dad.close()
 

