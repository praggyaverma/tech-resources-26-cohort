#10.
n=int(input())

for i in range(n):
  for j in range(n):
    if i+j==2 or i-j==2 or j-i==2 or i+j==6:
      print("*", end="")
    else:
      print(end=" ")
  print()
