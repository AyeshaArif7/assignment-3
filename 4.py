def cc(a):
    count1=0
    count2=0
    for i in a:
        if i.isupper() :
            count1=count1+1
        elif i.islower():
            count2=count2+1
    print("No. of Uppercase character: ",count1)
    print("No. of Lowercase Characters: ",count2)
string=input("Enter a string: ")
cc(string)