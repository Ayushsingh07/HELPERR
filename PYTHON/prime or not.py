#this func return true if the given number is prime or not effeciently
#only sieve algo is better than this
#if you want to check prime for small numbers , then this is the func you should use
def isprime(n):
    if n<2: return False
    if n==2 or n==3: return True
    if n%2==0 or n%3==0: return False
    for i in range(5,int(n**0.5)+1,6):
        if n%i==0 or n%(i+2)==0: return False 
    return True
print("Hello")#updation
