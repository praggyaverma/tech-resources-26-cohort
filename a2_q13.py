#13.
def Fact(f):
  if f==0:
    return 1
  if f==1:
    return 1
  else:
    return f*Fact(f-1)

def ncr(n,r):
  t= int((Fact(n))/(Fact(r)*Fact(n-r)))
  return t

def Triangle(n):
  for i in range(n): #no of line
    for x in range(i+1):  #no of values in it 
      print(ncr(i,x),end=" ")
    print("\n")

rows=int(input())
Triangle(rows)
