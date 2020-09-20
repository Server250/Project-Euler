def evenFibLimit(a,b,limit):
    c=a+b

    if b<limit:
        return (int(not bool(c%2))*c)+evenFibLimit(b,c,limit)
    else:
        return 0

def main():
    print(str(evenFibLimit(1,1,4000000)))

main()
