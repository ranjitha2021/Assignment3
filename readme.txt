n=int(input("enter a n number of people crossing the bridge:"))
d=0
sum=0
li=[]
print("enter the time for each people for crossing the bridge:")
try:
    for i in range(n):
        a=int(input(""))       
        if(i==0):
            first=a
        
        if(i>0 and a<d):
            raise ValueError("person",i+1," timings must be greater than person",i )
        else:   
            sum=sum+a
            li.append(a)
        d=a    
    print(li)
    sum=sum-first
    print("total timings for each person crossing bridge is:",sum)
except ValueError as e:
    print(e)
except:
    print("error in the program")
