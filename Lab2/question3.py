def isprime(n):
 i=2
 while i<n:
        r=n%i
        if(r==0):
            print("{} is not a prime".format(n))
            return False

        i+=1

 print("{} is a prime".format(n))
 return True
while True:
 a=isprime(int(input("please enter a nember >>> ")))