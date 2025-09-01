al = ["c=","c-","dz=","d-","lj","nj","s=","z="]

str = input()
for a in al :
    str = str.replace(a,"0")
    
print(len(str))