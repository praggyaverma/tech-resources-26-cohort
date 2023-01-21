#11

n=int(input())
x=1
for i in range(n+1):
  for j in range(i+1):
    print(x+i+j, end=" ")
  print("\n")
