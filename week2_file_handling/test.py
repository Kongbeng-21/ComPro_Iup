data=[]
with open("scores.txt",'r')as f:
    for line in f:
        name,score = line.strip().split(",")
        data.append((name,int(score)) )   

topnm,topsc = max(data,key=lambda s: s[1])
 
    
print(topnm,topsc)

