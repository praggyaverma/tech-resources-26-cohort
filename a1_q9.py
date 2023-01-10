n=int(input())
m=int(input())
hcf=1
for i in range(2,min(n,m)+1):
  if n%i==0 and m%i==0:
    hcf=i

print(hcf)
print(n*m//hcf)
