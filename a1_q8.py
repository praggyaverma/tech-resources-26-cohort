n=int(input()) #number
k=int(input()) #rotation value
L=str(n)
if k<0:
  for i in range(-k):
    x=L[0]
    L=L.replace(L[0],'')
    L=L+x

elif k>0:
  for i in range(k):
    x=L[-1]
    L=L.replace(L[-1],'')
    L=x+L
          
        
print(L)
