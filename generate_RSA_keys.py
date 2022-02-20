import random
import math
#all RSA calculations are done here

#this function takes a number, checks if its prime or not, and then returns true or false
#using Fermets little theoren
def check_prime(p):
    '''Test if p is prime with Fermat\'s little theorem\n'''
    t = True
    for i in range(1, p):
        if pow(i, p-1, p) != 1:
            t = False
            break
    if not t:
        return t
    else:
        return t

#this function generated a random prime number between 100,000 and 1 million
def generate_prime():
    is_prime=False
    while is_prime == False:
        p=random.randrange(100000,1000000,7)
        is_prime=check_prime(p)
    return p

#this function  generates a prime number between two and PHI of the random numbers
#using Euclids GCD
def co_prime(t):
    is_coprime=False
    while not is_coprime:
        c=random.randrange(2,t)
        if(math.gcd(t,c)==1):# and check_prime(c)):
            is_coprime=True
    return c

#(p-1)*(q-1)
phi=0
product=0

#evaluates the value of N and PHI
def phi_coprime():
    global phi
    global product
    phi=0
    product=0
    p = generate_prime()
    q = generate_prime()
    while(p==q):
        p = generate_prime()
        q = generate_prime()

    phi=(p-1)*(q-1)
    product=p*q

#Extended GCD is used to generate teh private key based on the PHI and public key
def extended_gcd(a=1,b=1):
    if b==0:
        return(1,0,a)
    (x,y,d)=extended_gcd(b,a%b)
    return y, x - a//b*y , d

#Here all keys for message encryption and decryption are initialized
#using the functions above
def generate_keys():
    phi_coprime()
    global phi
    global product

    public_key=co_prime(phi)

    a,private_key,b=extended_gcd(phi,public_key)
    if private_key<0:
        private_key+=phi
    return product,public_key,private_key

#Here all keys for signature validation are initialized
#using the functions above
def generate_sign_keys():
    phi_coprime()
    global phi
    global product

    public_key=co_prime(phi)

    a,private_key,b=extended_gcd(phi,public_key)
    if private_key<0:
        private_key+=phi
    return phi,product,public_key,private_key