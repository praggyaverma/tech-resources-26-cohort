t=int(input())
L=[]
for x in range(t):
    n=int(input())
    for j in range(2,n):
        if n%j==0:
            L.append([n,"not prime"])
            break
    else:
        L.append([n,"prime"])


for k in L:
  print(k[1])
