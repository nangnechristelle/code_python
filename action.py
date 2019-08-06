import random as ran
def seq_alea(n):
    base=["A","C","G","T"]
    li=[]
    reponse=input('entrer un nombre')
    n=int(reponse)
    i=0
    while i<n:
        li.append(ran.choice(base))
        i=i+1
    return(li)
print(seq_alea(15))
