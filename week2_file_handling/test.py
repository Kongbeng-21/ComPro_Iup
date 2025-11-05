data=[]
with open("scores.txt",'r')as f:
    for line in f:
        name,score = line.strip().split(",")
        data.append((name,int(score)) )   

topnm,topsc = max(data,key=lambda s: s[1])
 
avg = sum(i for i,j in data) / len (data)
      
print(topnm,topsc)

