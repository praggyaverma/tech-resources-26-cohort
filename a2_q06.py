#6.
n=int(input()) 
times=n//2+1 
space="  "
for i in range(1,n+1):
  if i>=1 and i<n//2+1:
    print("* "*(times+1-i),space,"* "*(times+1-i))
    space+=(space+space)
  elif i==n//2+1: # 3
    print("* ","  "*n,"* ")
  elif i>n//2+1 and i<=n: #4 5
    print("* " *(n-times),"  "*(n-i+1),"* "*(n-times))
    times-=1
