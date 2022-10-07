## You can use this function to return the list of prime numbers before number n
## in PYTHON

def sieve(n):
    l=[True for i in range(n+1)]
    l[0],l[1]=False,False
    for i in range(2,int(n**0.5)+1):
        if l[i]==True:
            for i in range(i*i,n+1,i):
                l[i]=False
    return l