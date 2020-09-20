
def main():
    target = 1000
    total = 0
    
    for i in range(3,target):
        if ((i%3==0) or (i%5==0)):
            total+=i
    print("Total: " + str(total))
    
    return 0

main()
