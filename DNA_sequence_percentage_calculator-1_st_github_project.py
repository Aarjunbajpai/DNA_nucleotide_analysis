dna=input("enter the dna sequence : ").upper()
q=dna.count('A')
w=dna.count('T')
e=dna.count('G')        
r=dna.count('C')
t=len(dna)
print("Adenine : ",q)
print("Thymine : ",w)
print("Guanine : ",e)   
print("Cytosine : ",r)
print("Total Nucleotides : ",len(dna))
x=((q+w)/t)*100
print("AT% : ",x)
y=((e+r)/t)*100   
print("GC% : ",y)

