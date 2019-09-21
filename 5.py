l=[]
for i in range(100,401):
    if i%2==0 and (i//10)%2==0 and (i//100)%2==0:
        l.append(i)
print(l)