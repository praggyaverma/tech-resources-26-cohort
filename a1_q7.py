n=int(input())
ans=0

org_p=1
inv_d=0
inv_p=0

while n!=0:
    org_d=n%10
    inv_d=org_p
    inv_p=org_d
    
    ans=ans + inv_d*(10**(inv_p-1))
    
    n//=10
    org_p+=1
    
print(ans)
