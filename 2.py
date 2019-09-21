def largest_word(a):
    b=[]
    for i in range(0,len(a)-1):
        if len(a[i])<len(a[i+1]) and len(b)<len(a[i+1]):
            b=a[i+1]
        elif len(a[i+1])<len(a[i]) and len(b)<len(a[i]):
            b=a[i]   
    return b
l=["hello","dude","!","what's","up","?"]
print("largest_word(",l,")")
x=largest_word(l)
print("The largest string is ",x)