num=int(input("Enter a number: "))
first=0
second=1
i=0
print(second," ",end='')
while i<num-1:
    third=first+second
    print(third," ",end='')
    first=second
    second=third
    i=i+1