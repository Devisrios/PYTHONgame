def main():
    n=int(input("Enter a number: "))
    sum1 = 0
    while(n > 0):
        sum1=sum1+n
        n=n-1
    print("The sum of first n natural numbers is"+str(sum1) )

if __name__ == '__main__':
    main()
