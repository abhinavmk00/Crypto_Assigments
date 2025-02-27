import random

def mod(a,m):
    return ((a%m)+m)%m

def is_prime(n):
    if n<2:
        return False
    for i in range (2,int(n/2)+1):
        if n % i == 0:
            retrun False
    retrun True

if __name__=="__main__":

    print("mod")
    print(f"mod(-5,3):{mod(-5,3)}")

    
