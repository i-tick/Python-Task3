def A():
        n=int(input("enter size of array: "))
        l=list(map(int,input("enter elements: ").split()))
        c=[]

        flag=0
        le = 1
        for i in range(0,n-1):

            #print(l[i],l[i+1])
            if(l[i]*l[i+1]<0):
                le+=1
                #print(le)
                flag=1
            else:
                if(flag==1):
                    while(le>0):

                        c.append(le)
                        le-=1
                    le=1
                else:
                    c.append(1)

                flag=0
        if(flag==1):
            while (le > 0):
                c.append(le)
                le -= 1
        else:
            while(len(c)!=n):
                c.append(1)



        print("output: ",*c)
def B():
    n=int(input("enter number of movies:"))
    a=[]
    b=[]
    for i in range(n):
        a.append(int(input("L"+str(i+1)+":")))
        b.append(int(input("R"+str(i+1)+":")))
    index=0
    product=0
    rating=0
    for i in range(n):
        curr=a[i]*b[i]
        if curr>product:
            product=curr
            rating=b[i]
            index=i
        elif curr==product:
            if b[i]>rating:
                rating=b[i]
                index=i
    print("output:",index+1)

def C():
    n=int(input("enter size of array: "))
    l=list(map(int,input("enter elements: ").split()))
    a=l[0]
    i=1
    for i in range(n):
        if l[i]<a:
            a=l[i]
    l=[]
    l.append(a)
    print((n-1)*a)
    print(l)
A()
B()
C()
