#12

def Fibonacci(n):
  for i in range(2,n+1):
    x=L[i-1]+L[i-2]
    L.append(x)
  return L

L=[0,1]

t=int(input())

Fibonacci(t*(t+1)//2)
x=1
for i in range(1,t+1):
  for j in range(1,i+1):
    print(L[x-1],end=" ")
    x=x+1
  print("\n")
