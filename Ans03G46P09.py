n = int(input("Enter the number of people crossing the bridge:"))
x = list(int(num) for num in input("Enter timings for each person:").strip().split(","))[:n]
d=0
sum=0
try:
      for i,m in enumerate(x):
            print("person ",i,"timings ",m)
            
            if(m>d):
                 sum=sum+m
            elif(m<d):
                  raise ValueError("person ",i+1, "timings must be greater than",i)
            d=m
      print("total timings for each person crossing bridge is:",(sum-x[0]))
            
except ValueError as e:
                  print("error is",e)                  
       
except:
      print(e)


