import math

def isPrime(x):
    if (x<=1): return False
    if (x%2==0): return False

    for i in range(3,int(math.sqrt(x))+1,2):
        if x%i==0:
            return False

    return True

def main():
    target = int(input("Target: "))
    result = 0
    
    for i in range(int(math.sqrt(target))+1,2,-1):
        if (target%i==0):
            if (isPrime(i)):
                result = i
                break
                
    print("Result: " + str(result))
    return 0

main()
